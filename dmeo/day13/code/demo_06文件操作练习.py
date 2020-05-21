# 1.封装函数，可以实现文件复制（先读取目标文件，再写入新文件）
# 如：将111.txt复制一份，文件名为222.txt
# def copy_file(file):
#     f1 = open(file,"r",encoding="utf-8")
#     content = f1.read()
#     f2 = open("333.txt","w",encoding="utf-8")
#     f2.write(content)
#     f1.close()
#     f2.close()
#
# copy_file("222.txt")


# 2.封装函数，可以实现文件备份（先读取目标文件，再写入新文件）
# 如：将111.txt复制一份，文件名为111_副本.txt
# def back_up(file):  #222.txt-->222_副本.txt
#     f1 = open(file,"r",encoding="utf-8")
#     content = f1.read()
#     new_file = file.partition(".") #将旧文件名拆分 1.文件名 2点 3后缀
#     new_name = new_file[0]+"_副本"+new_file[1]+new_file[2] #拼接新文件名
#     f2 = open(new_name,"w",encoding="utf-8")
#     f2.write(content)
#     f1.close()
#     f2.close()
# back_up("222.txt")


# 3.封装函数，打印某个文件内的所有的文件名
import os
def show_file(dir_path): #传递一个目录 "E:\python0421\day12\python0421班day12作业20200511e"
    file_lst = os.listdir(dir_path)
    # print(file_lst)
    for f in file_lst: #遍历目录列表
        path = dir_path+'/'+f #拼接完整路径
        # print(path)
        if os.path.isfile(path): #判断是否是文件，是就直接打印
            print(path)
        elif os.path.isdir(path): #如果是目录，递归调用
            show_file(path)

show_file(r"E:/python0421/day12/python0421班day12作业20200511")