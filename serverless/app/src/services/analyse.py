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
    'message': 'Analysing and detecting beats',
    'data': {
      'status': 'Analysing',
      'step': [3, 7],
      'filename': filename,
      'results': None
    }
  }))

def analyse_beats(y):
  # get beat times
  tempo, beats = librosa.beat.beat_track(y, sr=SR)
  times = librosa.frames_to_time(beats, sr=SR)
  melspec = extract_melspecs(y)
  # get beat-wise mel spectrograms
  sync = librosa.util.sync(melspec, beats)
  return sync, beats, times, tempo

def load_data(path):
  with open(path, 'rb') as f:
      data = pickle.load(f)
  return data

def save_results(prev, melspec, beats, times, tempo):
  filename = prev['filename']
  path = f'/mnt/access/data/metadata/{filename}.pkl'
  with open(path, 'wb') as f:
    pickle.dump({
      **prev,
      'melspec': melspec,
      'beats': beats,
      'times': times,
      'tempo': tempo
    }, f)
  return path

def analyse(event, context):
    # get payload
    payload = event['Input']['Payload']
    filename = payload['filename']
    emit_update(filename)

    data = load_data(payload['path'])

    melspec, beats, times, tempo = analyse_beats(data['mp3'])
    
    path = save_results(data, melspec, beats, times, tempo)
    return {
      'filename': filename,
      'path': path
    }
