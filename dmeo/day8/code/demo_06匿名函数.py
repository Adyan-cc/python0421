
# - 在定义函数的时候，如果不想给函数起名字，可以用lambda定义一个匿名函数
# - 语法： 变量名=lambda 参数：表达式
#   - 注意：1.表达式中不能有循环，return，可以包含if...else...  2.表达式结果直接返回

#1创建函数，无参数
# ret = lambda :3<5
# print(ret())

#2创建函数，有参数
# ret2 = lambda x,y:x<y
# print(ret2(3,5))

#3.返回参数中较小的数
# ret3 = lambda x,y:x if x<y else y
# print(ret3(3,5))

# lst = [
#     {"name":"梁少天","age":20,"score":90},
#     {"name":"朱益锋","age":22,"score":95},
#     {"name":"魏春平","age":21,"score":97},
# ]
# #返回年龄最大的那组信息,使用匿名函数
# ret = max(lst,key=lambda dic:dic["age"])
# print(ret)

#求列表中每一个元素的平方
# lst3 = [1,2,3]
# ret = list(map(lambda i:i**2,lst3))
# print(ret)

# lst4 = [1,2,3,4,5,6,7,8,9]
# #过滤列表中的所有奇数
# ret = list(filter(lambda i:i%2==0,lst4))
# print(ret)
# def func(i):
#     return i%2==0

# 现有两个元组(('a'),('b')),(('c'),('d'))，请生成[{'a':'c'},{'b':'d'}格式。
# tup1 = ('a','b')
# tup2 = ('c','d')
# tup3 = tuple(zip(tup1,tup2))
# print(tup3)
# ret = list(map(lambda tup:{tup[0]:tup[1]} ,tup3))
# print(ret)

# lambda 表达式也会产生一个新的局部作用域。在 def 定义的函数中嵌套 labmbda 表达式，
# lambda 表达式 能够看到所有 def 定义的函数中可用的变量

# def func():
#     name = "张伟强"
#     ret = lambda :name
#     print(ret())
# func()

# def func():
#     x = 4
#     action = lambda n,y=x:y**n
#     return action
# x = func()
# print(x(2))
"""
56:定义函数func
60右边的内容：调用func函数
             -->57 x=4,
             -->58 定义匿名函数，y=x,即y=4
             -->返回匿名函数的引用action
60左边内容：将匿名函数的引用action赋值给x
61  x(2)执行匿名函数，并传递参数2给n,
    -->58 执行lambda后面内容 y**n 即4**2=16
"""
# def func():
#     x = 4
#     def action(n,y=x):
#         return y**n
#     return action
# x = func()
# print(x(2))

#y是一个默认参数，形参
# def func():
#     x = 4
#     action = lambda n,x=x:x**n
#     return action
# x = func()
# print(x(2))

# 请说出 acts[0](2)的值，并且说明为什么
def makeAction():
    lst = []
    for i in range(4):
        lst.append(lambda x:i**x)
    return lst
acts = makeAction()
print(acts[0](2),acts[1](2),acts[2](2),acts[3](2))
"""
89 定义函数makeAction
94右边：执行makeAction
        -->90 定义列表lst=[]
        -->91，92循环0-3
            第一次循环：列表添加 匿名函数0
            第二次循环：列表添加 匿名函数1
            第三次循环：列表添加 匿名函数2
            第四次循环：列表添加 匿名函数3
        -->93 返回lst,此时lst中有4个匿名函数
94左边  将列表赋值给acts
95 acts[0]取出第一个函数，acts[0](2)执行函数，传递参数2-->x
    -->92 执行后面i**x，即i**2,i是for循环中的最后一个临时变量,此时i=3
    故i**2=3**2 = 9
"""
