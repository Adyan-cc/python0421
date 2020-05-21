import re

# ret = re.match('速度与激情\s','速度与激情 ')  #'速度与激情 '
# print(ret)
# \w :匹配单词字符（a-z，A-Z,0-9,_)
# ret = re.match('\w','1') #1
# ret = re.match('\w','A') #A
# ret = re.match('\w','a') #a
# ret = re.match('\w','—') # _
# ret = re.match('\w','@') #None
# ret = re.match('\w','无')  #无  可匹配中文字符
# print(ret)

# \W   匹配非单词字符
# ret = re.match('\w','1') #None
# # ret = re.match('\w','A')#None
# # ret = re.match('\w','a') #None
# # ret = re.match('\w','—') #None
# # ret = re.match('\w','@') #@
# # ret = re.match('\w','无')  #None
# # print(ret）


# 匹配多个字符
# 1.{m}：匹配前一个字符出现m次
# 案例：匹配合法手机号
# ret = re.match('\d {11}', '12345678901') #12345678901
# ret = re.match('1\d {10}', '32345678901') #None
# ret = re.match('1\d {10}', '3234ad78901') #None
# ret = re.match('1\d {10}', '123456789011qwerty')
# print(ret)

# 2.{m,n}:匹配前一个字符出现m到n次
# 案例：验证座机
# 列如： 010-1234567,  0558-8080255
# 规则：区号是3-4位数字，电话号是7-8位数，中间用-连接
# ret = re.match('\d{3,4}-\d{7,8}','010-1234567')  # '010-1234567'
# ret = re.match('\d{3,4}-\d{7,8}','0558-8080255')  # '0558-8080255'
# ret = re.match('\d{3,4}-\d{7,8}','0558-8080255a')  # '0558-8080255'
# print(ret)

# 3.?:前一个字符出现0或者1次，要么出现0次，要么出现1次
# 案例：验证座机
# 列如： 010-1234567,  0558-8080255
# 规则：区号是3-4位数字，电话号是7-8位数，中间用-连接，区号和电话中间_可有可无
# ret = re.match('\d{3,4}-\d{7,8}','0101234567')  # None
# ret = re.match('\d{3,4}-?\d{7,8}','05588080255a')  #'05588080255'
# ret = re.match('\d{3,4}-?\d{7,8}','0558@8080255a')  # None
# print(ret)

# 4. *:匹配前一个字符出现0次或多次
# 把一个文本内容全部提取出来
# content = 'life is short,I use Python'  # 'life is short,I use Python'
# content = 'life is short,I use\n Python'
# re.S可以匹配多行
# ret = re.match('.*',content,re.S)  # 'life is short,I use\n Python'
# ret = re.match('.*','')  # ''
# print(ret)

# 5.+:匹配前一个字符出现1次或多次，至少出现一次
# ret = re.match('a+','aaaaaa')  # 'aaaaaa'
# ret = re.match('a+','')  # None
# print(ret)

# 匹配开头与结尾
# 1.'^':匹配开头的字符串
# ret = re.search('ujiuye','www.ujiuye.com')  # 'ujiuye'
# # ret = re.search('^ujiuye','www.ujiuye.com')  # None
# ^用在[]中表示取反
# ret = re.search('速度与激情[^6]','速度与激情9')
# print(ret)

# 2.$:匹配以xxx结尾的字符串
# 案例：匹配出合法的手机号
# 规则;11位数字，且第一位是1
# ret = re.match("1\d{10}",'12345678901qwe')  # 匹配成功但不符合要求
# ret = re.match("1\d{10}$",'12345678901qwe')  # None
# print(ret)
# 案例1：匹配出合法的变量名
# names = ["age1","1age","AGO_","_9age","age_","a9#_2","a#ge"]
# # 匹配规则：字符由数字，字母，下划线组成，首字符不能是数字
# for i in names:
#     ret = re.match('^[a-zA-Z_]\w*',i)
#     if ret:
#         print("%s合法"%ret.group())

# 案例2：匹配合法的163邮箱
# 每邮箱以‘@163.com’结尾，@之前4-20个单词字符
# email_list = ["zhangweiqinag@163.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com.cn","liang@163ccom"]
# for f in email_list:
#     ret = re.match('\w{4,20}@163\.com$', f)
#     if ret:
#         print("%s合法"%ret.group())

