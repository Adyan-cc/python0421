

#一边下载歌曲，一边听歌
import time
import threading

# def listen():
#     for i in range(1,6):
#         print("正在听歌")
#         time.sleep(1)
# def down_load():
#     for i in range(1,6):
#         print("正在下载歌曲")
#         time.sleep(0.5)
#
# def main():
#     #创建线程
#     t1 = threading.Thread(target=down_load)
#     t2 = threading.Thread(target=listen)
#     # t1.setDaemon(True)
#     t2.setDaemon(True)
#     # 开启线程
#     t1.start()
#     t2.start()
# if __name__ == '__main__':
#     main()
#     print("程序执行结束了")



def listen():
    for i in range(1,6):
        print("正在听歌")
        time.sleep(1)
def down_load():
    for i in range(1,6):
        print("正在下载歌曲")
        time.sleep(0.5)

def main():
    #创建线程
    t1 = threading.Thread(target=down_load)
    t2 = threading.Thread(target=listen)
    print("t1线程开启之前的状态：",t1.is_alive())
    # t1.setName("陈星航1")
    # 开启线程
    # print("正在运行的线程数量：", threading.activeCount())
    t1.start()
    print("t1线程开启之后的状态：", t1.is_alive())
    # t1.join()
    t2.start()
    # print("当前线程：",threading.currentThread())
    # print(threading.enumerate())
    # print("正在运行的线程数量：",threading.activeCount())
    # print("线程t1的名称：",t1.getName())
if __name__ == '__main__':
    main()
    print("程序执行结束了")
    print("正在运行的线程数量：", threading.activeCount())