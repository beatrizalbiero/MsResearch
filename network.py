'''
packages
'''
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

'''
1.Load data
'''

# load ptverbs dataset
dataset = numpy.loadtxt("ptverbs.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,] #input column
Y = dataset[:,] #output column

'''
2. Define model
'''
# create model
model = Sequential()
model.add(Dense(460, input_dim=1, activation='relu'))
model.add(Dense(?, activation='relu'))
model.add(Dense(460, activation='sigmoid'))

'''
3. Compile model
'''

# Compile model
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

'''
4. Fit model
'''

model.fit(X, Y, epochs=150, batch_size=10)

'''
5. Evaluate model
'''
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
