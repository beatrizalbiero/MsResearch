"""
Decoding function.

This Python code will decode a one-hot vector of wickelfeatures back into a
verb after the neural network training.
"""
import pandas as pd
import numpy as np
from Files import nodes
wickelfeatures_list = nodes.nds
import coding_function as cf
import decoding_function as dec


def decoding(vector):
    """
    This function receives a vector that represents the prediction of
    wickelfeatures of a verb.

    :vector type: list
    :r type: str (?)
    """
    def createdf(vector):
        """
        Create a dataframe of wickelfeatures and prediction values.

        :vector type: list
        :r type: dataframe (pandas)
        """
        new = np.asarray(vector)
        df = pd.DataFrame()
        df['wickelfeatures'] = wickelfeatures_list
        df['values'] = new
        return df
    def sixteenbest(df):
        """
        Select sixteen best wickelfeatures.

        :df type: df (pandas)
        :r type: df (pandas)
        """
        x = df.sort_values(by = ['values'], axis = 0, ascending = False, inplace = False, kind='quicksort', na_position = 'last')
        r = x.head(16)
        return r
    def find_compatible(df1, df2):
        """
        Find Compatible.

        returns a new df with compatible wickelfeatures

        :df1 type: df
        :df2 type: df
        :r type: df
        """
        new_df = [['wickelfeatures'],['values']]
        for item1 in df1['wickelfeatures']:
            for item2 in df2['wickelfeatures']:
                if item1[1] == item2[0] and item1[2] == item2[1]:
                    new_df.append(item2)

        return new_df
    dfx = createdf(vector)
    begin = list(sixteenbest(dfx[361:])['wickelfeatures'])
    end = list(sixteenbest(dfx[261:361])['wickelfeatures'])
    dbeg = ''
    dend= ''
    for i in range(0,3):
        dbeg = dbeg + dec.competion(begin,i)
    for i in range(0,3):
        dend = dend + dec.competion(end,i)
    try:
        decoded = dbeg
        while True:
            new_wicklftrs = find_compatible(begin, list(sixteenbest(dfx[:261])['wickelfeatures']))
            phoneme = dec.competition(new_wicklftrs, 2)
            decoded = decoded + phoneme
            if decoded[-2] == dend[0] and decoded[-1] == dend[-1]:
                break
    except:
        pass
    return decoded
