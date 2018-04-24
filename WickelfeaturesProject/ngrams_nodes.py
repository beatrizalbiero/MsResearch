"""N Grams Model."""

import csv

path = 'Corpus/corpus_completo.csv'


def load_corpus(path, verbose=True):
    """
    Create a pandas data frame.

    Columns: 'infinitive': the verb's infinitive, 'vec_inf': the coded
    infinitive form,
    'f person': the verb's first person conjugation (in portuguese),
    'vec_I': the coded conjugate form.

    If verbose is True, returns the lenght of the corpus.

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
    if verbose == True:
        print(len(phoneticinf), len(phoneticI))
    return phoneticinf, phoneticI


infinitive, conjugated = load_corpus(path)

corpus = infinitive + conjugated
