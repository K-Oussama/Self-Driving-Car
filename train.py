# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
#from sklearn.externals import joblib
import joblib
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import cv2
import os
import pickle
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from keras.optimizers import Adam
import random
import h5py
   
with open('Assets/my_datasetimg.pickle', 'rb') as data:
    dataset = pickle.load(data)
X=np.array(dataset)

with open('Assets/my_dataset.pickle', 'rb') as datakey:
    datasetkey = pickle.load(datakey)
Y=np.array(datasetkey)

# create model
model = Sequential()
model.add(Lambda(lambda x: x/127.5-1.0, input_shape=(160, 320, 3)))
model.add(Conv2D(24, (5, 5), activation='elu', strides=(2, 2)))
model.add(Conv2D(36, (5, 5), activation='elu', strides=(2, 2)))
model.add(Conv2D(48, (5, 5), activation='elu', strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='elu'))
model.add(Conv2D(64, (5, 5), activation='elu'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(100, activation='elu'))
model.add(Dense(50, activation='elu'))
model.add(Dense(10, activation='elu'))
model.add(Dense(1,activation='relu'))
model.summary()
# Compile model
model.compile(loss='mean_squared_error', optimizer=Adam(lr=1.0e-4))
# Fit the model
model.fit(X, Y, epochs=100, batch_size=10)
model.save('model_15.h5')
# evaluate the model
scores = model.evaluate(X, Y)