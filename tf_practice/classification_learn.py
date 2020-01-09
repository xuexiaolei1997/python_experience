from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


def add_layer(inputs, in_size, out_size, layer_num, activation_function=None):
    with tf.name_scope('weights-%d' %layer_num):
        Weights = tf.Variable(tf.random_uniform([in_size, out_size]), name='weight')
    with tf.name_scope('biases-%d' %layer_num):
        biases = tf.Variable(tf.zeros([1, out_size])+0.1, name='biases')
    with tf.name_scope('wx_plus_bias'):
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
    return Wx_plus_b if activation_function is None else activation_function(Wx_plus_b)


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


mnist = input_data.read_data_sets('mnist_data', one_hot=True)
xs = tf.placeholder(tf.float32, [None, 28*28], name='img_in')
ys = tf.placeholder(tf.float32, [None, 10], name='img_out')
prediction = add_layer(xs, 28*28, 10, 1, activation_function=tf.nn.softmax)
cross_extropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_extropy)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 100 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
