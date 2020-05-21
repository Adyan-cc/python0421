
# 1.位置参数
#计算两个数的和
# num1 = 3
# num2 = 5
# def sum_num(a,b): #形参
#     ret = a+b
#     print(a)
#     print(b)
#     print(ret)
# sum_num(num1,num2) #实参


#2.关键字参数 ：以形参=实参的形式忽略形参的定义顺序进行的传参的传参方式

# def introduce(age,name):
#     print("大家好，我叫%s,今年%d岁"%(name,age))
# introduce(name="张伟强",age=18)

#关键字参数必须在位置参数的后面
# def introduce(name,age):
#     print("大家好，我叫%s,今年%d岁"%(name,age))
# introduce("张伟强",age = 18)

# 3.默认参数：在定义参数时，给参数一个默认值，调用函数时如果没有给默认值传参，会自动采用默认值
# def introduce(name,age=20):
#     print("大家好，我叫%s,今年%d岁"%(name,age))
# introduce("张伟强")
#
# def introduce(name,age=20):
#     print("大家好，我叫%s,今年%d岁"%(name,age))
# introduce("张伟强",25)

#调用函数的时候，不确定有几个参数
def sum_num(*args):
    print(args)
    # print(args[0],args[1],args[2])
# sum_num(1,2,3)
# *可以打散序列
tup = (1,2,3)
# print(*tup)
def sum_num2(a,b,c):
    print(a,b,c)
# sum_num2(*tup)

# ** kwargs，给形参前面添加**使参数变成一个字典，所有传递的参数变成字典的键值对，
# 这里传参 要求键等于值的形式
def introduce(**kwargs):
    print(kwargs)
# introduce(name = "张伟强",age = 25)

#* 具有打散字典的功能
# dic = {"name":"张伟强","age":18}
# print(*dic)

# def introduce2(**kwargs):
# def introduce2(name,age):
#     # print(kwargs)
#     print(name,age)
# dic = {"name":"张伟强","age":18}
# introduce2(**dic) #name="张伟强，age=18

# 定义参数时的顺序：位置参数-->元组参数-->默认参数-->字典参数
# def func(num,*args,name="张伟强",**kwargs):
def func(num, name="张伟强",*args, **kwargs):
    print(num,args,name,kwargs)
# func(1,2,3,"张威",age = 18)
