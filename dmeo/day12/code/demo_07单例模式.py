

# 是否是第一次创建对象，如果是首次创建对象，则调用父类`__new__`()方法创建对象并返回
# ​如果不是第一创建对象，直接返回第一次创建的对象即可
# class Shopping:
#     instance = None #记录创建的对象，None说明是第一次创建对象
#     def __new__(cls, *args, **kwargs):
#         #第一次调用new方法，创建对象并记录
#         #第2-n次调用new方式时，不创建对象，而是直接放回记录的对象
#
#         #判断是否是第一次创建对象
#         if cls.instance==None:
#             cls.instance = object.__new__(cls)
#             return cls.instance
#         else: #不是第一次创建对象
#             return cls.instance
#
# shop1 = Shopping()
# shop2 = Shopping()
# print(shop1,shop2)


# class Shopping:
#     instance = None #记录创建的对象，None说明是第一次创建对象
#     def __new__(cls, *args, **kwargs):
#         #第一次调用new方法，创建对象并记录
#         #第2-n次调用new方式时，不创建对象，而是直接放回记录的对象
#
#         #判断是否是第一次创建对象
#         if cls.instance==None:
#             cls.instance = object.__new__(cls)
#         return cls.instance
#
# shop1 = Shopping()
# shop2 = Shopping()
# print(shop1,shop2)

class Shopping:
    def __new__(cls, *args, **kwargs):
        #第一次调用new方法，创建对象并记录
        #第2-n次调用new方式时，不创建对象，而是直接放回记录的对象

        #判断是否是第一次创建对象,判断是否有instance属性
        if not hasattr(cls,"instance"):
            cls.instance = object.__new__(cls)
        return cls.instance

shop1 = Shopping()
shop2 = Shopping()
print(shop1,shop2)