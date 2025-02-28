import numpy as np
import pandas as pd

def print_full_df(dataframe):
    '''Prints the the full sized dataframe for easy viewing.
    dataframe, a dataframe,
    '''
    pd.set_option('display.max_rows', len(dataframe))
    display(dataframe)
    pd.reset_option('display.max_rows')