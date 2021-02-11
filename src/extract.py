import numpy as np
import librosa
import pickle
import pandas as pd
from tqdm import tqdm
from utils.utils import load_labels, extract_melspecs, normalized_melbands

SR = 22050
SALAMI_LABEL_DIR = "datasets/salami/annotations/"
HARMONIX_LABEL_DIR = "datasets/harmonix/segments/"

def load_beat_annotations(sal_fifty):
    features = []
    labels = []
    for item in tqdm(sal_fifty, total=len(sal_fifty)):
        """ iterate through dataframe"""
        mp3 = item["mp3"]
        file_name = str(item["SONG_ID"])
        ## we have two label options for SALAMI database
        file_one = HARMONIX_LABEL_DIR + file_name + "/parsed/textfile1_uppercase.txt"
        file_two = SALAMI_LABEL_DIR + file_name + "/parsed/textfile2_uppercase.txt"
        annotations = load_labels(file_one, file_two)
        # check if any labels were found
        if (len(annotations) > 0):
                labels.append(annotations)
                mel = extract_melspecs(mp3, n_mels=24, sr=SR)
                _, beats = librosa.beat.beat_track(mp3, sr=SR)
                sync = librosa.util.sync(mel, beats)
                item = {
                    "id": file_name,
                    "beat_times": librosa.frames_to_time(beats),
                    "beat_frames": beats,
                    "beat_count": sync.shape[1],
                    "melspec": normalized_melbands(sync),
                    "segments": annotations
                }
                features.append(item)
    return features, labels

def load_harmonix_annotations(file):
    annotations = pd.read_table(file, header=None, sep=' ', names=['Time', 'Section'])
    annotations = annotations.drop(['Section'], axis=1)
    annotations = np.squeeze(annotations.values)
    return annotations

def load_harmonix(harmonix):
    features = []
    labels = []
    for item in tqdm(harmonix, total=len(harmonix)):
        """ iterate through dataframe"""
        file_name = item
        mel = np.load('downloads/melspecs/' + file_name + '-mel.npy')
        beat_times = pd.read_table('datasets/harmonix/beats_and_downbeats/' + file_name + '.txt', header=None)[0]
        beat_frames = librosa.time_to_frames(beat_times, sr=SR)
        sync = librosa.util.sync(mel, beat_frames)   
        ## we have two label options for SALAMI database
        file_one = HARMONIX_LABEL_DIR + file_name + ".txt"
        annotations = load_harmonix_annotations(file_one)
        labels.append(annotations)
        item = {
            "id": file_name,
            "beat_times": beat_times,
            "beat_frames": beat_frames,
            "beat_count": sync.shape[1],
            "melspec": normalized_melbands(sync),
            "segments": annotations
        }
        features.append(item)
    return features, labels


def match_labels_to_beats_harmonix(feature_list, label_list):
    labels = []
    for f,l in zip(feature_list, label_list):
        beats = f["beat_count"]
        label_vec = np.zeros(beats)
        beat_frames = f["beat_frames"]
        segment_frames = librosa.time_to_frames(l, sr=SR)
        for segment in segment_frames:
            min = np.abs(beat_frames - segment)
            closest_beat = np.argmin(min)
            if (closest_beat < beats):
                label_vec[closest_beat] = 1
        labels.append(label_vec)
    return labels




if __name__ == "__main__":
    # harmonix = pd.read_csv("datasets/harmonix/metadata.csv")
    songs = pickle.load(open('dumps/sal_fifty/salami_fifty.p', 'rb'))

    features, labels = load_beat_annotations(songs)
    
    labels = match_labels_to_beats_harmonix(features, labels)

    features = pd.DataFrame(features)
    labels = pd.DataFrame(labels)

    features.to_pickle("dumps/sal_fifty/features_normalized.p")
    labels.to_pickle("dumps/sal_fifty/labels_normalized.p")