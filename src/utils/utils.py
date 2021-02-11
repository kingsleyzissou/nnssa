import os
import pandas as pd
import numpy as np
import librosa

def filter_silence(frame):
    frame = frame[frame[1] != "Silence"]
    frame = frame[frame[1] != "End"]
    frame = frame[frame[1] != "Z"]
    return frame


def load_labels(option_one, option_two):
    """
    Helper function to load labels
    from file, the file accepts two options,
    since the SALAMI database has multiple
    annotations per song

    :param option_one - first annotated file option
    :param option_two - second annotated file option 
    """
    if(os.path.exists(option_one)):
            t = pd.read_table(option_one, header=None)
            t = filter_silence(t)
            return t.iloc[:, 0].values
    if (os.path.exists(option_two)):
        t = pd.read_table(option_two, header=None)
        t = filter_silence(t)
        return t.iloc[:, 0].values
    return []

def extract_melspecs(y, sr=22040, n_fft=2048, n_mels=64, hop_length=512):
    """
    Helper function to take a sample audio signal
    and convert the signal to a log mel spectrogram

    :param y - the processed audio signal
    :
    :return log_mel_spec - the log mel spectrogram
    """
    melspec = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)
    ## convert the mel spect to a logarithmic representation
    return librosa.power_to_db(melspec, ref=np.max)

def normalized_melbands(melspec):
    normalized_bands = []
    for band in melspec:
        normalized_bands.append(normalize_band(band))
    return np.asarray(normalized_bands)


def normalize_band(band):
    mean = band.mean(axis=0)
    std = band.std(axis=0)
    return (band - mean) / std