

# class User:
#     """用户类型"""
#     def __init__(self,name,age):
#         """用户姓名和年龄"""
#         self.name = name
#         self.age = age
#     def __str__(self):
#         """打印用户信息"""
#         return f"我叫{self.name},今年{self.age}岁"
#
# user = User("刘江",23)
# # print(user)
# #访问用户的姓名
# # print(user.name)
# #可以修改用户的姓名
# user.name = "徐伟明"
# user.age = -20
# print(user)


# #属性私有化之后，用户信息不可以被外部访问或者修改
# class User:
#     """用户类型"""
#     def __init__(self,name,age):
#         """用户姓名和年龄"""
#         self.__name = name
#         self.__age = age
#     def __str__(self):
#         """打印用户信息"""
#         return f"我叫{self.__name},今年{self.__age}岁"
# user = User("刘江",23)
# # print(user)
# print(user.__name)
#
# #修改用户的姓名和年龄
# # user.__name = "梁国赞"
# # user.__age = -20
#
# # print(user.__name,user.__age)
# # print(user) #还是原来的属性，并没有修改，而是增加属性



# #属性私有化之后，提供公共的访问方式和修改方式
# class User:
#     """用户类型"""
#     def __init__(self,name,age):
#         """用户姓名和年龄"""
#         self.__name = name
#         self.__age = age
#
#     def set_name(self,name):
#         """修改姓名"""
#         self.__name = name
#     def get_name(self):
#         """获取姓名"""
#         return self.__name
#
#     def set_age(self,age):
#         """修改年龄"""
#         if 0<age<=100:
#             self.__age = age
#         else:
#             print("年龄不符合要求！")
#
#     def get_age(self):
#         """获取年龄"""
#         return self.__age
#
#     def __str__(self):
#         """打印用户信息"""
#         return f"我叫{self.__name},今年{self.__age}岁"
# user = User("刘江",23)
# # print(user)
# # print(user.get_name())
# # user.set_name("小江")
# user.set_age(120)
# user.set_age(25)
# print(user)




# - 私有方法：在方法前加__ 例如：send-->`__send`()
#
# - 作用：就是在开发过程中保护核心代码，在类的外部不能使用(对象不能调用私有方法)

# class A:
#     def __test1(self):
#         print("--in test1--")
#
#     def test2(self):
#         self.__test1()
#         print("--in test2--")
# a = A()
# # a.__test1() #对象不能调用私有方法
# a.test2()




# 案例：狗生一个崽儿，休一个月产假
#
# - 属性：孩子数量
# - 方法：生孩子，休产假，生孩子后自动调用休产假的方法

# class Dog:
#     """狗的类型"""
#     def __init__(self):
#         self.__baby_count = 0 #定义狗崽儿的数量
#
#     def birth(self):
#         print("生了一个崽儿")
#         self.__baby_count+=1
#         #调用休产假的方法
#         self.__holiday()
#
#     def __holiday(self):
#         print("休一个月产假！")
#
#     def __str__(self):
#         return f"孩子数量{self.__baby_count}"
#
# dog1= Dog()
# dog1.birth()
# print(dog1)
# # dog1.__holiday() #无法调用私有方法
# dog1.baby_count = 5  #无法修改狗崽儿的数量
# print(dog1)



# 练习：打电话
#
# - 手机类
# - 方法：
#   - 通话方法（私有方法）
#   - 平台方法，检查话费余额，大于0调用通话方法

# class Phone:
#     """手机类型"""
#     def __call(self):
#         """打电话方法"""
#         print("可以打电话！")
#
#     def platform(self,money):
#         if money>0:
#             self.__call()
#         else:
#             print("电话已欠费，请充值后再拨。。。")
# phone = Phone()
# # phone.__call() #私有方法不可以通过对象直接调用
# phone.platform(20)
# phone.platform(-10)


# 私有化封装后的限制
#
# - 1.类中                   可以访问
# - 2.类外/对象外      不可访问
# - 2.子类/子类对象  不可访问
# - 注意：
#   - 1.在Python中实现的封装操作，不是通过权限限制而是通过改名策略实现的，名字变了找不到而已。
#   - 2.可以使用`__dict__`()查看属性（包括私有属性），在类内部使用的私有属性，Python内部会自动进行转换成   \_类名_属性名
#   - 3.在类的外部不能给对象添加或者修改私有属性是因为不能转换为  \_类名_属性名

# class User:
#     """用户类型"""
#     def __init__(self,name,age):
#         """用户姓名和年龄"""
#         # self.name = name
#         # self.age = age
#         self.__name = name
#         self.__age = age
#
#     def __str__(self):
#         """打印用户信息"""
#         # return f"我叫{self.name},今年{self.age}岁"
#         return f"我叫{self.__name},今年{self.__age}岁"
# user = User("刘江",23)
# # print(user)
# #属性私有化之前，对象的属性如下
# # print(user.__dict__) #{'name': '刘江', 'age': 23}
# # user.name = "徐伟明" #可以修改
#
#
# #属性私有化之后，对象的属性如下
# print(user.__dict__) #{'_User__name': '刘江', '_User__age': 23}
# # user.__name = "徐伟明" #只是增加属性
# # print(user.__dict__)
#
# user._User__name = "徐伟明"
# print(user)





# 思考：在类属性中添加私有属性，可以访问吗？可以修改吗？
class User:
    """类属性"""
    __gender = "男"
    """用户类型"""
    def __init__(self,name,age):
        """用户姓名和年龄"""
        self.__name = name
        self.__age = age

    def __str__(self):
        """打印用户信息"""
        # return f"我叫{self.name},今年{self.age}岁"
        return f"我叫{self.__name},今年{self.__age}，性别:{self.__gender}"
user = User("刘江",23)
# User.__gender = "女"  #新增类属性
User._User__gender = "女" #修改类的私有属性
print(user)
# print(User.__dict__)