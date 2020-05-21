
# import views
# 导入模块会将模块中的代码执行一遍
# print(views.name)
# print("这是main模块")

# import 模块名 as 别名
# import views as v
#使用模块中的变量或者函数  模块名.函数()或模块名.变量
# v.func1()

#使用相对引入
# from . import views

# import 模块1，模块2
# import views,data

"""
有main.py
views.py :func1,name,age
data.py  :func2,name,age
导入views模块，使用func1，获取name变量并输入出
导入data模块起别名为d，使用func2，获取name变量并输入出
"""
# import views
# # views.func1(views.name)
# print(views.name)
# import data as d
# d.func2(d.name)

# from ... import ....
# from views import name
# from data import name
# name = "梁国赞"
# print(name)

# from demo2 import model1,model2
# print(model1.name)
# print(model2.name)
# 使用import导入model1
# import demo2.model1

# print(demo2.model1.name)


# from ... import *
# 一次性导入所有的函数和变量
# from views import *
# print(name,age)
# func1(name)
# func2()
# print(gender)

# 可以使用__all__来指定导入的变量
# __all__ = ["变量1","变量2"]
#只允许name,_gender,func2被导入
from views import *
print(name)
# print(age)
# func1(name)
func2()
print(_gender)