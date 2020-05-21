# 1.列举某个文件夹内所有的文件名，写入到a.txt文件
import os
# def show_file(dir_path): #传递一个目录 "E:\python0421\day12\python0421班day12作业20200511e"
#     file_lst = os.listdir(dir_path)
#     for f in file_lst: #遍历目录列表
#         path = dir_path+'/'+f #拼接完整路径
#         # print(path)
#         if os.path.isfile(path): #判断是否是文件，是就直接打印
#             print(path)
#         elif os.path.isdir(path): #如果是目录，递归调用
#             show_file(path)
#     with open
# show_file(r'')

# 2.文件添加前缀，将一个文件夹内所有.py文件前都添加上你的名字做前缀
## def back_up(file):  #222.txt-->222_副本.txt
#     f1 = open(file,"r",encoding="utf-8")
#     content = f1.read()
#     new_file = file.partition(".") #将旧文件名拆分 1.文件名 2点 3后缀
#     new_name = new_file[0]+"_副本"+new_file[1]+new_file[2] #拼接新文件名
#     f2 = open(new_name,"w",encoding="utf-8")
#     f2.write(content)
#     f1.close()
#     f2.close()
# back_up("222.txt")
# 3.删掉你刚刚添加的所有前缀
# def r (d):
#     f = os.linesep(d)
#     for i in f:
#         p = d + '/' + f
#         if i.endswith('.py')
#             so.chdir(d)
#

# 4.用户输入文件夹名以及开始搜索路径，搜索文件是否存在
#    遇到文件夹，则进入文件夹继续搜索，存在返回True并输出文件完整路径，不存在返回False
# def s (d,f):
#     l = os.linesep(d)
#     for i in f:
#         p = d + '/' + i
#         if os.path.isfile(path):
#             if i == file:
#                 print(path)
#             return  True
#         elif so.path.isdir(path):
#             return setattr()