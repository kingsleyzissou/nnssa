import numpy as np
import pickle
import mir_eval
import peakutils
import pandas as pd

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

def get_label_indices(labels):
    keys = []
    for k, v in enumerate(labels):
        if (v == 1):
            keys.append(k)
    return keys

if __name__ == "__main__":
    feature_list = pd.read_pickle('dumps/sal_fifty/features_normalized.p')
    preds = pickle.load(open('dumps/sal_fifty/preds.p', 'rb'))
    x_test = pickle.load(open('dumps/sal_fifty/x_test.p', 'rb'))
    y_test = pickle.load(open('dumps/sal_fifty/y_test.p', 'rb'))
    idx_test = pickle.load(open('dumps/sal_fifty/idx_test.p', 'rb'))

    preds = np.reshape(preds, len(preds))

    unique = np.unique(idx_test)

    df = feature_list[feature_list["id"].isin(unique)]

    f_score, precision, recall = [], [], []

    for _, item in df.iterrows():
        p = np.asarray(preds[idx_test == item["id"]])
        y = np.asarray(y_test[idx_test == item["id"]])
        p = np.asarray([1 if x > 0.25 else 0 for x in p])

        segments = item["segments"]

        beat_times = np.asarray(item["beat_times"])

        p = post_processing(p)
        peaks = peakutils.indexes(p, min_dist=6, thres=0.05)

        beats = beat_times[peaks]

        f, p, r = mir_eval.onset.f_measure(segments, beats, window=3)
        f_score.append(f)
        precision.append(p)
        recall.append(r)

    f_score = np.mean(np.asarray(f_score))
    precision = np.mean(np.asarray(precision))
    recall = np.mean(np.asarray(recall))

    print("F-score: ", f_score)
    print("Precision: ", precision)
    print("Recall: ", recall)
