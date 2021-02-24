import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import math 
from tensorflow.keras import layers 
from more_itertools import flatten
model_file_name = 'my_model'
c_model_file_name = 'my_model'

mnist = tf.keras.datasets.mnist
(x_train, y_train) , (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)


my_digit1 = x_train[28, : , : ]
my_digit2 = x_train[20375, : , : ]
my_digit3 = x_train[20446, : , : ]
my_digit4 = x_train[20497, : , : ]



print(list(flatten(my_digit1)))
print("")
print(list(flatten(my_digit2)))
print("")
print(list(flatten(my_digit3)))
print("")
print(list(flatten(my_digit4)))