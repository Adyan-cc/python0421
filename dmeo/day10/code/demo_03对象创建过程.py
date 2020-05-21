

# - 申请空间-->创建对象-->属性初始化
#
# - 类名(),准备创建对象，申请内存空间-->调用`__new__`()方法，创建对象-->
# 调用`__init__`()方法，对象初始化-->将创建好的对象赋值给"="左边的变量

class User:
    """用户类型"""
    def __init__(self,username):
        """记录用户属性"""
        print("对象初始化操作")
        self.username = username
    def __new__(cls, *args, **kwargs):
        """创建对象"""
        # print("开始创建对象")
        return object.__new__(cls)
user = User("张伟强")

# 练习1：需求每位同学有自己的姓名和年龄，可以自我介绍，如：我叫xxx，今年xx岁，请多多关照！
# 分析：学生类，属性：姓名，年龄		方法：自我介绍

# class Student:
#     """学生类"""
#     def __init__(self,name,age):
#         """初始化属性"""
#         self.name = name  #stu1.name="张伟强"
#         self.age = age
#
#     def introduce(self):
#         """自我介绍的方法"""
#         # print(f"我叫{self.name}，今年{self.age}岁，请多多关照！")
#         print(f"我叫{self.name}，今年{self.age}岁，分数是{self.score}，请多多关照！")
#
# stu1 = Student("张伟强",20)
# # stu1.introduce()
#
# #可以使用  对象名.属性名 = 属性值  的方式给对象添加属性
# stu1.score = 90
# stu1.introduce()
