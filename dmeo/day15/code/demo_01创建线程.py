

#一边下载歌曲，一边听歌
import time
import threading

def listen():
    for i in range(1,6):
        print("正在听歌")
        time.sleep(1)

def down_load():
    for i in range(1,6):
        print("正在下载歌曲")
        time.sleep(1)

# down_load()
# sing()

# if __name__ == '__main__':
#     #创建线程
#     t1 = threading.Thread(target=down_load)
#     t2 = threading.Thread(target=listen)
    #开启线程
    # t1.start()
    # t2.start()