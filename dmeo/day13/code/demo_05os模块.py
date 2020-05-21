

# 重命名文件   os.rename(旧文件名，新文件名)
import os
# # os.rename("demo_02/1.txt","demo_02/111.txt")
# os.rename("demo_02/2.txt","222.txt")

# 2.删除文件 os.remove(文件名)
#删除demo_02/3.txt
# os.remove("demo_02/3.txt")

# 3.创建单层目录 os.mkdir(目录名)
#创建test1目录
# os.mkdir("test1")

# 创建多级目录 os.makedirs(目录名)
# os.makedirs("a/b/c/d")

# 删除单层目录  os.rmdir(目录名)
# os.rmdir("test1")

# 删除多级目录 os.removedirs(目录名)
# os.removedirs("a/b/c/d")

# .获取当前所在目录  os.getcwd()
# print(os.getcwd()) #获取的是绝对路径


# 6.获取目录列表  os.listdir(path)
# print(os.listdir("E:\python0421\day13\code"))

# 7.切换所在目录  os.chdir()
# print(os.getcwd())
# os.chdir("a/b")
# # print(os.getcwd())
# with open("222.txt","w")as file:
#     file.write("hello world")

# 判断文件或文件夹是否存在  os.path.exists()
# print(os.path.exists("222.txt"))
# print(os.path.exists("a"))

# 9.判断是否是文件  os.path.isfile()
# print(os.path.isfile("222.txt"))
# print(os.path.isfile("a"))

# 10.判断是否是目录  os.path.isdir()
# print(os.path.isdir("222.txt"))
# print(os.path.isdir("a"))

# #获取绝对路径 os.path.abspath()
# print(os.path.abspath("222.txt"))
#
# # 获取路径中的最后部分
# print(os.path.basename("222.txt"))
# print(os.path.basename(r"E:\python0421\day13\code\222.txt"))
#
# #判断是否是绝对路径 os.path.isabs()
# print(os.path.isabs("222.txt"))
# print(os.path.isabs(r"E:\python0421\day13\code\222.txt"))
#
# #获取文件所在目录，os.path.dirname
# print(os.getcwd())
# print(os.path.dirname(r"E:\python0421\day13\code\a\b\11.txt"))
# print(os.path.dirname(r"E:\python0421\day13\code\a\b"))

#文件定位 tell()
# with open("222.txt","r") as f:
# with open("222.txt","a") as f:
#     print(f.tell())

#seek(offset,whence) offset偏移量，whence定位(0文件开头，1定位不变，2文件结尾)
with open("222.txt","r") as f:
    print(f.tell())
    f.seek(2,0)
    print(f.tell())
    print(f.read())
