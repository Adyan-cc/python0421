
import random
# randint():生成指定范围内的随机数
# num = random.randint(1,10)
# print(num)

# random():  生成0-1直接的随机小数
# print(random.random())

# uniform():  生成指定范围内的随机小数
# print(random.uniform(1,10))

# randrange: 生成指定范围内的随机整数，可以指定步长
# print(random.randrange(1,10,2))

# random.shuffle(): 可以打乱序列
# lst = [1,2,3,4,5]
# random.shuffle(lst)
# print(lst)

# choice():  随机返回列表中的一个元素
# lst = [1,2,3,4,5]
# print(random.choice(lst))

import sys
# - sys.version 返回解释器的版本号
# print(sys.version)
# - sys.path 返回模块的搜索路径
# print(sys.path)
# - sys.argv 接受命令行下的参数
# print(random.randint(1,18))

# name = "zs"
# pwd = "123"
# ret = sys.argv
# name = ret[1]
# pwd = ret[2]
# if name=="zs" and pwd=="123":
#     print("登录成功")
# else:
#     print("登录失败")

# import string
# print(string.whitespace)

import time
#时间戳
print(time.time())
#时间元组
# ret = time.localtime()
# print(ret)
# print(ret[-2])

#当前时间字符串
# ret = time.localtime()
# ret2 = time.strftime("%Y/%m/%d %H:%M:%S",ret)
# print(ret2)

# 时间字符串转换为时间元组  strptime(时间字符串,"格式定义")
#2019-08-08是2019年的第多少天？
ret = time.strptime("2019-08-08","%Y-%m-%d")
print(ret[-2])

