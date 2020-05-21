
#带参数的装饰器
# def outter(f):
#     def inner(*args,**kwargs):
#         print(args)
#         print(kwargs)
#         f()
#     return inner
#
# @outter # func=outter(func)
# def func():
#     print("这是func函数")
#
# #此时改变了原函数的调用方式
# func(10,20,name="徐伟明")

# def outter(f):
#     def inner(a,b):
#         f(a,b)
#     return inner
#
# @outter
# def func(a,b):
#     print(a+b)
#     print("这是func函数")
# func(3,5)

#带返回值的装饰器
# def outter(f):
#     def inner():
#         ret = f()
#         return ret
#     return inner
#
# @outter #func = outter(func)
# def func():
#     print("这是func函数")
#     return "hello world"
# ret = func()
# print(ret)


#多个装饰器的装饰过程
#执行原理：先执行距离函数近的装饰器
def outter1(f):
    def inner1():
        print("--before inner1--")
        f()
        print("--after inner1--")
    return inner1
def outter2(f):
    def inner2():
        print("--before inner2--")
        f()
        print("--after inner2--")
    return inner2

def func():
    print("--in func--")
func = outter2(func)
func = outter1(func)
func()
