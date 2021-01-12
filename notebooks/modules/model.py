import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense

def build_model(shape):
    """
    Build the Neural Network Model and add
    the various layers for computation

    param: shape - the shape of the input layer
    """
    return Sequential([
        Conv2D(32, (3,3), input_shape=(shape[1], shape[2], 1), activation='relu'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.5),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(32000, activation='sigmoid')
    ])