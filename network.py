'''
packages
'''
import keras
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense

# fix random seed for reproducibility
numpy.random.seed(7)

'''
1.Load data
'''

import coding_function as cf
import csv

'''
open a csv file containing phonetic transcribed verbs, inifitive and conjugated forms
'''
with open('ptverbs_test.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
    phoneticinf = []
    phoneticI = []

    for row in readcsv:
        phinf = row[1]
        phI = row[3]
        phoneticinf.append(phinf)
        phoneticI.append(phI)


'''
create two dictionaries, one for inifitive forms and another for conjugated forms
'''

dictioinf = {}
dictioI = {}

for item in phoneticinf:
    dictioinf[item] = cf.coding(item)

for item in phoneticI:
    dictioI[item] = cf.coding(item)

# dictioinf.values()
# dictioI


# split into input (X) and output (Y) variables
X = dictioinf.values() #input column
Y = dictioI.values() #output column

X
numpy.array(X)
len(X)

X = np.array(list(X))
Y = np.array(list(Y))

'''
2. Define model
'''

model = Sequential()
model.add(Dense(460, input_shape=(460,), activation='sigmoid'))

'''
3. Compile model
'''

model.compile(loss='mean_squared_error', optimizer='adadelta', metrics=['accuracy'])

'''
4. Fit model
'''
model.fit(X,Y, epochs=20, batch_size=5)

'''
5. Evaluate model
'''

import numpy as np
from keras.callbacks import Callback
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
class Metrics(Callback):
def on_train_begin(self, logs={}):
 self.val_f1s = []
 self.val_recalls = []
 self.val_precisions = []

def on_epoch_end(self, epoch, logs={}):
 val_predict = (np.asarray(self.model.predict(self.model.validation_data[0]))).round()
 val_targ = self.model.validation_data[1]
 _val_f1 = f1_score(val_targ, val_predict)
 _val_recall = recall_score(val_targ, val_predict)
 _val_precision = precision_score(val_targ, val_predict)
 self.val_f1s.append(_val_f1)
 self.val_recalls.append(_val_recall)
 self.val_precisions.append(_val_precision)
 print “ — val_f1: %f — val_precision: %f — val_recall %f” %(_val_f1, _val_precision, _val_recall)
 return

metrics = Metrics()
#F1_score
#https://en.wikipedia.org/wiki/F1_score
#threshold on numpy
# import numpy as np
#
# a = np.array([[0.2, 0.3, 0.5, 0.7, 0.9, 0.8],
#               [0.2, 0.4, 0.5, 0.9, 0.3, 0.1]])
# np.where(a >= 0.5, 1, 0)

'''
threshold
'''
a = np.array([[0.2, 0.3, 0.5, 0.7, 0.9, 0.8],
              [0.2, 0.4, 0.5, 0.9, 0.3, 0.1]])
np.where(a >= 0.5, 1, 0)
