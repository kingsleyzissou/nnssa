import os
import librosa
import pickle

def load_audio(filepath, sr=22050):
    if (os.path.exists(filepath)):
        mp3, _ = librosa.load(filepath, sr=sr)
        return mp3
    return []