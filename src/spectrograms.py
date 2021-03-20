import numpy as np
import librosa
from .constants import SR, N_FFT, N_MELS, HOP_SIZE


def extract_melspecs(y, sr=SR, n_fft=N_FFT, n_mels=N_MELS, hop_length=HOP_SIZE):
    """
    Helper function to take a sample audio signal
    and convert the signal to a log mel spectrogram

    :param y - the processed audio signal
    :
    :return log_mel_spec - the log mel spectrogram
    """
    melspec = librosa.feature.melspectrogram(
        y, sr=sr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)
    # convert the mel spect to a logarithmic representation
    return librosa.power_to_db(melspec, ref=np.max)
