# class User:
#     """用户类型"""
#     def __init__(self,username,password,nickname):
#         """记录用户属性"""
#         self.username = username
#         self.password = password
#         self.nickname = nickname
#
#     def save(self):
#         """保存方法"""
#         pass
#
#     def delete(self):
#         """删除方法"""
#         print("执行删除操作")
# # 创建user对象,会自动执行__init__()方法
# user = User("张伟强","123","强哥")
# print(user)
# print(id(user))

#可以通过 对象名.属性名 查看属性值，但是当属性比较多时，查看属性就不太方便
#打印对象时，会自动调用__str__()方法
# class User:
#     """用户类型"""
#     def __init__(self,username,password,nickname):
#         """记录用户属性"""
#         self.username = username
#         self.password = password
#         self.nickname = nickname
#     def __str__(self):
#         print("--str--")
#         # return "123"
#         return f"{self.username} {self.password} {self.nickname}"
# user = User("张伟强","123","强哥")
# #打印对象会自动执行__str__()方法
# print(user)
# print([user])

#在类型中添加一个__repr__()方法，用于对象包含在组合数据类型中时，按照自定义的方式展示对象的数据
# class User:
#     """用户类型"""
#     def __init__(self,username,password,nickname):
#         """记录用户属性"""
#         self.username = username
#         self.password = password
#         self.nickname = nickname
#     # def __str__(self):
#     #     print("--str--")
#     #     return f"{self.username} {self.password} {self.nickname}"
#
#     def __repr__(self):
#         print("--repr--")
#         return f"{self.username} {self.password} {self.nickname}"
# user = User("张伟强","123","强哥")
# #打印对象会自动执行__str__()方法,如果没有此方法，会寻找__repr__()方法
# print(user)
# print([user])


class Student:
    """学生类"""
    def __init__(self,name,age):
        """初始化属性"""
        self.name = name  #stu1.name="张伟强"
        self.age = age

    def __str__(self):
        """自我介绍的方法"""
        return (f"我叫{self.name}，今年{self.age}岁，请多多关照！")

stu1 = Student("张伟强",20)
print(stu1)
