#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This code learns Tensor Board.
And the origin video is on 
https://www.youtube.com/watch?v=FtxpjxFi2vk&index=14&list=PLXO45tsB95cJHXaDKpbwr5fC_CCYylw1f
"""

from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import subprocess


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# Make up some real data
#make data from -1 to 1 for 300 samples
#newaxis --> one column
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#plt.scatter(x_data, y_data)
#plt.savefig("origin.jpg")


# Define placeholder for inputs to network
#the None is representing the number of samples
#so whatever number samples passed to the placeholder
#the placeholder can hold on that number.
#1 is how many features for this X data
with tf.name_scope("inputs"):
    xs = tf.placeholder(tf.float32, [None, 1], name="x_inputs")
    ys = tf.placeholder(tf.float32, [None, 1], name="y_inputs")


# Add hidden layer
#1 in_size; 10 hidden units
l1 = add_layer(xs, 1, 10, activation_function = tf.nn.relu)

# Add output layer
prediction = add_layer(l1, 10, 1, activation_function = None)


# The error between prediction and real data
loss = tf.reduce_mean(
        tf.reduce_sum(tf.square(ys-prediction), 
        reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# Important step
init = tf.initialize_all_variables()
sess = tf.Session()
writer = tf.summary.FileWriter("logs/", sess.graph)

sess.run(init)


exit()
# Plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()


for i in range(1000):
    #training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 10 == 0:
    #to see the step improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_val = sess.run(prediction, feed_dict={xs: x_data})
        #plot the prediction
        lines = ax.plot(x_data, prediction_val, 'r-', lw = 5)
        #plt.pause(1)
        plt.savefig('picture' + str(i/10)+".jpg")

#subprocess.call(['ffmpeg', '-i', 'picture%d0.png', 'output.avi'])

































