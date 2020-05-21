
# 函数的相互调用和嵌套.
#相互调用
# def func1():
#     print("--before func1--")
#     print("--after func1--")
#
# def func2():
#     print("--before func2--")
#     func1()
#     print("--after func2--")
# func2()

#嵌套
# 在函数中又定义函数
def func1():
    print("func1..")
    def func2():
        print("func2...")
    func2()
func1()