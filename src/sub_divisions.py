import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler

from constants import *


def pad_melspec(melspec, padding, subdivision):
    """
    We pad the beginning and the end of
    each spectrogram with noise. We pad the
    mel spectrogram by the size of the context
    window - the size of the window to the left
    and right of a target label. This will enable
    to set all the labels with in that context window
    to positive
    
    melspec: the melspect to be padded
    padding: the amount by which we will pad the melspec
    """
    n_mel_bands = melspec.shape[0]
    return np.hstack((
        np.random.rand(n_mel_bands, padding)/100, 
        melspec,
        np.random.rand(n_mel_bands, padding * subdivision)/100,
    ))

def subdivide_frames(shape, subdivision):
    """
    This function helps get the shape of the
    desired output, if we want frames or beats
    the subdivision will be 1 and we return the shape
    of the labels.
    
    If we want bars, we subdived the labels into 4,
    we also pad the number of bars so it is a rounded
    number
    
    shape: the shape of the object as is
    subdivision: how the labels will be subdivided
    """
    shape = int(shape / subdivision)
    if subdivision == 1: return shape
    if shape % subdivision == 0: return shape
    return shape + (4 - (shape % 4))

def subdivide_labels(row, padding, subdivision = 0, sr=SR, hop_length=HOP_SIZE):
    """
    Polymorphic function to subdivide the labels so they match
    the size and shape of the input/features
    
    row: pandas row
    shape_field: the name of the field to be manipulated
    padding: amount of padding to add to the labels
    subdivision: 0 for frames, 1 for beats, 4 for bars
    """
    labels = np.zeros(row['Sub_Divisions'].shape[0])
    segment_frames = librosa.time_to_frames(row.Labels, sr=sr, hop_length=hop_length) + padding
    if (subdivision > 0):
        segment_frames = [np.argmin(np.abs(row.Beat_frames - s)) for s in segment_frames]
        segment_frames = [int(s/subdivision) for s in segment_frames]
    segment_frames = [s for s in segment_frames if s < len(labels)]
    labels[segment_frames] = 1
    return labels

def create_spec_windows(melspec, window, subdivision = 1):
    """
    This function is responsible for sub dividing the
    features into equally sized windows. This is required
    since CNN's require inputs to all have the same dimensions.
    
    This method is polymorphic in that it can subdived our melspectrograms
    into windows for frames, beats & bar subdivisions
    
    melspec: melspectrogram to be chunked
    window: the size of the window to chunk the melspectrograms
    subdivision: 1 for frames & beats, 4 for bars
    """
    subdivisions = subdivide_frames(melspec.shape[1], subdivision)
    padded_melspec = pad_melspec(melspec, window, subdivision)
    context_window = (window * 2) + 1
    bands = np.zeros(shape=(subdivisions, subdivision, melspec.shape[0], context_window))
    for s in range(subdivisions):
        context_range = (s * subdivision, s * subdivision + subdivision)
        bands[s, :, :, :] = [
            padded_melspec[:, i:(i + context_window)]
            for i in range(*context_range)
        ]
    return bands.swapaxes(1, 2)

def normalize(melspec):
    """
    Normalize the melspectrogram so that values are scaled
    such that the mean of each mel band is 0 and the standard
    deviation is 1. This is to ensure that very large values aren't
    overly represented in the data

    melspec: the melspectrogram to be normalized
    """
    shape = melspec.shape
    scaler = StandardScaler()
    scaled = scaler.fit_transform(melspec.reshape(shape[0], -1))
    return scaled.reshape(shape)