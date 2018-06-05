import sys
from keras.models import Sequential
from keras.layers import Dense
from keras_metrics import KerasMetrics
from keras.callbacks import EarlyStopping
import numpy as np
import utility as ut
sys.path.append('../')

path = 'Corpus/train_corpus.csv'
X, Y = ut.load_ngrams(path)
batch = len(X)

# 1. Define Model
model = Sequential()
model.add(Dense(1060, input_shape=(1060,), activation='sigmoid'))


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
model.fit(X, Y, epochs=400, batch_size=batch, verbose=False,
          callbacks=[stopper])

# 4. Evaluate model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%% \n%s: %.2f%% \n%s: %.2f%% \n%s: %.2f%%" %
      (model.metrics_names[0], scores[0]*100,
       model.metrics_names[1], scores[1]*100,
       model.metrics_names[2], scores[2]*100,
       model.metrics_names[3], scores[3]*100))

# 5. Save model
model.save('Models/NgramModels/second_test')

with open('Corpus/test_corpus.csv', 'r') as f:
    testRaw = f.read().split('\n')
test = list()
for item in testRaw:
    test.append(item.split(','))
test.pop(-1)


def pipeline(verbs, path, model):
    """
    Given a test dataset, returns a file with predictions.

    :verbs type: list
    :model type: keras model object
    :r type: pandas df
    """
    from ngrams_nodes import activation
    from tqdm import tqdm_notebook as tqdm
    import pandas as pd
    from time import gmtime, strftime
    from decoding_ngrams import decoding

    time = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    name = "output" + time + ".csv"
    f = open('Files/Results/' + name, "w")
    f.write("train data set:" + path + '\n' + 'Results:\n')

    # filtering the input values
    _input = list()
    for row in verbs:
        _input.append(row[1])

    # filtering the expected values
    _output = list()
    for row in verbs:
        _output.append(row[3])

    # coding the input values
    test_list = list()
    for i in _input:
        coding = activation(i)
        test_list.append(coding)
    test_list = np.array(test_list)
    prediction = model.predict(test_list)
    # Create pandas
    df = pd.DataFrame()
    df["prediction"] = []
    df["expected"] = []

    # comparing the expected values with predictions

    accuracy = 0.0
    result = list()
    for i, item in enumerate(tqdm(prediction)):
        x = decoding(item)
        result.append(x)
        if x == _output[i]:
            accuracy += 1

    df["prediction"] = result
    df["expected"] = _output

    f.write("accuracy: " + str(accuracy/len(_output)))
    f.close()
    df.to_csv('Files/Results/' + name, sep=';')

    print("accuracy: " + str(accuracy/len(_output)))

    return df


df = pipeline()
