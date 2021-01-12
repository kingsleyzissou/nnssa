import librosa
import numpy as np

def extract_mel_specs(y, sr=22040, n_fft=2048, n_mels=64, hop_length=512):
    """
    Helper function to take a sample audio signal
    and convert the signal to a log mel spectrogram

    :param y - the processed audio signal
    :
    :return log_mel_spec - the log mel spectrogram
    """
    mel_spec = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft, n_mels=n_mels, hop_length=hop_length)
    ## convert the mel spect to a logarithmic representation
    return librosa.power_to_db(mel_spec, ref=np.max)