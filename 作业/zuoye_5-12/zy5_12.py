# 1.�о�ĳ���ļ��������е��ļ�����д�뵽a.txt�ļ�
import os
# def show_file(dir_path): #����һ��Ŀ¼ "E:\python0421\day12\python0421��day12��ҵ20200511e"
#     file_lst = os.listdir(dir_path)
#     for f in file_lst: #����Ŀ¼�б�
#         path = dir_path+'/'+f #ƴ������·��
#         # print(path)
#         if os.path.isfile(path): #�ж��Ƿ����ļ����Ǿ�ֱ�Ӵ�ӡ
#             print(path)
#         elif os.path.isdir(path): #�����Ŀ¼���ݹ����
#             show_file(path)
#     with open
# show_file(r'')

# 2.�ļ����ǰ׺����һ���ļ���������.py�ļ�ǰ����������������ǰ׺
## def back_up(file):  #222.txt-->222_����.txt
#     f1 = open(file,"r",encoding="utf-8")
#     content = f1.read()
#     new_file = file.partition(".") #�����ļ������ 1.�ļ��� 2�� 3��׺
#     new_name = new_file[0]+"_����"+new_file[1]+new_file[2] #ƴ�����ļ���
#     f2 = open(new_name,"w",encoding="utf-8")
#     f2.write(content)
#     f1.close()
#     f2.close()
# back_up("222.txt")
# 3.ɾ����ո���ӵ�����ǰ׺
# def r (d):
#     f = os.linesep(d)
#     for i in f:
#         p = d + '/' + f
#         if i.endswith('.py')
#             so.chdir(d)
#

# 4.�û������ļ������Լ���ʼ����·���������ļ��Ƿ����
#    �����ļ��У�������ļ��м������������ڷ���True������ļ�����·���������ڷ���False
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