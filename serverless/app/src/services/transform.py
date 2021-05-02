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
from nnssa.sub_divisions import create_spec_windows, normalize


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
    'message': 'Generating mel spectrogram',
    'data': {
      'status': 'Transforming',
      'step': [4, 7],
      'filename': filename,
      'results': None
    }
  }))

def transform_beats(melspec):
  # get beat times
  melspec = create_spec_windows(melspec, 16, 4)
  return normalize(melspec)

def load_data(path):
  with open(path, 'rb') as f:
      data = pickle.load(f)
  return data

def save_results(prev, melspec):
  filename = prev['filename']
  path = f'/mnt/access/data/metadata/{filename}.pkl'
  with open(path, 'wb') as f:
    pickle.dump({
      **prev,
      'melspec': melspec
    }, f)
  return path

def transform(event, context):
    # get payload
    payload = event['Input']['Payload']
    filename = payload['filename']
    emit_update(filename)

    data = load_data(payload['path'])

    melspec = transform_beats(data['melspec'])
    
    path = save_results(data, melspec)
    return {
      'filename': filename,
      'path': path
    }
