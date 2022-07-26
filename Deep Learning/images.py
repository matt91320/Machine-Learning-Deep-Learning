from utilities import *
from formules import *
import matplotlib.pyplot as plt

X_train, y_train, X_test, y_test = load_data()

X_train_reshape = X_train.reshape(X_train.shape[0], -1) / X_train.max()
X_test_reshape = X_test.reshape(X_test.shape[0], -1) / X_train.max()

W, b = artificial_neuron(X_train_reshape, y_train, X_test_reshape, y_test)