
# tup1 = ("张伟强","刘江","张威")
# print(tup1)
# print(type(tup1))
# #通过索引获取“刘江”
# print(tup1[1])
# #切片获取"刘江","张威"
# tup2 = tup1[1::] #返回的是元组
# print(tup2)
# #通过for循环获取所有元素
# for i in tup1:
#     print(i)

#元组的合并和重复：合并：+    重复：*
# tup1 = ("许博宁","梁少天")
# tup2 = ("陈星航","谢海平")
# # print(type(tup1))
# tup3 = tup1+tup2
# print(tup3)
# tup4 = tup1*3
# print(tup4)

#多维元组
# tup1 = (("许博宁",18),("陈星航",25),("梁少天",20))
# #获取每个人的姓名
# for i in tup1:
#     print(i[0])

#使用多个变量接收值
#可以使用序列解包
# tup1 = ("许博宁",18,180)
# name,age = tup1
# print(name)
# print(age)
# tup2 = (1,2,3,4,5)
# v1,*v2 = tup2
# print(v1)
# print(v2)

#如果元素本身是一个可变数据类型的列表，那么其嵌套项可以被改变
# a = [3]
# tup1 = (1,2,a)
# a.append(4)
# print(tup1)

#列表深浅拷贝，
# 列表中有元组,如果元组中都是不可变数据，则元组无法拷贝
#如果元组中有可变数据，则元组可以拷贝
# import copy
# # tup1 = (3,4)
# a = [5]
# tup1 = (3,4,a)
# lst = [1,2,tup1]
# lst2 = copy.deepcopy(lst) #lst2是lst的深拷贝
# print(id(lst[2]),id(lst2[2]))
# a.append(6)
# print(lst,lst2)


# tuple()函数
# lst = ["许博宁","梁少天"]
# tup1 = tuple(lst)
# print(tup1)
# print(list(range(1,5)))
# print(tuple(range(1,5)))
# string = "hello"
# print(list(string))
# print(tuple(string))
# num = 1
# print(tuple(num)) #数值型无法转换为元组


# - index  从左往后返回第一个遇到的指定元素的索引，如果没有，会报错     元组.index(元素)
# - count  返回元组当中指定元素的个数    元组.count(元素)
# tup1 = (1,2,3,5,7,2,3)
# print(tup1.index(2))
# # print(tup1.index(12)) #找不到对应的索引会报错
# print(tup1.count(2))

# tup1 = ("许博宁","梁少天","陈星航","谢海平")
# for i in enumerate(tup1,1):
#     print(i)


#max(),min(),sum()
#求最大值，最小值，求和的函数

#练习1：元组求和
# tup1 = (1,2,3,4,5,6,7,8,9)
# sum_num = 0
# for i in tup1:
#     sum_num+=i
# print(sum_num)
# print(sum(tup1))

#练习2：求1-100范围内偶数的和
# ret = sum([i for i in range(2,101,2)])
# print(ret)

#练习3：输出元组内最大值和最小值及其下标
# tup1 = (20,11,3,44,8,9,5,6)
# max_num = min_num = tup1[0]
# max_index=min_index = 0
# for i in tup1:
#     if max_num<i:
#         max_num = i
#         max_index = tup1.index(i)
#     elif min_num>i:
#         min_num = i
#         min_index = tup1.index(i)
# print("最大值及对应索引：",(max_num,max_index))
# print("最小值及对应索引：",(min_num,min_index))
# print("最大值及对应索引：",(max(tup1),tup1.index(max(tup1))))
# print("最小值及对应索引：",(min(tup1),tup1.index(min(tup1))))

#练习4:生成所有(x,y)的元组
#x是0-5之间的偶数，y是0-5之间的奇数
# lst = []
# for x in range(0,6,2):
#     for y in range(1,6,2):
#         # print((x,y))
#         lst.append((x,y))
# print(lst)

lst = [(x,y) for x in range(0,6,2) for y in range(1,6,2)]
print(lst)