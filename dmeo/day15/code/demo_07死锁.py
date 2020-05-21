
# 在多个线程共享资源的时候，如果两个线程分别占有一部分资源，
# 并且同时等待对方的资源， 就会造成死锁现象，尽管死锁很少发生，
# 但是一旦发生就会造成应用程序停止相应

import threading
# #创建锁
# mutex = threading.Lock()
#
# #锁定
# mutex.acquire()
#
# #释放
# mutex.release()

import time

def test1():
    #lock1上锁
    lock1.acquire()
    print("--test1开始执行--")
    time.sleep(1)
    # lock2上锁
    lock2.acquire()
    print("--test1执行完成--")
    lock2.release() #lock2解锁
    lock1.release() #lock1解锁

def test2():
    # lock2上锁
    lock2.acquire()
    print("--test2开始执行--")
    time.sleep(1)
    # lock1上锁
    lock1.acquire()
    print("--test2执行完成--")
    lock1.release()  # lock1解锁
    lock2.release()  # lock2解锁
lock1 = threading.Lock()
lock2 = threading.Lock()
if __name__ == '__main__':
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
