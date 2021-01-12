import os
import pandas as pd

def load_labels(option_one, option_two):
    """
    Helper function to load labels
    from file, the file accepts two options,
    since the SALAMI database has multiple
    annotations per song

    :param option_one - first annotated file option
    :param option_two - second annotated file option 
    """
    if(os.path.exists(option_one)):
            t = pd.read_table(option_one, header=None)
            return t.iloc[:, 0].values
    if (os.path.exists(option_two)):
        t = pd.read_table(option_two, header=None)
        return t.iloc[:, 0].values
    return []