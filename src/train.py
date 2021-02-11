import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense, BatchNormalization, Bidirectional, ConvLSTM2D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from collections import Counter

context_length = 32
half_window = int(context_length / 2) 
num_mel_bands = 24

METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),
      tf.keras.metrics.AUC(name='auc'),
]

def trim_samples(features, labels):
    y = labels
    X = features
    shape = X.shape
    temp = X.reshape(shape[1], shape[0])
    return X, y, shape, temp

def validate_index(idx, labels):
    return not ((idx < 0) or (idx >= len(labels)) or (idx == 1))

def encode_triangular_filters(labels):
    segments = np.where(labels == 1)[0]
    for segment in segments:
        for i in range(segment + 4):
            if (i < len(labels)):
                labels[i] = 1
    return labels

def decode_triangular_filters(labels):
    weights = np.ones(labels.shape)
    actual = np.where(labels == 1)
    triangle = np.where(labels == 2)
    weights[actual] = 1
    return labels, weights

def oversample(features, labels):
    X, y, shape, temp = trim_samples(features, labels)
    y = LabelEncoder().fit_transform(labels)
    if (Counter(y)[1] <= 5):
        return X, y
    over = SMOTE(sampling_strategy=0.4)
    under = RandomUnderSampler()
    pipeline = Pipeline(steps=[('o', over), ('u', under)])
    X, y = under.fit_resample(temp, y)
    return X.reshape(shape[0], -1), y

def pad_song_features(features):
    return np.hstack((
        np.zeros((num_mel_bands, context_length)), 
        features,
        np.zeros((num_mel_bands, context_length))
    ))

def beat_windows(features, labels, weights, track, beats, X, y, w, idx):
    padded_features = pad_song_features(features)
    beats = int(beats)
    for k in range(0, beats - 1):
        if (k < len(labels)):
            features = padded_features[:, k:k + context_length + 1]
            # features = np.hamming(features)
            X.append(features)
            y.append(labels[k])
            w.append(weights[k])
            idx.append(track)
    return X, y, w, idx

def feature_pipeline(feature_list, label_list, training = True):
    X, y, w, idx = [], [], [], []
    for features, labels in zip(feature_list.iterrows(), label_list):
        _, features = features
        melspec = features["melspec"]
        if (training):
            labels = encode_triangular_filters(labels)
            # melspec, labels = oversample(melspec, labels)
        labels, weights = decode_triangular_filters(labels)
        beats = melspec.shape[1]
        X, y, w, idx = beat_windows(melspec, labels, weights, features["id"], beats, X, y, w, idx)
    X, y, w, idx = np.array(X), np.array(y), np.array(w), np.array(idx)
    X = np.expand_dims(X, axis=-1)
    return X, y, w, idx


def clean_labels(label_list):
    labels = []
    for label in label_list:
        temp = []
        for l in label:
            if (not np.isnan(l)):
                temp.append(l)
        temp = np.array(temp)
        labels.append(temp)
    return labels

def build_lstm():
    return  Sequential([
        Bidirectional(
            ConvLSTM2D(
                32, 
                kernel_size = (3, 3),
                padding = 'same',
                return_sequences = True
            )
        ),
        BatchNormalization(),
        Bidirectional(
            ConvLSTM2D(
                16, 
                kernel_size = (3, 3),
                padding = 'same',
                return_sequences = True
            )
        ),
        BatchNormalization(),
        Dropout(0.3),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])

def build_cnn(initial_bias):
    initial_bias = tf.keras.initializers.Constant(initial_bias)
    return Sequential([
        Conv2D(32, (4,4), input_shape=(num_mel_bands, context_length + 1, 1), activation='relu', padding="same"),
        MaxPooling2D(pool_size=(3, 3)),
        BatchNormalization(),
        Dropout(0.5),
        Conv2D(64, (2,2), activation='relu', padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        BatchNormalization(),
        Dropout(0.5),
        Dense(256, activation='relu'),
        Conv2D(16, (2,2), activation='relu', padding="same"),
        MaxPooling2D(pool_size=(2, 2)),
        BatchNormalization(),
        Dropout(0.5),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid', bias_initializer=initial_bias)
    ])

if __name__ == "__main__":
    feature_list = pd.read_pickle('dumps/sal_fifty/features_normalized.p')
    label_list = pd.read_pickle('dumps/sal_fifty/labels_normalized.p')

    labels = label_list.values.tolist()
    labels = clean_labels(labels)

    x_train, x_test, y_train, y_test = train_test_split(feature_list, labels, test_size=0.2, random_state=42)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

    x_train, y_train, w_train, idx_train = feature_pipeline(x_train, y_train)
    x_val, y_val, w_val, idx_val = feature_pipeline(x_test, y_test, False)
    x_test, y_test, w_test, idx_test = feature_pipeline(x_test, y_test, False)

    model = build_cnn()

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=METRICS)

    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='auc', patience=10, mode='max', restore_best_weights=True)

    results = model.evaluate(x_test, y_test, batch_size=128, verbose=0)
    print("Loss: {:0.4f}".format(results[0]))

    model.fit(
        x_train, 
        y_train, 
        batch_size=64,
        epochs=80, 
        shuffle=True,
        verbose=1,
        validation_data=(x_val, y_val),
        callbacks=[early_stopping]
    )    

    preds = model.predict(x_test, batch_size=1, verbose=1)

    score = model.evaluate(x_test, y_test)

    model.save_weights('models/sal_fifty/cnn')

    pickle.dump(preds, open('dumps/sal_fifty/preds.p', 'wb'))
    pickle.dump(x_train, open('dumps/sal_fifty/x_train.p', 'wb'))
    pickle.dump(y_train, open('dumps/sal_fifty/y_train.p', 'wb'))
    pickle.dump(w_train, open('dumps/sal_fifty/w_train.p', 'wb'))
    pickle.dump(idx_train, open('dumps/sal_fifty/idx_train.p', 'wb'))
    pickle.dump(x_test, open('dumps/sal_fifty/x_test.p', 'wb'))
    pickle.dump(y_test, open('dumps/sal_fifty/y_test.p', 'wb'))
    pickle.dump(w_test, open('dumps/sal_fifty/w_test.p', 'wb'))
    pickle.dump(idx_test, open('dumps/sal_fifty/idx_test.p', 'wb'))