import sys
import os
import pickle

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import tensorflow as tf
import numpy as np

def predict(data, context):
    # get event
    filename = 'billionaire.pkl'

    # data = pickle.load(open('/mnt/access/data/pre_processing/' + filename, 'rb'))

    model = tf.keras.models.load_model('/mnt/access/model/binary_model.h5')
    predictions = model.predict(data['melspec'])

    # filename = filename.split('.')[0] + '.npy'
    # path = '/mnt/access/data/predictions/' + filename
    # np.save(path, preds)
    return {
      *data,
      'predictions': predictions
    }