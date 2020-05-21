

# print("hello world")
# print(1/0)
# print("代码结束")



# try:
#     print("hello")
#     # print(1 / 0)
#     print("world")
# except:
#     print("try中的代码有问题")
#
# print("代码结束")
# 异常类型：ZeroDivisionError,IndexError,NameError,FileExistsError,FileNotFoundError,TypeError

# try...except...else
#
# - try正常执行结束，不会走except，走else
# - try中有异常，会走except，不走else
# try:
#     print("a")
#     print(1/0)
#     print("b")
# # except ZeroDivisionError:
# #     print("0不可以是除数")
# # except NameError:
# #     print("出现命名错误")
# # except Exception:
# #     print("出现异常")
# except BaseException:
#     print("出现异常")
# else:
#     print("没有异常")



# finally：无论代码是否有异常，都会走finally
# try:
#     print("a")
#     # print(1/0)
#     print("b")
# except BaseException:
#     print("出现异常")
# else:
#     print("没有异常")
# finally:
#     print("有无异常都会执行的代码")


# 获取异常信息描述
# try:
#     print("a")
#     print(1/0)
#     print("b")
# except Exception as e:
#     print(e)

### 触发异常  raise
# - 用户可以根据业务逻辑手动的抛出异常。
#用户注册，输入注册用户名，用户名全为字母，抛出异常
# try:
#     name = input("请输入注册用户名：")
#     if name.isalpha():
#         raise Exception("不可以全部是字母")
# except Exception as e:
#     print(e)

#用户注册，输入注册用户名，如果用户名长度小于5，抛出自定义异常，输出异常信息：输入太短

# class ShortInputException(Exception):
    # def __init__(self,msg):
    #     self.msg = msg
    #
    # def __str__(self):
    #     return self.msg
    # pass

# try:
#     name = input("请输入注册用户名：")
#     if len(name)<5:
#         raise ShortInputException("输入太短")
# except Exception as e:
#     print(e)


#判断输入的字符串长度，如果小于指定长度就抛出自定义异常
class MyException(Exception):
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast
    def __str__(self):
        return f"你输入字符串长度是{self.length},规定长度是{self.atleast}"

try:
    content = input("请输入内容:")
    if len(content)<5:
        raise MyException(len(content),5)
except Exception as e:
    print(e)