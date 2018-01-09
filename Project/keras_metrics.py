#codigo do menino
from keras import backend as K
import numpy as np

class KerasMetrics:
    def precision(self, y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision


    def recall(self, y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall


def fbeta_score(self, y_true, y_pred, beta=1):
        if beta < 0:
            raise ValueError('The lowest choosable beta is zero (only precision).')

        if K.sum(K.round(K.clip(y_true, 0, 1))) == 0:
        return 0

        p = self.precision(y_true, y_pred)
        r = self.recall(y_true, y_pred)
        bb = beta ** 2
        fbeta_score = (1 + bb) * (p * r) / (bb * p + r + K.epsilon())
        return fbeta_score


    def f2_score(self, y_true, y_pred):
        return self.fbeta_score(y_true, y_pred, beta=2)

metrics = KerasMetrics()
