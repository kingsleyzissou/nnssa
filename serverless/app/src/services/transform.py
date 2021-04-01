import boto3
import sys
import os
import pickle

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import librosa
from nnssa.constants import SR
from nnssa.spectrograms import extract_melspecs
from nnssa.sub_divisions import create_spec_windows, normalize

s3 = boto3.client('s3')

BUCKET_NAME = "nnssa-songs"
PRE_PROCESS_DIR = "pre_processing"

def pre_process(path):
    y, _ = librosa.load(path, sr=SR)
    tempo, beats = librosa.beat.beat_track(y, sr=SR)
    times = librosa.frames_to_time(beats, sr=SR)
    melspec = extract_melspecs(y)
    sync = librosa.util.sync(melspec, beats)
    melspec = create_spec_windows(melspec, 8, 4)
    melspec = normalize(melspec)
    return {
        'melspec': melspec,
        'beats': beats,
        'times': times,
        'tempo': tempo
    }


def transform(event, context):
    # get event
    key = event['Records'][0]['s3']['object']['key']
    filename = key.split('/')[1]

    temp = '/mnt/access/data/song/' + filename
    s3.download_file(BUCKET_NAME, key, temp)
    
    data = pre_process(temp)

    # filename = filename.split('.')[0] + '.pkl'
    # path = '/mnt/access/data/pre_processing/' + filename
    # pickle.dump(data, open(path, 'wb'))
    return data
