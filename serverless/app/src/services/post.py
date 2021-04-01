import sys
import os
import pickle

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import numpy as np

def post(event, context):
    # get event
    filename = 'billionaire.pkl'

    data = pickle.load(open('/mnt/access/data/pre_processing/' + filename, 'rb'))
    preds = np.load('/mnt/access/data/predictions/billionaire.npy')
    
    beat_times = data['times']

    preds = np.asarray([1 if x > 0.95 else 0 for x in preds])
    pred_sections = (np.where(preds == 1)[0]) * 4
    pred_sections = [p for p in pred_sections if p < len(beat_times)]
    sections = beat_times[pred_sections]
    
    path = '/mnt/access/data/results/billionaire.npy'
    np.save(path, sections)
