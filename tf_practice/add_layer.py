import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, layer_num, activation_function=None):
    with tf.name_scope('weights-%d' %layer_num):
        Weights = tf.Variable(tf.random_uniform([in_size, out_size]), name='weight')
    with tf.name_scope('biases-%d' %layer_num):
        biases = tf.Variable(tf.zeros([1, out_size])+0.1, name='biases')
    with tf.name_scope('wx_plus_bias'):
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
    return Wx_plus_b if activation_function is None else activation_function(Wx_plus_b)


x_data = np.linspace(-1, 1, 300, dtype=np.float)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float)
y_data = np.square(x_data)-0.5+noise

xs = tf.placeholder(tf.float32, [None, 1], name='x_in')
ys = tf.placeholder(tf.float32, [None, 1], name='y_in')

l1 = add_layer(xs, 1, 10, 1, tf.nn.relu)
prediction = add_layer(l1, 10, 1, 2, None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(3000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 200 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

writer = tf.summary.FileWriter('logs', sess.graph)
