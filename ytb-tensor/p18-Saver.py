#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import tensorflow as tf
import numpy as np

# Save to file
# remember to define the same dtype and shape when restore

#W = tf.Variable([[1, 2, 3], [3, 4, 5]], dtype = tf.float32, name="weights")
#b = tf.Variable([[1, 2, 3]], dtype = tf.float32, name="biases")
#
#init = tf.global_variables_initializer()
#saver = tf.train.Saver()
#
#with tf.Session() as sess:
#    sess.run(init)
#    save_path = saver.save(sess, "params/savenet.ckpt")
#    print ("Save to path: ", save_path)


#####Restore#####

# Restore variables redefine the same shape and same dtype
# for your variables
W = tf.Variable(tf.zeros([2, 3]), dtype = tf.float32, name="weights")
b = tf.Variable(tf.zeros([1, 3]), dtype = tf.float32, name="biases")

# Not need init step
saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "params/savenet.ckpt")
    print ("*" * 10)
    print ('weights', sess.run(W))
    print ('biases', sess.run(b))





