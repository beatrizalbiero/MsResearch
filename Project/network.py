"""
Neural Network with Keras.
"""

import sys
from keras.models import Sequential
from keras.layers import Dense
from keras_metrics import KerasMetrics
from keras.callbacks import EarlyStopping
from keras import optimizers
import numpy as np
import decoding2
#import decoding_function as df
import utility as ut
sys.path.append('../')


def pipeline(verbs):
    """
    Pipeline receives a list of verbs and decodes it.

    :verbs type: list
    :r type: string
    """
    import coding_function as cf
    test_list = []
    for i in verbs:
        coding = cf.coding(i)
        test_list.append(coding)
    test_list = np.array(test_list)
    prediction = model.predict(test_list)
    for i in prediction:
        print(decoding2.decoding(i))
    return test_list.shape

# 0. Load Data
path = '../data/prop_55.csv'  # len 464
# path = '../data/prop_65.csv'
# path = '../data/prop_75.csv'
# path = '../data/prop_85.csv'
# path = '../data/prop_95.csv'
X, Y = ut.load_data(path)
batch = len(X)

# 1. Define Model
model = Sequential()
model.add(Dense(460, input_shape=(460,), activation='sigmoid'))

# 2. Compile model
keras_metrics = KerasMetrics()
model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=[keras_metrics.fbeta_score,
             keras_metrics.recall,
             keras_metrics.precision]
            )

# 3. Fit model
stopper = EarlyStopping(monitor='fbeta_score', min_delta=0.00005, patience=50,
                        verbose=1, mode='max')

model.fit(X, Y, epochs=150, batch_size=batch, verbose=False, callbacks=
          [stopper])

# 4. Evaluate model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%% \n%s: %.2f%% \n%s: %.2f%%" % (model.metrics_names[1],
      scores[1]*100, model.metrics_names[2], scores[2]*100,
      model.metrics_names[3], scores[3]*100))

# 5. Save model
#model.save('../data/prop_95')

# 6. Test Model with real verbs.

pipeline(['#pega#', '#sega#', '#seka#', '#leva#', '#ora#', '#mora#', '#posta#',
          '#joga#', '#sortia#', '#media#', '#kompo#', '#po#', '#tendi#',
          '#jenti#', '#menti#', '#hendi#', '#tosi#', '#kobri#', '#faze#',
          '#mata#', '#paga#', '#sai#', '#bate#', '#kome#'])
