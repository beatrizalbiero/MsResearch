'''
packages
'''
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
import random
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

numpy.array(Y)


'''
2. Define model
'''
# create model
model = Sequential()
model.add(Dense(460, input_dim=460, activation='sigmoid'))
#model.add(Dense(150, activation='sigmoid'))
model.add(Dense(460, activation='sigmoid'))

'''
3. Compile model
'''

# Compile model
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

'''
4. Fit model
'''

# def get_batch(n):
#     chosen = random.sample(range(1,20), n)
#     for i in range(n):
#         #todo: how to select dictionary entries?
#     return x, y

model.fit(X, Y, epochs=150, batch_size=20)

'''
5. Evaluate model
'''
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
