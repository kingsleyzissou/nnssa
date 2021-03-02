import os
import pandas as pd
import numpy as np
import librosa

CONTEXT_WINDOW = 17

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

def pad_melspec(n_mel_bands, padding, melspec):
    return np.hstack((
        np.zeros((n_mel_bands, padding)), 
        melspec,
        np.zeros((n_mel_bands, padding * 10))
    ))

def beats_to_bars(melspec):
    beats = melspec.shape[1]
    bars = int(beats / 4)
    bars = bars if bars % 4 == 1 else bars + (5 - (bars % 4))
    bands = np.zeros(shape=(bars, 4, melspec.shape[0], CONTEXT_WINDOW))
    padded_melspec = pad_melspec(melspec.shape[0], 8, melspec)
    for bar in range(bars):
        b = []
        for beat in range(bar * 4, bar * 4 + 4):
            mel = padded_melspec[:, beat:beat + CONTEXT_WINDOW]
            b.append(mel)
            # print(mel.shape)
            # mel = normalized_melbands(mel)
            # bands[:, beat, :] = mel
        # print(np.shape(b))
        bands[bar, :, :, :] = b
    return bands.swapaxes(1, 2)