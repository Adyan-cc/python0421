
# 1.存在字典 info = {'name':'张三'},给字典增加性别信息，值为“男”。
# 	清空整个字典
# 	根据键获取字典的性别信息，获取不到默认是男性
# 	删除整个字典
# info = {'name':'张三'}
# info["gender"] = "男"
# info.clear()
# print(info["gender"])
# print(info.get("gender","男"))
# del info
# print(info)
# 2.使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），
# 这些信息来自键盘的输入
# lst = ["姓名","年龄","学号","QQ","微信","住址"]
# info_dic = {}
# for i in lst:
#     string = "请输入"+i
#     ret = input(string)
#     info_dic[i] = ret
# print(info_dic)


# 3.字典dict1 = {'name':'小明','age':18,'weight':180,'score':150}，交换键和值并输出
dict1 = {'name':'小明','age':18,'weight':180,'score':150}
# dict2 = {}
# for k,v in dict1.items():
#     # print(k,v)
#     dict2[v] = k  #新字典的k是老字典的v，新字典的值是老字典的k
# print(dict2)
#字典推导式
#{k:v for k,v in dic.items()}
# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)

# 4.循环录入3个学生的学生信息(姓名，年龄，性别，分数)，存储到合理的容器中
# (可以使用字典或者列表)
# 如：[{'姓名': '李白', '年龄': '25', '性别': '男', '分数': '100'},
# {'姓名': '貂蝉', '年龄': '20', '性别': '女', '分数': '99'}, {'姓名': '吕布', '年龄': '33', '性别': '男', '分数': '35'}]
# info_lst = []
# lst = ["姓名","年龄","性别","分数"]
# for i in range(1,4):
#     info_dic = {}
#     for j in lst:
#         ret = input("请输入第%d个人的%s："%(i,j))
#         info_dic[j] = ret
#     info_lst.append(info_dic)
# print(info_lst)


# 5.列表 lst=['hello','world','python','java','web', 'UI', 'linux', 'unity']
# 请以字符串为键，长度为值建立字典。
# lst=['hello','world','python','java','web', 'UI', 'linux', 'unity']
# # str_dic = {}
# # for i in lst:
# #     # print(i,len(i))
# #     str_dic[i] = len(i)
# # print(str_dic)
# str_dic = {i:len(i) for i in lst}
# print(str_dic)


# 6.生成如下格式字典，格式如下:{'a':97,'b':98,'c':99...}
# print(chr(97),chr(122))
# info_dic = {}
# for i in range(97,123):
#     # print(chr(i),i)
#     info_dic[chr(i)] = i
# info_dic = {chr(i):i for i in range(97,123)}
# print(info_dic)



# 7.使用列表推导式输出一个10以内的偶数的平方的列表
lst = [i*i for i in range(1,11) if i%2==0]
print(lst)


# 8.商城项目综合开发，将数据，如注册用户信息等存储到列表或字典中