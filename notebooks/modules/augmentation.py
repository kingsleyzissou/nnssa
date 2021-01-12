import librosa
import numpy as np

def pitch_shift(y, sr=22050):
    """
    Change the pitch of the audio sample by
    randomly changing the pitch

    :param y - audio signal
    :param sr - sampling rate
    :return pitch shifted audio signal
    """
    pitch_samples = y.copy()
    bins = 12
    pitch = 2
    change = pitch * 2 * (np.random.uniform())
    return librosa.effects.pitch_shift(
        pitch_samples.astype("float64"), 
        sr=SR, 
        n_steps=change, 
        bins_per_octave=bins
    )

def add_noise(y):
    """
    Add noise to the audio signal

    :param y - audio signal
    :return audio signal with additional noise
    """
    y_noise = y.copy()
    # you can take any distribution from https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
    noise_amp = 0.005*np.random.uniform()*np.amax(y_noise)
    return y_noise.astype('float64') + noise_amp * np.random.normal(size=y_noise.shape[0])


def augment(y):
    """
    Change the dynamics of the audio signal

    :param y - audio signal
    :return dynamically changed audio signal
    """
    y_aug = y.copy()
    dyn_change = np.random.uniform(low=1.5,high=3)
    return y_aug * dyn_change