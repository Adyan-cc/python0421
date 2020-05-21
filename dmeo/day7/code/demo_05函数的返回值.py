

# def func():
#     a = 1
#     print("内部a的值：",a)
# func()
# print("外部a的值：",a)

# def func():
#     a = 1
#     print("内部a的值：",a)
#     return a
#
# # print(func())
# a = func()
# print("外部a的值：",a)

#可以返回多个数据
def func():
    a = 1
    b = 2
    return a,b
# print(func())
a,b = func()
print(a,b)