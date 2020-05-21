
# read()
# - 调用 read()会一次性读取文件的全部内容，如果文件有 10G，内存就爆了，会导致程序卡死，
# 所以，要保险起见，可以反复调用 read(size)方法，每次最多读取 size 个字符的内容

# file = open("demo_02/2.txt","r")
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))
# file.close()

# readline 每次读取一行，并且自带换行功能 每一行末尾会读到\n
# #可以指定每行读取的字符长度，下一次读取会从此位置开始
# file = open("demo_02/1.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# 一次性以行的形式读取文件的所有内容并返回一个 list，需要去遍历读出来
# file = open("demo_02/1.txt","r")
# ret = file.readlines()
# # print(ret)
# for i in ret:
#     print(i,end='')
# file.close()

# file 句柄是一个可迭代的对象因此，可以循环读取文件中的内容，每次读一行
# file = open("demo_02/1.txt","r")
# for i in file:
#     print(i,end='')
# file.close()

# 写入write和writelines(多行一次性写入)
# file = open("demo_02/3.txt",'w')
# # file.write("zhangweiqiang")
#
# lst = ["hello","world","zs","ls"]
# for i in lst:
#     file.write(i)
# # file.writelines(lst)
#
# file.close()


import csv

# print(dir(csv))
# help(csv.reader)

# 必须创建 csv 模块中对应的 writer 对象，通过 writer 对象完成文件内容的写入操作
"""
电影名称  评分  演员  网址
战狼     9.0    吴京   www.zhanlang.com
战狼2    9.2    吴京   www.zhanlang2.com
"""
# file = open("demo_02/movie.csv","w",newline="")
# writer = csv.writer(file)
# writer.writerow(["电影名称","评分","演员","网址"])
# writer.writerows([["战狼"," 9.0","吴京","www.zhanlang.com"],
#                  ["战狼2"," 9.2","吴京","www.zhanlang2.com"]])
# file.close()

# 读取 csv 文件的操作，主要通过 csv 模块中的 reader 对象来完成，
# 通过加载文件数据到 reader 对象中，文件中的数据就会按照固定的格式读取到程序中进行处理
# file = open("demo_02/movie.csv","r",newline="")
# reader = csv.reader(file)
# # print(reader)  #<_csv.reader object at 0x0000000002205F50>
# for i in reader:
#     print(i)
# file.close()

# 爬取豆瓣电影写入csv文件
from demo.movie import movie_dict2
# print(movie_dict2)
# for i in movie_dict2["data"]:
#     # print(i)
#     print(i["title"],i["rate"],i["casts"],i["url"])

#提取电影名称、评分、演员、网址写入到csv文件
# import csv
# file = open("demo_02/movie2.csv","w",newline="")
# writer = csv.writer(file)
# writer.writerow(["电影名称","评分","演员","网址"])
# for i in movie_dict2["data"]:
#     # print(i["title"],i["rate"],i["casts"],i["url"])
#     movie_name = i["title"]
#     rate = i["rate"]
#     casts = i["casts"]
#     url = i["url"]
#     writer.writerow([movie_name,rate,casts,url])
#
# file.close()

# 使用 with 方式操作文件，可以不用关闭文件，会自动关闭文件

# with open("demo_02/1.txt","r") as file:
#     print(file.read())

#with 内部实现了__enter__和__exit__方法，会自动关闭文件

# class Foo:
#     def __init__(self):
#         print("--init--")
#     def test(self):
#         print("--test--")
#     def __enter__(self):
#         print("enter")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("with执行完毕，调用exit")
# with Foo() as f:
#     f.test()
# print("最后一行代码")

with open("demo_02/5.txt","w",encoding="utf-8") as file:
    file.write("人生苦短，我用python！")