


import threading
import time

def test1():
    for i in range(1,6):
        time.sleep(1)
        print("--子线程1--%d"%i)
        print("子线程1中查看线程情况:",threading.enumerate())

def test2():
    for i in range(1,6):
        time.sleep(1)
        print("--子线程2--%d"%i)
        print("子线程2中查看线程情况:",threading.enumerate())
def main():
    print("创建线程之前的线程情况：",threading.enumerate())

    #创建线程
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    time.sleep(1)
    print("创建线程之后的线程情况：", threading.enumerate())

    #开启线程
    t1.start()
    t2.start()
    time.sleep(1)
    print("调用start之后的线程情况：", threading.enumerate())
    time.sleep(6)
    print("等待子线程执行结束后的线程情况：", threading.enumerate())
if __name__ == '__main__':
    main()