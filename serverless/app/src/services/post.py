import sys
import os
import pickle
import boto3
import json

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

from nnssa.mqtt import connect
import numpy as np

def get_client():
  host = os.environ['MQTT_HOST']
  username = os.environ['MQTT_USERNAME']
  password = os.environ['MQTT_PASSWORD']
  port = int(os.environ['MQTT_PORT'])
  client_id = 'nnssa-predict'
  return connect(host, client_id, username, password, port)

def emit_update(filename):
  client = get_client()
  client.publish(f'nnssa/{filename}', json.dumps({
    'statusCode': 200,
    'message': 'Processing predictions and calculating onset times',
    'data': {
      'status': 'Processing',
      'step': [6, 7],
      'filename': filename,
      'results': None
    }
  }))

def load_data(payload):
  with open(payload['path'], 'rb') as f:
    data = pickle.load(f)

  preds = np.load(payload['predictions'])
  return data, preds

def calculate_sections(preds, beat_times):
  sections = (np.where(preds == 1)[0]) * 4
  sections = [p for p in sections if p < len(beat_times)]
  sections = beat_times[sections]
  return sections

def save_results(filename, sections):
  path = f'/mnt/access/data/results/{filename}.npy'
  np.save(path, sections)

def post(event, context):
  # get payload
  payload = event['Input']['Payload']
  filename = payload['filename']
  emit_update(filename)
  
  data, preds = load_data(payload)
  preds = np.asarray([1 if x > 0.95 else 0 for x in preds])
  sections = calculate_sections(preds, data['times'])
  save_results(filename, sections)
  return {
    **payload,
    'result': sections.tolist(),
    'title': str(data['title']),
    'artist': str(data['artist']),
    'album': str(data['album']),
    'tempo': data['tempo'],
    'key': data['key']
  }
