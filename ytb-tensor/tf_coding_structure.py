#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3



###create tensorflow structure start###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.random_uniform([1]))

y = Weights * x_data + biases   #predict y, we define how to calculate

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)  #0.5 --> learning rate
train = optimizer.minimize(loss)

    #once you have defined any variable in your code,
    #you should init all Variables
init = tf.initialize_all_variables()    #important
###create tensorflow structure end###

#sess is like a point, if it points to `y`, it just calc `y`
sess = tf.Session()
sess.run(init)  #Once you run session, the structure is activated from static

for step in range(3010):
    sess.run(train)     #Train all the paramters
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))



















