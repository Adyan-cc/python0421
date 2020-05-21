

#增加
lst = ["张伟强","刘江","徐伟明","刘伟超"]
#在列表尾部增加 “梁国赞”append
lst.append("梁国赞")
# print(lst)
#extend
# lst2 = ["梁国赞","张威"]
# lst.extend(lst2)
# print(lst)
# lst = ["张伟强","刘江","徐伟明","刘伟超"]
#insert
#将"梁国赞"插入到“刘江”的前面
# lst.insert(1,"梁国赞")
# print(lst)
#将"梁国赞"插入到“刘伟超”的前面
# lst.insert(-1,"梁国赞")
# print(lst)
#将"梁国赞"插入到“刘伟超”的后面
# lst.insert(5,"梁国赞")
# print(lst)

#删除
#pop()
# lst = ["张伟强","刘江","徐伟明","刘伟超"]
#删除 刘江
# lst.pop(1)
# ret = lst.pop()
# print(ret)
# print(lst)
# remove()
# lst = ["张伟强","刘江","徐伟明","刘伟超","刘江"]
#删除刘江
# lst.remove("刘江")
# print(lst)
#clear()
# lst.clear()
# print(lst)
#del
#删除列表
# del lst
# print(lst)
#删除刘江
# del lst[1]
# print(lst)

#修改
# lst = ["张伟强","刘江","徐伟明","刘伟超","刘江"]
#将"张伟强"修改为"小张"
# lst[0] = "小张"
# print(lst)
#reverse
# lst.reverse()
# print(lst)

#sort
# lst = [4,6,1,3,5]
# lst.sort()
# lst.sort(reverse=True)
# #从大到小排序
# print(lst)
# sorted()
# lst2 = sorted(lst)
# lst2 = sorted(lst,reverse=True)
# print(lst)
# print(lst2)

#A:65,a:97
# lst = ['a','c','b']
# lst.sort()
# print(lst)
# lst = ['abc',"ABC","aBe"]
#step1：先比较每个字符串的第一个字符的ascii码值
# "abc"-->"a"   97
# "ABC"-->"A"   65
# "aBe"-->"a"   97
#得出 "ABC"最小
#step1：再比较"abc"和"aBe"的第二个字符的ascii码值
# "abc"-->"b"   98
# "aBe"-->"B"   66
#得出"aBe"<"abc"
#最终："ABC"<"aBe"<"abc"
# lst.sort()
# print(lst)

# lst = ['a','3','1','e','5','b']
# lst.sort()
# print(lst)

#查找
# lst = [1,2,3,7,2,6,2,3,2]
# #查看2出现的次数
# # print(lst.count(2))
# #查看2的索引
# print(lst.index(2))
# print(lst.index(3))


#注意：列表不可以一边遍历，一边删除
# lst = [1,2,2,2,5,6,7,2,9]
#将列表中的2全部删除
# for i in lst:
#     if i==2:
#         lst.remove(i)
# print(lst)


# new_lst = []
# for i in lst:
#     if i!=2:
#         new_lst.append(i)
# print(new_lst)

# lst_2 = [] #将所有的2存起来
# for i in lst:
#     if i==2:
#         lst_2.append(i)
# for j in lst_2:
#     lst.remove(j)
# print(lst)


#列表嵌套
# lst = [[1,2,3],[4,5,6],[7,8,9]]
#取出3
# print(lst[0][2])
#取出1,4,7
# for i in lst:
#     print(i[0])

#len()函数
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(lst))

#练习
#取出1,5,9
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(range(5)))
# print(range(len(lst)))
#列表的长度比最大索引大1
# for i in range(len(lst)):
#     print(lst[i][i])

#创建一个空列表，循环生成5个10以内的数字，添加到列表中
#查询列表中是否有元素3，如果有，删除该元素
import random
lst = []
for i in range(5):
    ret = random.randint(0,3)
    if ret!=3:
        lst.append(ret)
print(lst)