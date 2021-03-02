import numpy as np
import pandas as pd
import pickle
import peakutils
import mir_eval
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense, BatchNormalization, Bidirectional, ConvLSTM2D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.utils import compute_class_weight
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from collections import Counter

from tensorflow.python.ops.gen_array_ops import empty

context_length = 17 
half_window = int(context_length / 2) 
num_mel_bands = 80

EPOCHS = 50
BATCH_SIZE = 32
UNDER_SAMPLING = None
OVER_SMOTE = None

METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy', threshold=0.15),
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
        for i in range(segment - 3, segment + 3):
            if (i > 0 and i < len(labels)):
                if(i != segment):
                    labels[i] = 2
    return labels

def decode_triangular_filters(labels):
    weights = np.ones(labels.shape)
    actual = np.where(labels == 1)
    triangle = np.where(labels == 2)
    weights[actual] = 1
    labels[triangle] = 1
    weights[triangle] = 0.5
    return labels, weights

def oversample(features, labels):
    X, y, shape, temp = trim_samples(features, labels)
    y = LabelEncoder().fit_transform(labels)
    if (Counter(y)[1] <= 5):
        return X, y
    over = SMOTE(sampling_strategy=OVER_SMOTE)
    under = RandomUnderSampler(sampling_strategy=UNDER_SAMPLING)
    pipeline = Pipeline(steps=[('o', over), ('u', under)])
    X, y = pipeline.fit_resample(temp, y)
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
        weights = np.ones(labels.shape)
        if (training):
            # labels = encode_triangular_filters(labels)
            # labels, weights = label_smear(labels, weights)
            melspec, labels = oversample(melspec, labels)
            weights = np.ones(labels.shape)
        # labels, weights = decode_triangular_filters(labels)
        beats = melspec.shape[1]
        X, y, w, idx = beat_windows(melspec, labels, weights, features["id"], beats, X, y, w, idx)
    X, y, w, idx = np.array(X), np.array(y), np.array(w), np.array(idx)
    # X = np.expand_dims(X, axis=-1)
    return X, y, w, idx

def label_smear(labels, weights):
    truth = np.where(labels == 1)[0]
    weights[truth] = 2
    labels[truth[:-1] + 1] = 1
    # weights[truth[:-1] + 1] = 0.5
    labels[truth[1:] - 1] = 1
    # weights[truth[1:] - 1] = 0.5
    labels[truth[:-1] + 2] = 1
    weights[truth[:-1] + 2] = 0.5
    labels[truth[1:] - 2] = 1
    weights[truth[1:] - 2] = 0.5
    return labels, weights

def oversample_bars(features, labels):
    X, y = features, labels
    shape = X.shape
    temp = X.reshape(shape[0], -1)
    if (Counter(y)[1] <= 5):
        return X, y
    over = SMOTE(sampling_strategy=0.3)
    under = RandomUnderSampler(sampling_strategy=0.6)
    pipeline = Pipeline(steps=[('o', over), ('u', under)])
    X, y = under.fit_resample(temp, y)
    return X.reshape(-1, shape[1], 4, 9), y

def label_smear_bars(bars, labels, weights):
    truth = np.where(labels == 1)[0]
    weights[truth] = 2
    labels[truth[:-1] + 1] = 1
    weights[truth[:-1] + 1] = 0.5
    labels[truth[1:] - 1] = 1
    weights[truth[1:] - 1] = 0.5
    return bars, labels, weights

def feature_pipeline_bars(feature_list, label_list, training = True):
    X, y, w, idx = [], [], [], []
    for features, labels in zip(feature_list.iterrows(), label_list):
        _, features = features
        bars = features["melspec"]
        weights = np.ones(labels.shape)
        # quit()
        if (training):
            # bars, labels = oversample_bars(bars, labels)
            # weights = np.ones(labels.shape)
            bars, labels, weights = label_smear_bars(bars, labels, weights)
        for i, bar in enumerate(bars):
            X.append(bar)
            y.append(labels[i])
            idx.append(features["id"])
            w.append(weights[i])
        # X, y, w, idx = beat_windows(melspec, labels, features["id"], beats, X, y, idx)
    X, y, w, idx = np.array(X), np.array(y), np.array(w), np.array(idx)
    return X, y, w, idx

