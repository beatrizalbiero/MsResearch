from functools import partial
import pickle
import pandas as pd
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, load_model
from keras.layers import Input, LSTM, Dense, Masking
import matplotlib
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
from keras_metrics import KerasMetrics
from keras.optimizers import adam
import keras.backend as K
from sklearn.metrics import f1_score
from scipy.spatial import distance
opt = adam()

with open('Files/phones.pickle', 'rb') as file:
    phones = pickle.load(file)

def features():
    features = ['oclusiva', 'nasal', 'tepe', 'fricativa', 'l-aprox', 'bilabial', 'labiodental',
               'alveolar', 'p-alveolar', 'palatal', 'velar', 'glotal', 'vozeada', 'fechada',
               'm-fechada', 'm-aberta', 'aberta', 'anterior', 'posterior', 'beg', 'end']
    return features

def code(phone): 
    array = []
    fts = features()
    for item in fts:
        if item in phones[phone]:
            array.append(1)
        else:
            array.append(0)
    return np.array(array)

def code_verb(verb):
    coded = list()
    for item in verb:
        coded.append(code(item))
    return np.array(coded)

def verify(verb):
    for phone in verb:
        if phone not in phones.keys():
            print(phone, verb)

def preprocessing(corpus):
    coded_in = corpus.iloc[:,0].apply(code_verb)
    coded_out = corpus.iloc[:,1].apply(code_verb)
    coded_out_target = coded_out.apply(lambda x: np.vstack((x[1:],np.zeros(21))))
    padded_in = pad_sequences(coded_in, value=np.zeros(21))
    padded_out = pad_sequences(coded_out, value=np.zeros(21),padding="post")
    padded_out_target = pad_sequences(coded_out_target, value=np.zeros(21),padding="post")
        
    return coded_in, coded_out, padded_in, padded_out, padded_out_target

def find_closest_array(predicted):
    """
    Find closest array.
    
    Parameters:
    ----------   
    predicted : type array
    
    Returns:
    -------
    candidate : type string
    """
    min_dst = 10000
    candidate = ''
    import pickle 
    with open('WickelfeaturesProject/Files/phone_arrays.pickle', 'rb') as file:
        phone_arrays = pickle.load(file)
    del phone_arrays['PAD']
    for phone in phone_arrays:
        dst = distance.euclidean(predicted, phone_arrays[phone])
        # finds the minimum distance first
        if dst < min_dst:
            min_dst = dst
            candidate = phone
    return candidate

def decode_sequence(input_seq, encoder, decoder, renormalize=False):
    # Encode the input as state vectors.
    states_value = encoder.predict(input_seq)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1, 21)) # max decoder len = 13, 21 features
    max_decoder_seq_length = 13
    
    #Populate the first character of target sequence with the start character.
    target_seq= lookup['#'].reshape(1, 1, -1)

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_verb = ''
    while not stop_condition:
        output_phones, h, c = decoder.predict(
            [target_seq] + states_value)

        # Sample a phone
        if renormalize:
            sampled_phone = find_closest_array(output_phones[0, -1, :]/omega)
        else:
            sampled_phone = find_closest_array(output_phones[0, -1, :])                                               
        sampled_phone_vector = lookup[sampled_phone]
        decoded_verb += sampled_phone
        # Exit condition: either hit max length
        # or find stop character.
        if (sampled_phone == '$' or 
           len(decoded_verb) > max_decoder_seq_length):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = sampled_phone_vector.reshape(1, 1, -1)
#         target_seq = np.zeros((1, 1, num_decoder_tokens))
#         target_seq[0, 0, sampled_phone_vector] = 1.

        # Update states
        states_value = [h, c]

    return decoded_verb[:-1]


def decode_sequences(seq, encoder, decoder, renormalize=False):
    if len(seq.shape) == 3:
        return [decode_sequence(s.reshape(1,*s.shape), encoder, decoder, renormalize=renormalize) for s in seq]
    else:
        return [decode_sequence(seq.reshape(1,*seq.shape), encoder, decoder, renormalize=renormalize)]
    
    
def decode_from_df(df, encoder, decoder):
    data, coded_in, coded_out, padded_in, padded_out, padded_out_target = preprocessing(df)
    decoded_seqs = decode_sequences(padded_in, encoder, decoder)
    pd.DataFrame(decoded_seqs, index=data.iloc[:,0].tolist()).reset_index()
    return decoded_seqs


def train(data, epochs, length=None, verbose=False, latent_dim=256, NUM_ENCODER_TOKENS=21):
    
    coded_in, coded_out, padded_in, padded_out, padded_out_target = preprocessing(data)
    if length==None: length=len(padded_in)
        
    # Define an input sequence and process it.
    encoder_inputs = Input(shape=(None, NUM_ENCODER_TOKENS)) #19
    #encoder_inputs = Masking()(encoder_inputs) # Assuming PAD is zeros
    encoder = LSTM(latent_dim, return_state=True)
    # Now the LSTM will ignore the PADs when encoding
    # by skipping those timesteps that are masked
    encoder_outputs, state_h, state_c = encoder(encoder_inputs)
    # We discard `encoder_outputs` and only keep the states.
    encoder_states = [state_h, state_c]

    # Set up the decoder, using `encoder_states` as initial state.
    num_decoder_tokens = 21
    decoder_inputs = Input(shape=(None, num_decoder_tokens))
    # We set up our decoder to return full output sequences,
    # and to return internal states as well. We don't use the
    # return states in the training model, but we will use them in inference.
    decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                             initial_state=encoder_states)
    decoder_dense = Dense(num_decoder_tokens, activation='sigmoid')
    decoder_outputs = decoder_dense(decoder_outputs)

    # Define the model that will turn
    # `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    
    
    encoder_model = Model(encoder_inputs, encoder_states)
    
    decoder_state_input_h = Input(shape=(latent_dim,))
    decoder_state_input_c = Input(shape=(latent_dim,))
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
    decoder_outputs, state_h, state_c = decoder_lstm(
        decoder_inputs, initial_state=decoder_states_inputs)
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_dense(decoder_outputs)
    decoder_model = Model(
        [decoder_inputs] + decoder_states_inputs,
        [decoder_outputs] + decoder_states)
    
    decoder = partial(decode_from_df, encoder=encoder_model, decoder=decoder_model)

    keras_metrics = KerasMetrics()
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=[ keras_metrics.fbeta_score,
                   keras_metrics.recall,
                   keras_metrics.precision]) #, mean_pred],)
    
    history = model.fit([padded_in[:length], padded_out[:length]],
                        padded_out_target[:length],
                        batch_size=128,
                        epochs=epochs,
                        validation_split=0.2,verbose=verbose)
        
    return model, decoder, history

def plot_f_beta(history):
    plt.plot(history.history['fbeta_score'])
    plt.plot(pd.Series(history.history['val_fbeta_score']))
    plt.title('f1 score')
    plt.ylabel('f1_Score')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left');
    
    
def plot_recall(history):
    score = 'recall'
    plt.plot(history.history[score])
    plt.plot(pd.Series(history.history['val_{}'.format(score)]))
    plt.title('model {}'.format(score))
    plt.ylabel(score)
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left');

def plot_precision(history):
    score = 'precision'
    plt.plot(history.history[score])
    plt.plot(pd.Series(history.history['val_{}'.format(score)]))
    plt.title('model {}'.format(score))
    plt.ylabel(score)
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left');