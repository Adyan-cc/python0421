


# 1.列举某个文件夹内所有的文件名，写入到a.txt文件

import os
# def show_file(dir_path,file): #传递一个目录 "E:\python0421\day12\python0421班day12作业20200511e"
#     file_lst = os.listdir(dir_path)
#     for f in file_lst: #遍历目录列表
#         path = dir_path+'/'+f #拼接完整路径
#         if os.path.isfile(path): #判断是否是文件，是就直接打印
#             file.write(f+'\n')
#         elif os.path.isdir(path): #如果是目录，递归调用
#             show_file(path,file)
#             file.write(f+'\n')
#             print()
#
# file = open("a.txt","a+",encoding="utf-8")
# show_file(r"E:/python0421/day12/python0421班day12作业20200511",file)

# file = open("1.txt","w")
# file.write("hello")
# file.write("world")
# file.close()

# 2.文件添加前缀，将一个文件夹内所有.py文件前都添加上你的名字做前缀
#demo_05os模块.py-->陈星航demo_05os模块.py
# def add_name(dir_path):
#     file_lst = os.listdir(dir_path) #获取目录列表
#     for f in file_lst: #遍历目录列表
#         path = dir_path + '/' + f  # 拼接完整路径
#         if os.path.isfile(path): #判断是否是文件，是继续判读是否是.py文件
#             if f.endswith(".py"):
#                 os.chdir(dir_path) #进入到目录
#                 os.rename(f,"陈星航"+f)
#         else:
#             add_name(path)
# add_name(r"E:\python0421\code")



# 3.删掉你刚刚添加的所有前缀
# def remove_name(dir_path):
#     file_lst = os.listdir(dir_path) #获取目录列表
#     for f in file_lst: #遍历目录列表
#         path = dir_path + '/' + f  # 拼接完整路径
#         if os.path.isfile(path):  # 判断是否是文件，是继续判读是否是.py文件
#             if f.endswith(".py"):
#                 os.chdir(dir_path)  # 进入到目录
#                 names = f.partition("陈星航")
#                 os.rename(f,names[2])
#         else:
#             remove_name(path)
# remove_name(r"E:\python0421\code")

# 4.用户输入文件夹名以及开始搜索路径，搜索文件是否存在
#    遇到文件夹，则进入文件夹继续搜索，存在返回True并输出文件完整路径，不存在返回False

def search_file(dir_path,file):
    file_lst = os.listdir(dir_path) #获取目录列表
    for f in file_lst: #遍历目录列表
        path = dir_path + '/' + f  # 拼接完整路径
        if os.path.isfile(path):  # 判断是否是文件，是继续判读是否是.py文件
            if f==file:
                print(path)
                return True
        elif os.path.isdir(path):
            ret = search_file(path,file)
            if ret==True:
                return True
    else:
        return False
ret = search_file(r"E:\python0421","222.txt")
print(ret)