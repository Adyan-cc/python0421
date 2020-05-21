



# 类属性只能被类名称引用修改，不能通过对象的引用变量修改
# 1.不可变类型：对象名.属性名=属性值   给对象添加属性，而不是进行修改
# 2.可变类型：如果对象是修改可变类型数据，是真正的修改
# ​			如果是重新给可变类型变量赋值，则是给对象添加属性
#数据类型
class Data:
    """数据类型"""
    # courses_dict = "Python"
    courses_dict = ["Python"]

data = Data()
#使用类对象修改课程为"java"
# Data.courses_dict = "java"
#使用实例对象访问
# print(data.courses_dict)
#使用类对象访问
# print(Data.courses_dict)

#使用实例对象修改课程为 "UI"
# data.courses_dict = "UI" #实际上是给实例对象增加属性
#使用实例对象访问
# print(data.courses_dict)
#使用类对象访问
# print(Data.courses_dict)


#如果类属性为可变数据类型，则使用实例对象或者类对象都是真正的修改
# Data.courses_dict.append("java")
#使用实例对象添加
# data.courses_dict.append("java")
#使用实例对象访问
# print(data.courses_dict)
#使用类对象访问
# print(Data.courses_dict)

#实例对象给可变类型重新赋值，则是给该对象添加属性
data.courses_dict = ["Python","java"]
#使用实例对象访问
# print(data.courses_dict)
#使用类对象访问
# print(Data.courses_dict)


# class User:
#     def __init__(self,name,age):
#         """实例属性初始化"""
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"我叫{self.name}，今年{self.age}岁")
# user = User("zs",18)
# # user.introduce()
# # User.introduce(user)
# print(User.name) #类对象不能调用实例属性