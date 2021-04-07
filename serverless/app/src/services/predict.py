import sys
import os
import pickle
import json
import boto3

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

from nnssa.mqtt import connect
import tensorflow as tf
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
    'message': 'Making prediction',
    'data': {
      'status': 'predicting',
      'step': [2, 4],
      'filename': filename,
      'results': None
    }
  }))

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
  emit_update(filename)

  data = load_data(payload['path'])
  # build model
  model = tf.keras.models.load_model('/mnt/access/model/binary_model.h5')
  # make predictions
  predictions = model.predict(data['melspec'])
  path = save_results(filename, predictions)
  payload['predictions'] = path
  return payload