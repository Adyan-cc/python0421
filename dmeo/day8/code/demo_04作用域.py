

# - L-->local(函数内部) 局部作用域
# - E-->Enclosing  嵌套作用域
# - G-->Global 全局作用域
# - B--built-in  內建作用域

# name = "张伟强"
# def outter():
#     name = "张威"
#     def inner():
#         # name = "刘江"
#         print(name)
#     inner()
# outter()
#1.调用自己内部inner的name
#2.注释掉name = "刘江"，调用父函数中的name
# 3.注释掉name = "张威"，调用全局name,

# - 模块（model），类(class),函数(def、lambda)会产生新的作用域
# - 条件语句(if...else...)，循环语句(while....,for....)
# for i in range(10):
#     num = 5
# print(num)

# if 10>=5:
#     num=20
# print(num)
#
# def func():
#     lst = [1,2]  #产生新的作用域，出了函数就无法使用
# func()
# print(lst)

# - global 关键字可以将局部变量变成一个全局变量 格式: global 变量名称
# - nonlocal 关键字可以修改外层(非全局)变量
# name = "张伟强"
# lst = [10]
# def func():
#     name = "刘江"
#     lst.append(20)
#     print("内部：",name)
# func()
# print("外部：",name)
# print(lst)

# name = "张伟强"
# def func():
#     global name  #声明全局变量
#     name = "刘江"
#     print("内部：",name)
# func()
# print("外部：",name)

#修改嵌套中的name
name = "徐伟明"
def func1():
    name = "张伟强"
    def func2():
        #在func2中修改name = "张伟强"
        nonlocal name
        name = "刘江"
    func2()
    print("嵌套：",name)
func1()
print("全局：",name)