def clean_labels(label_list):
    labels = []
    for label in label_list:
        temp = []
        for l in label:
            if (not np.isnan(l)):
                temp.append(int(l))
        temp = np.array(temp)
        labels.append(temp)
    return labels

# def build_cnn(initial_bias):
#     initial_bias = tf.keras.initializers.Constant(initial_bias)
#     initializer = tf.keras.initializers.HeNormal()
#     return Sequential([
#         Conv2D(64, (8,6), input_shape=(num_mel_bands, context_length + 1, 1), activation='relu', kernel_initializer=initializer, padding="same"),
#         MaxPooling2D(pool_size=(5, 2)),
#         BatchNormalization(),
#         Dropout(0.5),
#         Conv2D(128, (6,4), activation='relu', padding="same", kernel_initializer=initializer),
#         MaxPooling2D(pool_size=(2, 2)),
#         BatchNormalization(),
#         Conv2D(32, (2,2), activation='relu', padding="same"),
#         MaxPooling2D(pool_size=(2, 2)),
#         BatchNormalization(),
#         Dense(128, activation='relu'),
#         Dropout(0.5),
#         Flatten(),
#         Dense(256, activation='sigmoid'),
#         Dropout(0.5),
#         Dense(1, activation='sigmoid', bias_initializer=initial_bias)
#     ])

def build_cnn(initial_bias):
    initial_bias = tf.keras.initializers.Constant(initial_bias)
    initializer = tf.keras.initializers.HeNormal()
    return Sequential([
        Conv2D(32, (8,6), input_shape=(num_mel_bands, 4, context_length), activation='relu', kernel_initializer=initializer, padding="same"),
        MaxPooling2D(pool_size=(5, 2)),
        BatchNormalization(),
        Dropout(0.5),
        Conv2D(64, (6,4), activation='relu', padding="same", kernel_initializer=initializer),
        MaxPooling2D(pool_size=(2, 2)),
        BatchNormalization(),
        Dropout(0.5),
        Flatten(),
        Dense(256, activation='sigmoid'),
        Dropout(0.5),
        Dense(1, activation='sigmoid', bias_initializer=initial_bias)
    ])

def post_processing(preds_track):
    """
    Post processing of prediction probabilities, applies smoothing
    window and emphasizes beats by multiplying with running avarage.
    :param preds_track: CNN predictions per beat
    :return: post-processed predictions

    This function was taken from:
    https://github.com/mleimeister/SegmentationCNN/blob/a9a35b5c4ce4ca1f968fd333535d534ba6b7b857/Python/evaluation.py#L41
    """

    # smoothing
    preds_track = np.convolve(preds_track, np.hamming(4) / np.sum(np.hamming(4)), 'same')

    # emphasize peaks
    preds_track = np.multiply(preds_track,
                              np.convolve(preds_track, np.hamming(32) / np.sum(np.hamming(32)), 'same'))

    # unit maximum
    preds_track /= np.max(preds_track)

    return preds_track

def evaluate(feature_list, preds, y_test, idx_test, bars=False):
    unique = np.unique(idx_test)

    features = feature_list[feature_list["id"].isin(unique)]

    f_score, precision, recall = [], [], []

    for _, item in features.iterrows():
        bpm = item["bpm"]
        bps = bpm / 60
        window = (1 / bps) * 8

        window = 3
        p = np.asarray(preds[idx_test == item["id"]])
        y = np.asarray(y_test[idx_test == item["id"]])
        p = np.asarray([1 if x > 0.25 else 0 for x in p])

        segments = item["segments"]

        beat_times = np.asarray(item["beat_times"])

        p = post_processing(p)
        peaks = peakutils.indexes(p, min_dist=6, thres=0.05)

        if (bars):
            peaks = [(p * 4) for p in peaks if (p * 4) < len(beat_times)]
        beats = beat_times[peaks]

        f, p, r = mir_eval.onset.f_measure(segments, beats, window=window)

        f_score.append(f)
        precision.append(p)
        recall.append(r)

    f_score = np.mean(np.asarray(f_score))
    precision = np.mean(np.asarray(precision))
    recall = np.mean(np.asarray(recall))

    return f_score, precision, recall

