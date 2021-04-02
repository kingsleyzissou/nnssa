import sys
import os
import pickle

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import tensorflow as tf
import numpy as np

def predict(event, context):
    # get payload
    payload = event['Input']['Payload']

    with open(payload['path'], 'rb') as f:
      data = pickle.load(f)

    # build model
    model = tf.keras.models.load_model('/mnt/access/model/binary_model.h5')
    # make predictions
    predictions = model.predict(data['melspec'])
    
    filename = payload['filename']
    path = f'/mnt/access/data/predictions/{filename}.npy'
    np.save(path, predictions)

    payload['predictions'] = path
    return payload