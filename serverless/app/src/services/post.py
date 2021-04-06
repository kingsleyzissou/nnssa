import sys
import os
import pickle
import boto3
import json

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import numpy as np

def emit_update(filename):
  ## TODO add this to package
  client = boto3.client('lambda')
  client.invoke(
    FunctionName = os.environ['NOTIFY_LAMBDA'],
    InvocationType = 'Event',
    Payload = json.dumps({
      'statusCode': 200,
      'message': 'Processing predictions',
      'data': {
        'status': 'processing',
        'step': [3, 4],
        'filename': filename,
        'results': None
      }
    })
  )

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
  # emit_update(filename)
  
  data, preds = load_data(payload)
  preds = np.asarray([1 if x > 0.95 else 0 for x in preds])
  sections = calculate_sections(preds, data['times'])
  save_results(filename, sections)
  payload['result'] = sections.tolist()
  return payload
