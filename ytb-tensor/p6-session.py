#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],    #two rows, one column
                        [2]])

# We don't have to run the init all Variables because
# no variable defined
product = tf.matmul(matrix1, matrix2)   #np.dot(m1, m2)

if False:
    # Method 1
    sess = tf.Session()
    result = sess.run(product)
    print(result)
    sess.close()
else:
    # Method 2
    with tf.Session() as sess:
        result2 = sess.run(product)
        print(result2)

# And once we run code above, the session has been closed.




















