import os

SR = 22050
N_FFT = 2048
N_MELS = 80
HOP_SIZE = 1024
CONTEXT_WINDOW = 33

METADATA_DIR = os.path.join('data', '00_Raw_Data', 'metadata')
AUDIO_DIR = os.path.join('data', '00_Raw_Data', 'audio')
INTER_DIR = os.path.join('data', '01_Intermediate_Data')
ANNOTATIONS_DIR = os.path.join('data', '02_Annotations')
BEATS_DIR = os.path.join('data', '03_Beat_Times')
MELS_DIR = os.path.join('data', '04_Mel_Spectrograms')
SUB_DIVS_DIR = os.path.join('data', '05_Sub_Divisions')

# Harmonix dataset
HARMONIX = os.path.join(METADATA_DIR, 'harmonix.csv')
HARMONIX_LABELS = os.path.join(ANNOTATIONS_DIR, 'harmonix')
HARMONIX_BEATS = os.path.join(BEATS_DIR, 'harmonix')
HARMONIX_MELS = os.path.join(MELS_DIR, 'harmonix')

# Salami dataset
SALAMI = os.path.join(METADATA_DIR, 'salami.csv')
SALAMI_LABELS = os.path.join(ANNOTATIONS_DIR, 'salami')
SALAMI_BEATS = os.path.join(BEATS_DIR, 'salami')
SALAMI_MELS = os.path.join(MELS_DIR, 'salami')