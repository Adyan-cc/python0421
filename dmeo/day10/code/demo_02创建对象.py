

# class User:
#     """用户类型"""
#     def __init__(self,username,password,nickname):
#         """记录用户属性"""
#         print("开始执行对象初始化")
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
#
#
# #对象的实例属性：通过对象直接拿到实例属性
# print(user.username)
#
# # 对象的实例方法
# user.delete()


# self关键字
#
# - 描述的是当前对象自身，谁调用，self就是谁
# - 注意：声明在方法的第一个位置参数上，是一个形参，但是约定俗称使用self

class User:
    """用户类型"""
    def __init__(self,username):
        """记录用户属性"""
        print("内部self的内存地址：",id(self))
        self.username = username

# 创建user对象,会自动执行__init__()方法
user = User("张伟强")
#user = User(user,"张伟强") #内部已实现这种传递方式
#Python会将对象本身当成第一个参数传递给self
# print(user.username)

#查看对象的内存地址
print("外部创建对象的内存地址：",id(user))