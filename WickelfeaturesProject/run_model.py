from __future__ import print_function

from keras.models import Model, load_model
from keras.layers import Input, LSTM, Dense
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from random import shuffle as sfl
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import GridSearchCV
import pickle
import time

def load_train_test(corpus, num_samples, test_size):
    with open(corpus, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    train_data = lines[:num_samples]
    test_data = lines[num_samples:]
    train_file = 'Corpus/train' + str(num_samples) + 'verbs.csv'
    test_file = 'Corpus/test' + str(test_size) + str(time.time())[:10] + 'verbs.csv'
    
    with open(train_file, 'w', encoding='utf-8') as f:
        for line in train_data:
            f.write(line + '\n')
    
    with open(test_file, 'w', encoding='utf-8') as f:
        for line in test_data:
            f.write(line + '\n')
    
    return train_file, test_file


# Restore the model and construct the encoder and decoder


def test_train_dataset(encoder_input_data):
    for seq_index in range(100):
        # Take one sequence (part of the training set)
        # for trying out decoding.
        input_seq = encoder_input_data[seq_index: seq_index + 1]
        decoded_sentence = decode_sequence(input_seq)
        print('-')
        print('Input sentence:', input_texts[seq_index])
        print('Decoded sentence:', decoded_sentence)

def load_test(test_file):
    import pandas as pd

    test = pd.read_csv(test_file, 
                       sep=';', names=['infinitivo','conjugado'])
    return test