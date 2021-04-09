import boto3
import sys
import os
import pickle
import json

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import librosa
import music_tag
from nnssa.constants import SR
from nnssa.mqtt import connect

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
    'message': 'Decoding audio and extracting metadata',
    'data': {
      'status': 'Decoding',
      'step': [2, 7],
      'filename': filename,
      'results': None
    }
  }))

def extract_metadata(path):
  f = music_tag.load_file(path)
  return f['title'], f['artist'], f['album']

def download_song(songname, bucket, key):
  # download the item from the bucket
  temp = '/tmp/' + songname
  s3.download_file(bucket, key, temp)
  return temp

def save_results(songname, filename, key, mp3, title, artist, album):
  path = f'/mnt/access/data/metadata/{filename}.pkl'
  with open(path, 'wb') as f:
    pickle.dump({
      'songname': songname,
      'filename': filename,
      'key': key,
      'mp3': mp3,
      'title': title,
      'artist': artist,
      'album': album,
    }, f)
  return path

def decode(event, context):
    # get S3 uploaded file
    bucket = event['Input']['bucket']
    key = event['Input']['key']
    songname = os.path.basename(key)
    filename, _ = os.path.splitext(songname)
    emit_update(filename)

    temp = download_song(songname, bucket, key)
    y, _ = librosa.load(temp, sr=SR)
    title, artist, album = extract_metadata(temp)
    
    path = save_results(songname, filename, key, y, title, artist, album)
    return {
      'songname': songname,
      'filename': filename,
      'path': path
    }
