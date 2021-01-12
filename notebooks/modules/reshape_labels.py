import numpy as np

def reshape(label, feature_shape, sr, hop_length):
    """
    Helper function that helps reshape the 
    labels to the same shape as the mel spectrograms

    :param label - a list of all the label boundaries
    :param feature_shape - the dimensions of the corresponding feature
    :param sr - sampling rate
    :param hop_lenght - mel spec window size
    """
    ## initialise empty vector with shape of features
    label_vector = np.zeros(feature_shape) 
    ## given by the relationship T = 1/F
    time = sr/hop_length 
    for l in label:
        """ iterate through labels """
        ## check that label start time is greater than 0
        if (l > 0):
            ## convert label time to integer which is the
            ## index in the labels vector
            label_time = int(np.round(l*time))
            if(label_time < len(label_vector)):
                ## set the index of the label vector to one
                ## indicating a boundary
                label_vector[label_time] = 1
    return label_vector