import tensorflow as tf 

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a+b

sess = tf.Session()
print(sess.run(adder_node, {a: 3, b: 4.5}))
print (sess.run(adder_node,{a: [3,4], b:[1,2]}))

add_and_triple = adder_node * 3
print (sess.run(add_and_triple, {a:3, b:4.5}))

