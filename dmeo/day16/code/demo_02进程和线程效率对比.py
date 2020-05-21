
# 测试多线程的效率 在单线程中数 8 千万个数和在两个线程中分别数 8 千万个数，
# 哪个效率更高？速度更快？

import threading
import time
def func1():
    start = time.time()
    for i in range(140000000):
        i+=1
    end = time.time()
    print("func1-->total_time:{}".format(end-start))
# if __name__ == '__main__':
#     t1 = threading.Thread(target=func1)
#     t1.start()  #5.49


def func2():
    start = time.time()
    for i in range(70000000):
        i+=1
    end = time.time()
    print("func2-->total_time:{}".format(end-start))
def func3():
    start = time.time()
    for i in range(70000000):
        i+=1
    end = time.time()
    print("func3-->total_time:{}".format(end-start))
# if __name__ == '__main__':
#     t2 = threading.Thread(target=func2)
#     t3 = threading.Thread(target=func3)
#     t2.start()
#     t3.start()  #5.51

#使用多进程数8千万个数
import multiprocessing
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=func2)
    p2 = multiprocessing.Process(target=func3)
    p1.start()
    p2.start()