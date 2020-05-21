
# name = "张伟强"
# print(name)
#
# def func1():
#     print("这是views中的func1...")

name = "刘江"

def func1(name):
    print("这是func1")
    print(name)

age = 18

def func2():
    print("这是views中的func2")

# 可以使用__all__来指定导入的变量
# __all__ = ["变量1","变量2"]
_gender = "男"
#只允许name,_gender,func2被导入
__all__=["name","_gender","func2"]