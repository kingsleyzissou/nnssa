import sys
import os
import pickle
import json
import boto3

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import tensorflow as tf
import numpy as np

def emit_update(filename):
  ## TODO add this to package
  client = boto3.client('lambda')
  client.invoke(
    FunctionName = os.environ['NOTIFY_LAMBDA'],
    InvocationType = 'Event',
    Payload = json.dumps({
      'statusCode': 200,
      'message': 'Making prediction',
      'data': {
        'status': 'predicting',
        'step': [2, 4],
        'filename': filename,
        'results': None
      }
    })
  )

def load_data(path):
  with open(path, 'rb') as f:
      data = pickle.load(f)
  return data

def save_results(filename, predictions):
  path = f'/mnt/access/data/predictions/{filename}.npy'
  np.save(path, predictions)
  return path

def predict(event, context):
  # get payload
  payload = event['Input']['Payload']
  filename = payload['filename']
  # emit_update(filename)

  data = load_data(payload['path'])
  # build model
  model = tf.keras.models.load_model('/mnt/access/model/binary_model.h5')
  # make predictions
  predictions = model.predict(data['melspec'])
  path = save_results(filename, predictions)
  payload['predictions'] = path
  return payload