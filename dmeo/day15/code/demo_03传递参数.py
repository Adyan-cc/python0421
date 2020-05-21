

# import time
# import threading
#
# def listen(num):
#     for i in range(1,num):
#         print(f"正在听歌--{i}")
#         time.sleep(1)
#
# def down_load(num):
#     for i in range(1,num):
#         print(f"正在下载歌曲--{i}")
#         time.sleep(1)
# def main():
#     t1 = threading.Thread(target=down_load,args=(5,))
#     t2 = threading.Thread(target=listen,args=(3,))
#     t1.start()
#     t2.start()
#
# if __name__ == '__main__':
#     main()

# join()方法
#
# - 功能：当前线程执行完之后，其他线程才会继续执行

import time
import threading

def listen(num):
    for i in range(1,num):
        print(f"正在听歌--{i}")
        time.sleep(1)

def down_load(num):
    for i in range(1,num):
        print(f"正在下载歌曲--{i}")
        time.sleep(1)
def main():
    #下载完歌曲，才可以听歌
    t1 = threading.Thread(target=down_load,args=(5,))
    t2 = threading.Thread(target=listen,args=(5,))
    t1.start()
    # t1.join() #在t1执行完之后，t2和主线程才执行
    t2.start()
    # t2.join() # 在t1，t2执行完后，再继续执行主线程

if __name__ == '__main__':
    main()
    print("程序执行结束了")