

# #参数传递比较麻烦
# def process():
#     std = "学生资源" #std是局部变量，但是每个函数都需要，索引要传进去
#     do_task(std)
#
# def do_task(std):
#     func1(std)
#     func2(std)
#
# def func1(std):
#     print("func1",std)
# def func2(std):
#     print("func2",std)
#
# if __name__ == '__main__':
#     process()


#使用全局字典
# import threading
# global_dict = {}
# def process():
#     std = "学生资源"
#     #把std放到全局字典global_dict中
#     global_dict[threading.currentThread()] = std
#     do_task()
#
# def do_task():
#     func1()
#     func2()
#
# def func1():
#     std = global_dict[threading.currentThread()]
#     print("func1",std)
# def func2():
#     std = global_dict[threading.currentThread()]
#     print("func2",std)
#
# if __name__ == '__main__':
#     process()

# 使用threadlocal
import threading
local_std = threading.local()
def process():
    std = "学生资源"
    local_std.std = std
    do_task()

def do_task():
    func1()
    func2()

def func1():
    std = local_std.std
    print("func1",std)
def func2():
    std = local_std.std
    print("func2",std)

if __name__ == '__main__':
    process()