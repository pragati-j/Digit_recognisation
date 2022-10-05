# -*- coding: utf-8 -*-
"""Digit_recognization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NUTF02z-snPtH64Fk5cwfzQGfPVwCsrc

<H1>IMPORTING LIBARIES</H1>
"""

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import tensorflow as tf
from keras import backend as K

(x_train,y_train),(x_test,y_test)=mnist.load_data()

print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

"""<h4>Preprocessing dataset</h4>


1.   Adding another dimension to train and test data
2.   Converting vectors into binary class metrics




"""

x_train= x_train.reshape(x_train.shape[0],28,28,1)
x_test= x_test.reshape(x_test.shape[0],28,28,1)

input_size=(28,28,1)
num_classes=10

y_train=  tf.keras.utils.to_categorical(y_train,num_classes)
y_test=  tf.keras.utils.to_categorical(y_test,num_classes)


x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

"""BUILDING MODEL SEQUENCE"""

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3),activation='relu',input_shape=input_size))  #appying 32 filter of size 3*3..output_size=(28,28,32) 
# model.add(MaxPooling2D((2,2)))                                                    #maxpooling of size 2*2 
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation='softmax'))
# print(x_train.shape)
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),metrics=['accuracy'])

batch_size=128
epochs=10

hist=model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test,y_test))
print("Model Ready!!!")

model.save("mymodel.h5")
print("model saved as mymodel.h5")

accuracy=model.evaluate(x_test,y_test,verbose=0)

print('test loss:',accuracy[0])
print('test accuracy:',accuracy[1])