import os
import librosa.display
import matplotlib.pyplot as plt

def plot_mel_spec(data):
    """
    Helper function to plot mel spectrogram

    param: data - mel spectrogram data to be plotted
    """
    plt.figure(figsize=(25,10))
    librosa.display.specshow(data, sr=SR, x_axis="time", y_axis="mel")
    plt.colorbar(format='%+2.0f dB')