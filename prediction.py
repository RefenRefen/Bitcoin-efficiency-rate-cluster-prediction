import tensorflow as tf
import numpy as np
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM, Dense, RepeatVector, TimeDistributed
# from tensorflow.keras
from sklearn.model_selection import train_test_split
from keras.losses import CategoricalCrossentropy
import matplotlib.pyplot as plt
import seaborn as sns


def split_sequence(sequence, n_steps_in, n_steps_out):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        if out_end_ix > len(sequence):
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)


# def get_model(n_steps_in):
#     model = Sequential()
#     model.add(Dense(1, activation='relu', input_shape=(n_steps_in,)))
#     # model.add(RepeatVector(n_steps_out))
#     model.add(Dense(64, activation='relu'))
#     model.add(Dense(32, activation='relu'))
#     model.add(Dense(16, activation='relu'))
#     model.add(Dense(3, activation='softmax'))
#     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#     return model


# def get_model(n_steps_in, n_features):
#     n_steps_out = 1
#     model = Sequential()
#     model.add(LSTM(256, activation='relu', input_shape=(n_steps_in, n_features), return_sequences=True))
#     model.add(LSTM(128, activation='relu', return_sequences=True))
#     model.add(LSTM(64, activation='relu'))
#     model.add(RepeatVector(n_steps_out))
#     model.add(LSTM(64, activation='relu', return_sequences=True))
#     model.add(LSTM(128, activation='relu', return_sequences=True))
#     model.add(LSTM(256, activation='relu', return_sequences=True))
#     model.add(TimeDistributed(Dense(1)))
#     model.compile(optimizer='adam', loss='mse', metrics=['mae'])
#     return model

def get_model(n_steps_in, n_features):
    model = Sequential()
    model.add(LSTM(256, activation='relu', input_shape=(n_steps_in, n_features), return_sequences=True))
    model.add(LSTM(128, activation='relu', return_sequences=True))
    model.add(LSTM(64, activation='relu', return_sequences=True))
    model.add(LSTM(32, activation='relu', return_sequences=True))
    model.add(LSTM(16, activation='relu', return_sequences=True))
    model.add(LSTM(8, activation='relu', return_sequences=True))
    # model.add(RepeatVector(n_steps_out))
    model.add(LSTM(4, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


class Model:
    def __init__(self, input_dict: dict, currency: str = 'bitcoin'):
        self.dict = input_dict
        self.currency = currency
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def preprocessing(self):

        cluster_array = self.dict[self.currency]['efficiency_rate']
        import numpy

        numpy.savetxt("cluster_array.csv", cluster_array, delimiter=",")
        n_steps_in, n_steps_out = 4, 1
        X, y = split_sequence(cluster_array, n_steps_in, n_steps_out)
        # y = np.where(y == -1, 2, y)
        n_features = 1
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        y = y.reshape((y.shape[0], y.shape[1], n_features))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        for i in range(self.X_test.shape[0]):
            print(self.X_test[i], self.y_test[i])
        # plt.plot(cluster_array)
        # sns.boxplot(x=cluster_array)
        # plt.show()

    def train(self):
        self.preprocessing()
        mdl = get_model(4, 1)
        print(mdl.summary())
        # history = mdl.fit(self.X_train, self.y_train, epochs=1000, verbose=1)
        # plt.plot(history.history['loss'])
        # plt.show()
        # plt.plot(history.history['mae'])
        # plt.show()
        # mdl.evaluate(self.X_test, self.y_test, )
        #
        # yhat = mdl.predict(self.X_test, verbose=1)
        # print(self.X_test)
        # print(yhat)
        # predicted_val = list()
        # for element in yhat:
        #     predicted_val.append(element[0])
        #
        # y_test = list()
        # for element in self.y_test:
        #     y_test.append(element[0][0])
        #
        # plt.plot(predicted_val, label='Predicted Values')
        # plt.plot(y_test, label='True Value')
        # plt.xlabel('Day')
        # plt.ylabel('Number Of Failure')
        # plt.legend()
        # plt.show()
