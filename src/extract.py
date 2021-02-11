import numpy as np
import librosa
import pickle
import os
import pandas as pd
from tqdm import tqdm

SR = 22050
SALAMI_LABEL_DIR = "datasets/salami/annotations/"
HARMONIX_LABEL_DIR = "datasets/harmonix/segments/"

def extract_mel_specs(y, sr=22040, n_fft=2048, n_mels=64, hop_length=512):
    """
    Helper function to take a sample audio signal
    and convert the signal to a log mel spectrogram

    :param y - the processed audio signal
    :
    :return log_mel_spec - the log mel spectrogram
    """
    mel_spec = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)
    ## convert the mel spect to a logarithmic representation
    return librosa.power_to_db(mel_spec, ref=np.max)

def filter_silence(frame):
    frame = frame[frame[1] != "Silence"]
    frame = frame[frame[1] != "End"]
    frame = frame[frame[1] != "Z"]
    return frame


def load_labels(option_one, option_two):
    """
    Helper function to load labels
    from file, the file accepts two options,
    since the SALAMI database has multiple
    annotations per song

    :param option_one - first annotated file option
    :param option_two - second annotated file option 
    """
    if(os.path.exists(option_one)):
            t = pd.read_table(option_one, header=None)
            t = filter_silence(t)
            return t.iloc[:, 0].values
    if (os.path.exists(option_two)):
        t = pd.read_table(option_two, header=None)
        t = filter_silence(t)
        return t.iloc[:, 0].values
    return []

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
                mel = extract_mel_specs(mp3, n_mels=24, sr=SR)
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

def normalized_melbands(melspec):
    normalized_bands = []
    for band in melspec:
        normalized_bands.append(normalize_band(band))
    return np.asarray(normalized_bands)


def normalize_band(band):
    mean = band.mean(axis=0)
    std = band.std(axis=0)
    return (band - mean) / std


if __name__ == "__main__":
    # harmonix = pd.read_csv("datasets/harmonix/metadata.csv")
    songs = pickle.load(open('dumps/sal_fifty/salami_fifty.p', 'rb'))

    features, labels = load_beat_annotations(songs)
    
    labels = match_labels_to_beats_harmonix(features, labels)

    features = pd.DataFrame(features)
    labels = pd.DataFrame(labels)

    features.to_pickle("dumps/sal_fifty/features_normalized.p")
    labels.to_pickle("dumps/sal_fifty/labels_normalized.p")