import boto3
import sys
import os
import pickle
import json

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import librosa
from nnssa.constants import SR
from nnssa.mqtt import connect
from nnssa.spectrograms import extract_melspecs
from nnssa.sub_divisions import create_spec_windows, normalize

s3 = boto3.client('s3')


def get_client():
  host = os.environ['MQTT_HOST']
  username = os.environ['MQTT_USERNAME']
  password = os.environ['MQTT_PASSWORD']
  port = int(os.environ['MQTT_PORT'])
  client_id = 'nnssa-transform'
  return connect(host, client_id, username, password, port)

def emit_update(filename):
  client = get_client()
  client.publish(f'nnssa/{filename}', json.dumps({
    'statusCode': 200,
    'message': 'Decoding audio',
    'data': {
      'status': 'decoding',
      'step': [1, 4],
      'filename': filename,
      'results': None
    }
  }))

def pre_process(path):
  # process the song and
  # get bar subdivisions
  y, _ = librosa.load(path, sr=SR)
  tempo, beats = librosa.beat.beat_track(y, sr=SR)
  times = librosa.frames_to_time(beats, sr=SR)
  melspec = extract_melspecs(y)
  sync = librosa.util.sync(melspec, beats)
  melspec = create_spec_windows(melspec, 8, 4)
  melspec = normalize(melspec)
  return melspec, beats, times, tempo

def download_song(songname, bucket, key):
  # download the item from the bucket
  temp = '/tmp/' + songname
  s3.download_file(bucket, key, temp)
  return temp

def save_results(songname, filename, melspec, beats, times, tempo):
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
  return path

def transform(event, context):
    # get S3 uploaded file
    bucket = event['Input']['bucket']
    key = event['Input']['key']
    songname = os.path.basename(key)
    filename, _ = os.path.splitext(songname)
    emit_update(filename)

    temp = download_song(songname, bucket, key)
    melspec, beats, times, tempo = pre_process(temp)
    path = save_results(songname, filename, melspec, beats, times, tempo)
    return {
      'songname': songname,
      'filename': filename,
      'path': path
    }
