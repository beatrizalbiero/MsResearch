"""N Grams Model."""

import csv
import coding_function as cf
import pickle

path = 'Corpus/treated_corpus.csv'


def load_corpus(path, verbose=False):
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
    if verbose is True:
        print(len(phoneticinf), len(phoneticI))
    return phoneticinf, phoneticI


def ngrams_generator():
    """Create a file with trigrams."""
    import itertools
    infinitive, conjugated = load_corpus(path)
    corpus = infinitive + conjugated
    trigrams = list()
    for item in corpus:
        trigrams.append(cf.trigramizer(item))
    grams = list()
    for sublist in trigrams:
        for item in sublist:
            grams.append(item)
    grams.sort()
    trigrams = list(k for k, _ in itertools.groupby(grams))
    with open("trigrams.txt", "wb") as fp:   # Pickling
            pickle.dump(trigrams, fp)


def activation(verb):
    """
    Activation of nodes.

    :type verb: string
    :r type: list (boolean vector)
    """
    from trigrams_nodes import trigrams_dict
    verb_trigram = cf.trigramizer(verb)
    nodes = [0]*1060
    for i, trigram_i in enumerate(trigrams_dict):
        for trigram_j in verb_trigram:
            if trigram_i == trigram_j:
                nodes[i] = 1
    return nodes
