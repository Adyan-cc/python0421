
# 1.嵌套 2.内层函数使用外城函数的变量  3.外层函数返回内层函数的引用
# def outter(num):
#     def inner():
#         print(num)
#     return inner
# ret = outter(5)
# ret()
#执行函数后，函数并没有结束

#装饰器

#共有有N个部门，负责相应的业务
# def f1():
#     print("f1")
# def f2():
#     print("f2")
# def f3():
#     print("f3")

#部门在执行相应业务前要进行身份验证 print("身份验证")

# def f1():
#     print("身份验证")
#     print("f1")
# def f2():
#     print("身份验证")
#     print("f2")
# def f3():
#     print("身份验证")
#     print("f3")
# f1()
# f2()
# f3()
#开放封闭原则
#封闭：已经写好的代码，不轻易修改
#开放：可以对外拓展功能

# def outter(f):
#     def inner():
#         print("身份验证")
#         f()
#     return inner
#
# def f1():
#     print("f1")
#
# f1 = outter(f1)
# f1()
"""
1.定义outter,f1函数
2.调用outter函数，并将函数对象f1当成参数传递过去 f1-->f
    定义inner函数，将inner函数对象返回
    并赋值给等号左边的f1变量  f1实际指向inner函数
3.f1() 执行inner函数
            -->print("身份验证")
            -->执行f,即执行传过来的函数对象f1()， print("f1")
"""


def outter(f):
    def inner():
        print("--before  inner--")
        f()
        print("--after  inner--")
    print("--outter---")
    return inner
@outter
def func():
    print("这是func函数")

# func = outter(func)