# 匹配分组
# 1.|：匹配左右任意一个表达式
# 匹配出合法的163或者126或者qq
# email_list = ["zhangweiqinag@163.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com.cn","liang@163ccom"]
# for f in email_list:
#     ret = re.match('\w{4,20}|163\.com$', f)
#     if ret:
#         print("%s合法"%ret.group())
#
# 2.（ad）：分组
# email_list = ["zhangweiqinag@126.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com","liang@163ccom"]
# for f in email_list:
#     ret = re.match('\w{4,20}@(163|qq|126)\.com$', f)
#     if ret:
#         print("%s合法" % ret.group())

# 3.引用分组：引用分组匹配到的字符串
# 案例：检查html网页语法的合法性
# 语法规则：标签必须配对
# content = '<h1>hello world</h1>'
# content = '<h1>hello world</h2>'
#不严谨的写法
# # ret = re.match('<\w+>.*</\w+>',content)
# ret = re.match('<(\w+)>.*</\\1>',content)
# print(ret)

# 4.给分组起别名 （?P<name,名字随意>）

#5.（?P=name）：引用别名为name的分组匹配到字符串
# content = '<h1><boby>hello world</boby></h1>'
# # ret = re.match('<(\w+)><(\w+)>.*</\\2></\\1>',content)
# ret = re.match('(?P<a>\w+)><(?P<b>\w+)>.*</(?P=b)></(?P=a)>',content)
# print(ret)

# re模块的其他用法 setattr()，findall（），sub（）
# setattr()，查看匹配的数据，匹配到立即反复
# c = '阅读次数88次，下载次数30次'
# r = re.search('\d+',c)
# print(r)
# findall（）:查找字符串中所有的数据，返回列表
# c = '阅读次数88次，下载次数30次'
# r = re.findall('\d+',c)
# print(r)
# sud ：替换，返回的是替换后的字符串
# 将所有的数据归零
# c = '阅读次数88次，下载次数30次'
# r = re.sub('\d+','0',c)
# print(r)

# 贪婪和非贪婪
# python中默认为贪婪，总是尝试尽可能多的匹配字符，非贪婪相反
# ret = re.match('r\d{2,5}','12345')
# print(ret)


# 迭代器
# from collections import Iterable
# print(isinstance([],Iterable))  # True
# print(isinstance(123,Iterable))  #False
# for i in 'hello':
#     print(i)

# __iter__和__next__
# for i in "hello":
#     print(i)
# s = "hello"
# # 获取迭代器
# q = iter(s)
# # 使用next元素
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))
# print(next(q))

# 迭代器实现斐波那契数列
# class Fib:
#     def __init__(self,n):
#         self.n = n  # 第几个数
#         self.a = 1
#         self.b = 1
#         self.index = 0  # 记录位置
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<self.n:
#             n = self.a
#             self.a, self.b = self.b, self.a+self.b
#             self.index += 1
#             return n
#
#         else:
#             raise StopIteration
# fib = Fib(5)
# # f = Fib()
# # print(isinstance(f,ImportError))

# 生成器
# def func():
#     print('__func')
#     yield 1
#     print('__func2')
#     yield 2
# g = func()
# # print(g)
# print(next(g))
# print(next(g))
# next(g)  # 超出抛出异常
# 生成器实现斐波那契
# def fib(n):
#     a,b = 1,1
#     index = 0
#     print('。。。1...')
#     while index<n:
#         print('。。。2...')
#         yield a
#         a,b = b,a  + b
#         index+=1
#         print('。。。3..')
# g = fib(5)
# for i in g :
#     print(i,end=' ')

# send() 用法
# def generator():
#     print('a')
#     count = yield 1  # count 值返回给了第一个print(g.__next__())
#     print('q',count)  # 所以此处 count 返回 None  #  send 可以传递一个数据给第二个 count 改变第一个 yield的返回值
#     print('b')
#     yield 2
#     print('c')
# g = generator()
# print(g.__next__())
# # print(g.__next__())
# print(g.send(10))

# yield from 循环遍历容器类型
# def func():
#     yield from 'hello'
#     yield from range(3)
# f = func()
# for i in f :
#     print(i,end=' ')


