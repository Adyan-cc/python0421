
# 生产者与消费者模式
#
# - 生产者：生产数据的线程
# - 消费者：处理数据的线程
# - 目的：平衡生产者和消费者的工作能力来提高程序的整体处理数据的速度

# .简单的--两个消费者对应一个生产者

import threading
import queue
import time

def producer(name): #生产者
    count = 1
    while True:
        print("%s生产了包子%d"%(name,count))
        q.put(count)
        count+=1
        time.sleep(0.2)
        print("包子总数",q.qsize())
def costom(name): #消费者
    while True:
        print("%s吃了包子%d"%(name,q.get()))
        time.sleep(1)
if __name__ == '__main__':
    q = queue.Queue(maxsize=3)
    t1 = threading.Thread(target=producer,args=("张大厨",))
    t2 = threading.Thread(target=costom, args=("吃货刘",))
    t3 = threading.Thread(target=costom, args=("吃货朱",))
    t1.start()
    t2.start()
    t3.start()