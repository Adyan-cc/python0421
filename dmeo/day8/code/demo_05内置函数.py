
#abs()
# print(abs(-5))

# max() 函数 ：求最大值    max(数据)
# lst = [2,1,6,3,4]
# ret = max(lst)
# print(ret)

# lst2 = [-2,5,-8,3,6,1]
# def abs(num):
#     if num>0:
#         return num
#     else:
#         return -1*num
#求绝对值最大的数   -8
# ret = max(lst2,key=abs) #[2,5,8,3,6,1]
# print(ret)
#练习：
# lst3 = [2,6,-10,50]
#求相反数最大的数   -10
# def func(num):
#     return -1*num
# ret = max(lst3,key=func)
# print(ret)

lst = [
    {"name":"梁少天","age":20,"score":90},
    {"name":"朱益锋","age":22,"score":95},
    {"name":"魏春平","age":21,"score":97},
]
#返回年龄最大的那组信息  {"name":"朱益锋","age":22,"score":95}
#返回分数最大的那组信息  {"name":"魏春平","age":21,"score":97}
# def max_age(dic):
#     return dic["age"]
# ret1 = max(lst,key=max_age)
# print(ret1)
#
# def max_score(dic):
#     return dic["score"]
# ret2 = max(lst,key=max_score)
# print(ret2)


# string = "abc1122aabdddccddwddd"
# #使用max()函数找出出现次数最多的字符
# ret = max(string,key=string.count)
# print(ret)

# map(func,iterable) 函数,第一个参数是函数，第二个参数是可迭代对象。
# 函数会作用在可迭代内容的每一个元素上进行计算，返回一个新的可迭代内容
#求列表中每一个元素的平方
# lst3 = [1,2,3]
# ret = [i*i for i in lst3]
# print(ret)
# def func(num):
#     return num**2
# ret = map(func,lst3)
# print(ret)
# # for i in ret:
# #     print(i,end=' ')
# print(list(ret))

#求两个列表中元素相加的和
# lst1 = [1,2,3,4,5,6,7,8]
# lst2 = [2,3,4,5,6]
# def func(x,y):
#     return x+y
# ret = map(func,lst1,lst2)
# print(list(ret))

# filter(func，iterable) 函数：用于过滤序列，过滤不符合条件的元素，
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进判
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中
# lst4 = [1,2,3,4,5,6,7,8,9]
# #过滤列表中的所有奇数
# def func(num):
    # if num%2==0:
    #     return True
    # else:
    #     return False
    # return num%2==0
#     return True if num%2==0 else False
# ret = filter(func,lst4)
# print(list(ret))

# zip 函数接受任意多个可迭代对象作为参：数,将对象中对应的元素打包成一个 tuple
# 然后返回一个可迭代的 zip 对象zip()
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# #转换为（1,4）,(2,5),(3,6)
# ret = zip(lst1,lst2)
# print(list(ret))

# str1 = "abc"
# str2 = "12345"
# ret = zip(str1,str2)
# print(tuple(ret))

# 现有两个元组(('a'),('b')),(('c'),('d'))，请生成[{'a':'c'},{'b':'d'}格式。
tup1 = ('a','b')
tup2 = ('c','d')
# def func(x,y):
#     return {x:y}
# ret = map(func,tup1,tup2)
# print(list(ret))

# def func(tup):
#     return {tup[0]:tup[1]}
# ret = zip(tup1,tup2)
# # print(tuple(ret))
# ret2 = map(func,ret)
# print(list(ret2))

ret = list(map(lambda tup:{tup[0]:tup[1]},zip(tup1,tup2)))
print(ret)