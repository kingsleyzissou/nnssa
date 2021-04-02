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

def pre_process(path):
    y, _ = librosa.load(path, sr=SR)
    tempo, beats = librosa.beat.beat_track(y, sr=SR)
    times = librosa.frames_to_time(beats, sr=SR)
    melspec = extract_melspecs(y)
    sync = librosa.util.sync(melspec, beats)
    melspec = create_spec_windows(melspec, 8, 4)
    melspec = normalize(melspec)
    return melspec, beats, times, tempo


def transform(event, context):
    # get S3 uploaded file
    bucket = event['Input']['bucket']
    key = event['Input']['key']
    songname = key.split('/')[1]
    filename = songname.split('.')[0]

    # download the item from the bucket
    temp = '/tmp/' + songname
    s3.download_file(bucket, key, temp)

    # process the song and
    # get bar subdivisions
    melspec, beats, times, tempo = pre_process(temp)

    path = f'/mnt/access/data/decoded/{filename}.pkl'

    with open(path, 'wb') as f:
      pickle.dump({
        'songname': songname,
        'filename': filename,
        'melspec': melspec,
        'beats': beats,
        'times': times,
        'tempo': tempo
      }, f)

    return {
      'songname': songname,
      'filename': filename,
      'path': path
    }
