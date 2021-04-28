import numpy as np
import mir_eval
import peakutils

def post_processing(preds_track):
    """
    Post processing of prediction probabilities, applies smoothing
    window and emphasizes beats by multiplying with running avarage.
    :param preds_track: CNN predictions per beat
    :return: post-processed predictions

    This function was not written by me and can be found at the link below:
    https://github.com/mleimeister/SegmentationCNN/blob/a9a35b5c4ce4ca1f968fd333535d534ba6b7b857/Python/evaluation.py#L41
    """

    # smoothing
    preds_track = np.convolve(preds_track, np.hamming(4) / np.sum(np.hamming(4)), 'same')

    # emphasize peaks
    preds_track = np.multiply(
        preds_track,
        np.convolve(
            preds_track, np.hamming(32) / np.sum(np.hamming(32)), 
            'same'
        )
    )

    # unit maximum
    preds_track /= np.max(preds_track)

    return preds_track

def evaluate(feature_list, preds, ids_test, bars=False, bar_window = False, window = 3):
    """
    This function iterates through the predictions and calculates
    the F1-score, precision and recall. The tolerance window for the
    F1-score calculation is defaulted to 3, but can be configured
    to use a musical tolerance window.

    :param feature_list: List of features
    :param preds: List of CNN predictions
    :param ids_test: List of track ids
    :param bars: Subdivide predictions into bars
    :param bar_window: Use a musical tolerance window of 2 bars
    :param window: Tolerance window for the F1-score
    :return: mean F1-score, mean precision, mean recall
    """

    unique = np.unique(ids_test)
    features = feature_list[feature_list["File"].isin(unique)]
    
    f_score, precision, recall = [], [], []

    for _, feature in features.iterrows():
        
        if bar_window:
            bpm = feature["BPM"]
            bps = bpm / 60
            window = (1 / bps) * 8

        idxs = np.where(ids_test == feature["File"])
        p = np.asarray(preds[idxs]).squeeze()
        
        segments = feature["Labels"]

        beat_times = np.asarray(feature["Beat_times"])

        ## use moving average to smooth predictions
        p = post_processing(p)
        ## get peaks of the predictions
        peaks = peakutils.indexes(p, min_dist=4, thres=0.05)
        
        if (bars):
            peaks = [(p * 4) for p in peaks if (p * 4) < len(beat_times)]
            
        beats = beat_times[peaks]

        ## use mir_eval to calculate onset accuracy
        f, p, r = mir_eval.onset.f_measure(segments, beats, window=window)

        f_score.append(f)
        precision.append(p)
        recall.append(r)

    f_score = np.mean(np.asarray(f_score))
    precision = np.mean(np.asarray(precision))
    recall = np.mean(np.asarray(recall))

    return f_score, precision, recall
