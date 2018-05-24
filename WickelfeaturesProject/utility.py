"""Utilities."""

import pandas as pd
import csv
import coding_function as cf
import numpy as np
from ngrams_nodes import activation


def load_data(path, verbose=False):
    """
    Create a pandas data frame.

    Columns: 'infinitive': the verb's infinitive, 'vec_inf': the coded
    infinitive form,
    'f person': the verb's first person conjugation (in portuguese),
    'vec_I': the coded conjugate form.

    If verbose is True, returns the lenght of the unique values of the dataset.

    :path type: string
    :verbose type: bool
    :r type: tuple
    """
    with open(path, 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        phoneticinf = []
        phoneticI = []
        for row in readcsv:
            phoneticinf.append(row[1])
            phoneticI.append(row[3])
    cf.dataTest(phoneticinf, phoneticI)  # tests if dataset is ok
    vec_inf = []
    vec_I = []
    for item in phoneticinf:
        vec_inf.append(cf.coding(item))
    for item in phoneticI:
        vec_I.append(cf.coding(item))
    d = {'infinitive': phoneticinf, 'vec_inf': vec_inf,
         'f person': phoneticI, 'vec_I': vec_I}
    df = pd.DataFrame(data=d)
    X = np.array(df['vec_inf'].tolist())
    Y = np.array(df['vec_I'].tolist())
    if verbose is False:
        return X, Y
    else:
        print('unique verbs:', len(set(phoneticinf)), '\n')
        print('lenght of data set:', len(X))
        return X, Y


def load_ngrams(path, verbose=False):
    """
    Activation of nodes.

    :type verb: string
    :r type: numpy array (boolean vector)
    """
    with open(path, 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        infinitive = []
        conjugated = []
        for row in readcsv:
            infinitive.append(row[1])
            conjugated.append(row[3])
    cf.dataTest(infinitive, conjugated)  # tests if dataset is ok
    vec_inf = []
    vec_con = []
    for item in infinitive:
        vec_inf.append(activation(item))
    for item in conjugated:
        vec_con.append(activation(item))
    d = {'infinitive': infinitive, 'vec_inf': vec_inf,
         'f person': conjugated, 'vec_con': vec_con}
    df = pd.DataFrame(data=d)
    X = np.array(df['vec_inf'].tolist())
    Y = np.array(df['vec_con'].tolist())
    if verbose is False:
        return X, Y
    else:
        print('unique verbs:', len(set(infinitive)), '\n')
        print('lenght of data set:', len(X))
        return X, Y
