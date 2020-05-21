
# 线程之间共享全局变量
import threading
import time
#
# g_num = 100
#
# def work1():
#     global g_num
#     for i in range(3):
#         g_num+=1
#     print(f"--in work1,g_num is {g_num}")
#
# def work2():
#     global g_num
#     print(f"--in work2,g_num is {g_num}")
#
# print("创建线程之前g_num:",g_num)
# t1 = threading.Thread(target=work1)
# t1.start()
# time.sleep(1)
# t2 = threading.Thread(target=work2)
# t2.start()




# def work1(g_nums):
#     g_nums.append(44)
#     print(f"--in work1,g_num is {g_nums}")
#
# def work2(g_nums):
#     time.sleep(0.5)
#     print(f"--in work2,g_num is {g_nums}")
#
# g_nums = [11,22,33]
# t1 = threading.Thread(target=work1,args=(g_nums,))
# t1.start()
# t2 = threading.Thread(target=work2,args=(g_nums,))
# t2.start()

# 多线程开发可能会遇到的问题

# g_num = 0
#
# def work1(num):
#     global  g_num
#     for i in range(num):
#         g_num+=1
#     print(f"--in work1,g_num is {g_num}")
#
# def work2(num):
#     global  g_num #work1执行10次执行切换到work2
#     for i in range(num):
#         g_num+=1
#     print(f"--in work2,g_num is {g_num}")
# print("创建线程之前g_num:",g_num)
# t1 = threading.Thread(target=work1,args=(100,))
# t1.start()
# t2 = threading.Thread(target=work2,args=(100,))
# t2.start()


# g_num = 0
# def work1(num):
#     global  g_num
#     for i in range(num):
#         g_num+=1
#     print(f"--in work1,g_num is {g_num}")
#
# def work2(num):
#     global  g_num #work1执行10次执行切换到work2
#     for i in range(num):
#         g_num+=1
#     print(f"--in work2,g_num is {g_num}")
# print("创建线程之前g_num:",g_num)
# t1 = threading.Thread(target=work1,args=(1000000,))
# t1.start()
# t2 = threading.Thread(target=work2,args=(1000000,))
# t2.start()

# import threading
# #创建锁
# mutex = threading.Lock()
#
# #锁定
# mutex.acquire()
#
# #释放
# mutex.release()
# 注意：如果这个锁之前没有上锁，那么acquire不会堵塞
# 如果在调用acquire 对这个锁上锁之前，他已经被其他线程上了锁，此时acquire会堵塞，直到锁被解锁位置

#使用互斥锁完成2个线程对同一全局变量各加100万次操作
g_num = 0
def work1(num):
    global  g_num
    for i in range(num):
        # 锁定
        mutex.acquire()
        g_num+=1
        # 释放
        mutex.release()


def work2(num):
    global  g_num #work1执行10次执行切换到work2
    for i in range(num):
        # 锁定
        mutex.acquire()
        g_num += 1
        # 释放
        mutex.release()

#创建锁
mutex = threading.Lock()

t1 = threading.Thread(target=work1,args=(1000000,))
t1.start()
t2 = threading.Thread(target=work2,args=(1000000,))
t2.start()

while len(threading.enumerate())!=1:
    time.sleep(1)
print(f"--最终结果,g_num is {g_num}")