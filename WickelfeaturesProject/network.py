"""Neural Network with Keras."""

import sys
from keras.models import Sequential
from keras.layers import Dense
from keras_metrics import KerasMetrics
from keras.callbacks import EarlyStopping
import numpy as np
import decoding2
import utility as ut
sys.path.append('../')


def pipeline(verbs, path, load):
    """
    Pipeline receives a list of verbs and predicts a conjugated form for them.

    The prediction is saved in an output file.
    :verbs type: list
    :rtype: string
    """
    import coding_function as cf
    from time import gmtime, strftime
    time = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    name = "output" + time + ".txt"

    correct = {'#pega#': '#pEgu', '#sega#': '#sEgu#', '#seka#': '#sEku#',
               '#leva#': '#lEvu#', '#ora#': '#Oru#', '#mora#': '#mOru#',
               '#posta#': '#pOtu#', '#joga#': '#jOgu#', '#sortia#': '#soiu#',
               '#media#': '#medeiu#', '#kompo#': '#koiu#', '#po#': '#poiu#',
               '#menti#': '#mintu#', '#tosi#': '#tusu#', '#kobri#':
               '#kubro#', '#faze#': '#fasu#', '#mata#': '#matu#', '#paga#':
               '#pagu#', '#sai#': '#saiu#', '#bate#': '#batu#', '#kome#':
               '#komu#'}

    f = open('Files/Results/' + name, "w")
    f.write("train data set:" + path + '\n' + 'Results:\n' + 'model name: ' +
            load + '\n')
    test_list = []
    for i in verbs:
        coding = cf.coding(i)
        test_list.append(coding)
    test_list = np.array(test_list)
    prediction = model.predict(test_list)
    for i, j in list(zip(verbs, prediction)):
        f.write('verb: ' + i + ", expected: " + correct[i] + ", prediction: " +
                decoding2.decoding(j) + '\n')
    scores = model.evaluate(X, Y)
    f.write("\n%s: %.2f%% \n%s: %.2f%% \n%s: %.2f%%" %
            (model.metrics_names[1], scores[1]*100,
             model.metrics_names[2], scores[2]*100,
             model.metrics_names[3], scores[3]*100))
    f.close()
    return print("Predictions saved in the file: " + name)

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
