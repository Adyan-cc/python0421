

# class User:
#     def __init__(self,name,age):
#         """实例属性初始化"""
#         print("init方法对象初始化")
#         self.name = name
#         self.age = age
#     def __new__(cls, *args, **kwargs):
#         print("new方法开始创建对象")
#         return object.__new__(cls)
# user = User("zs",18)
# # print(user.name)
# print(user)


# class User:
#     def __init__(self,name):
#         """实例属性初始化"""
#         print("init方法对象初始化")
#         self.name = name
#
#     def __del__(self):
#         print("对象将要被删除")
#
# user = User("zs")
# print("代码执行结束")


# class User:
#     def __init__(self,name):
#         """实例属性初始化"""
#         print("init方法对象初始化")
#         self.name = name
#
#     def __del__(self):
#         print("对象将要被删除")
#
# def func():
#     user = User("zs")
# func()
# print("代码执行结束")


# __call__`()方法让对象可以类似函数的方法直接调用执行

# class User:
#     def __call__(self, *args, **kwargs):
#         print("我叫张伟强,请多多关照")
#
#     def introduce(self):
#         print("我叫刘江,请多多关照")
# user= User()
# # user.introduce()
# user()

# __eq__()方法定义==的操作

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # return self.age==other.age
        return self.__dict__==other.__dict__

    def __gt__(self, other):
        return self.age>other.age

    def __cmp__(self, other):
        # if self.age>other.age:
        #     return 1
        # elif self.age<other.age:
        #     return -1
        # else:
        #     return 0

        return (self.age>other.age)-(self.age<other.age)
user1 = User("刘江",25)
user2 = User("张伟强",23)
user3 = User("刘江",20)
# print(user1==user2) #自定义比较年龄
#自定义比较所有的属性相同，对象才相同
# print(user1<user2)

print(user1.__cmp__(user2))

# print(user1==user3)
# # == 比较的是值，is比较内存地址
# lst1 = [1,2,3]
# lst2 = [1,2,3]
# print(lst1==lst2)
# print(lst1 is lst2)