
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
           time.sleep(1)
           msg = f"I'm {self.name} @{i}"
           print(msg)

def test1():
    for i in range(5):
        #创建线程
        t = MyThread()
        #开启线程
        t.start()

def main():
    test1()
main()