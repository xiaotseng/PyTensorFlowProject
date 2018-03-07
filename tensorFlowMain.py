#coding:utf-8
import tensorflow as tf
def inference(x):#推断模型
    pass
def loss(x,y):#计算损失

    pass

def inputs():#输入训练数据
    return x,y
    pass
def train(total_loss):#训练
    pass
def evaluate(sess,x,y):#评估
    pass
with tf.Session() as sess:
    tf.initialize_all_variables().run()#初始化变量
    X,Y=inputs()#输入训练数据
    total_loss=loss(X,Y)#损失函数
    train_op=train(total_loss)#训练函数

    coord=tf.train.Coordinator()
    threads=tf.train.start_queue_runners(sess=sess,coord=coord)

    training_steps=1000
    for step in range(training_steps):#开始训练
        sess.run([train_op])
        if step % 10==0:
            print("loss",sess.run([total_loss]))
    evaluate(sess,X,Y)

    coord.request_stop()
    coord.join(threads)
    sess.close()

