import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.activations import relu,linear
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

"""
df = pd.read_csv("lung_cancer.csv")
df['GENDER'] = df['GENDER'].replace({'M': 1})
df['GENDER'] = df['GENDER'].replace({'F': 0})
df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'YES': 1})
df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'NO': 0})

df.to_csv("lung_cancer.csv", index=False)
"""

lung_data = np.genfromtxt('lung_cancer.csv', delimiter=',', skip_header=1)
lung_data[:,1] /= 100
lung_data[:,2:lung_data.shape[1]-1] -= 1
X = lung_data[:,0:lung_data.shape[1]-1]
y = lung_data[:,lung_data.shape[1]-1]
y.shape = (309, 1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30)


model = Sequential(
    [
        Dense(25, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        Dense(15, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        Dense(1, activation="sigmoid")
    ]
)

model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
)

model.fit(
    X_train,y_train,
    epochs=300
)

pickle.dump(model, open('model.pkl', 'wb'))

predictions = model.predict(X_test)
predictions_bin = np.zeros(len(predictions))

for i in range(len(predictions)):
    if predictions[i,0] < 0.5:
        predictions_bin[i] = 0
    else:
        predictions_bin[i] = 1

incorrect = 0
indexes = []
for i in range(len(predictions)):
    if predictions_bin[i] != y_test[i,0]:
        incorrect += 1
        indexes.append(i)
err = incorrect / len(predictions)
print(err)