if __name__ == "__main__":
    feature_list = pd.read_pickle('dumps/bars/features_normalized.p')
    label_list = pd.read_pickle('dumps/bars/labels_normalized.p')
    # preds = pickle.load(open('dumps/bars/preds.p', 'rb'))
    # x_train = pickle.load(open('dumps/bars/x_train.p', 'rb'))
    # y_train = pickle.load(open('dumps/bars/y_train.p', 'rb'))
    # w_train = pickle.load(open('dumps/bars/w_train.p', 'rb'))
    # idx_train = pickle.load(open('dumps/bars/idx_train.p', 'rb'))
    # x_test = pickle.load(open('dumps/bars/x_test.p', 'rb'))
    # y_test = pickle.load(open('dumps/bars/y_test.p', 'rb'))
    # w_test = pickle.load(open('dumps/bars/w_test.p', 'rb'))
    # idx_test = pickle.load(open('dumps/bars/idx_test.p', 'rb'))
    # x_val = pickle.load(open('dumps/bars/x_val.p', 'rb'))
    # y_val = pickle.load(open('dumps/bars/y_val.p', 'rb'))

    feature_list = feature_list.head(50)
    label_list = label_list.head(50)

    labels = label_list.values.tolist()
    labels = clean_labels(labels)

    x_train, x_test, y_train, y_test = train_test_split(feature_list, labels, test_size=0.2, random_state=42)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

    x_train, y_train, w_train, idx_train = feature_pipeline_bars(x_train, y_train)
    x_val, y_val, w_val, idx_val = feature_pipeline_bars(x_test, y_test, False)
    x_test, y_test, w_test, idx_test = feature_pipeline_bars(x_test, y_test, False)

    count = np.bincount(y_train)
    neg, pos = count[0], count[1]
    total = neg + pos
    initial_bias = np.log([pos/neg])

    model = build_cnn(initial_bias)

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=METRICS)

    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_auc', patience=10, mode='max', restore_best_weights=True)

    results = model.evaluate(x_test, y_test, batch_size=BATCH_SIZE, verbose=0)
    print("Loss: {:0.4f}".format(results[0]))

    model.fit(
        x_train, 
        y_train, 
        batch_size=BATCH_SIZE,
        epochs=EPOCHS, 
        shuffle=True,
        verbose=1,
        sample_weight=w_train,
        validation_data=(x_val, y_val),
        callbacks=[early_stopping]
    )    

    preds = model.predict(x_test, batch_size=1, verbose=1)

    score = model.evaluate(x_test, y_test)

    # model.save_weights('models/sal_fifty/cnn')

    # pickle.dump(preds, open('dumps/bars/preds.p', 'wb'))
    # pickle.dump(x_train, open('dumps/bars/x_train.p', 'wb'))
    # pickle.dump(y_train, open('dumps/bars/y_train.p', 'wb'))
    # pickle.dump(w_train, open('dumps/bars/w_train.p', 'wb'))
    # pickle.dump(idx_train, open('dumps/bars/idx_train.p', 'wb'))
    # pickle.dump(x_test, open('dumps/bars/x_test.p', 'wb'))
    # pickle.dump(y_test, open('dumps/bars/y_test.p', 'wb'))
    # pickle.dump(w_test, open('dumps/bars/w_test.p', 'wb'))
    # pickle.dump(idx_test, open('dumps/bars/idx_test.p', 'wb'))
    # pickle.dump(x_val, open('dumps/bars/x_val.p', 'wb'))
    # pickle.dump(y_val, open('dumps/bars/y_val.p', 'wb'))

    y_pred = [1 if (p > 0.25) else 0 for p in preds]
    y_pred = np.asarray(y_pred)

    print(classification_report(y_test, y_pred))
    
    f_score, precision, recall = evaluate(feature_list, preds, y_test, idx_test, True)

    print("F-score: ", f_score)
    print("Precision: ", precision)
    print("Recall: ", recall)

    # quit()

    df_metrics = pd.read_csv("results/results.csv")
    # columns = df_metrics.columns

    columns=["n_mels", "window_type", "window_length", "oversampling", "undersampling", "smote", "label_smearing", "f_score", "precision", "recall", "threshold", "optimizer", "epochs", "batch_size"]
    results = [[num_mel_bands, "bars", context_length, None, UNDER_SAMPLING, OVER_SMOTE, "+/- 1", f_score, precision, recall, 3, "adam", EPOCHS, BATCH_SIZE]]

    df_metrics = df_metrics.append(pd.DataFrame(results, columns=columns))

    df_metrics.to_csv("results/results.csv", index=False)
