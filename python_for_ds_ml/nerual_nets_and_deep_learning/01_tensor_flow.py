#%%
import tensorflow as tf

#%%
hello = tf.constant('Hello World')

#%%
type(hello)

#%%
sess = tf.Session()

#%%
sess.run(hello)

#%%
x = tf.constant(2)
y = tf.constant(3)

#%%
with tf.Session() as sess:
  print(sess.run(x+y))
  print(sess.run(x-y))

#%%
x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)

#%%
add = tf.add(x, y)

#%%
with tf.Session as sess:
  print(sess.run(add, feed_dict={x: 20, y: 33}))

#%%
