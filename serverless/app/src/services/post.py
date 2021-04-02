import sys
import os
import pickle

## Mount EFS path before attempting 
## to import the next dependencies
sys.path.append('/mnt/access/pkgs')

import numpy as np

def post(event, context):
    # get payload
    payload = event['Input']['Payload']
    
    with open(payload['path'], 'rb') as f:
      data = pickle.load(f)

    preds = np.load(payload['predictions'])
    preds = np.asarray([1 if x > 0.95 else 0 for x in preds])
  
    sections = (np.where(preds == 1)[0]) * 4
    sections = [p for p in sections if p < len(data['times'])]
    sections = data['times'][sections]
    
    filename = payload['filename']
    path = f'/mnt/access/data/results/{filename}.npy'
    np.save(path, sections)
