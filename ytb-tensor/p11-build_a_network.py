#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import subprocess


def add_layer(inputs, in_size, out_size, activation_function=None):
    #add one more layer and return the output of this layer
    with tf.name_scope("layer"):
        with tf.name_scope("weights"):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="W")
        with tf.name_scope("biases"):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name="b")
        with tf.name_scope("inputs"):
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


# Define placeholder for inputs to network
#the None is representing the number of samples
#so whatever number samples passed to the placeholder
#the placeholder can hold on that number.
#1 is how many features for this X data
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])


# Add hidden layer
#1 in_size; 10 hidden units
l1 = add_layer(xs, 1, 10, activation_function = tf.nn.relu)

# Add output layer
prediction = add_layer(l1, 10, 1, activation_function = None)


# The error between prediction and real data
with tf.name_scope("loss"):
    loss = tf.reduce_mean(
            tf.reduce_sum(tf.square(ys-prediction),
            reduction_indices = [1]))

with tf.name_scope("train"):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# Important step
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


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

































