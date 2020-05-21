

# set1 = {3,2,6,4,1,3,6}
# # set1 = {3,2,6,4,1,3,6,[2]} #集合中的元素只能是不可变类型
# print(set1)

#去除列表中重复的元素
# lst = [1,2,2,3,3,5,6,3]
# print(set(lst))

#集合增加
# set1 = {1,2}
# # # set1.add(3)
# # set2 = {2,3}
# # set1.update(set2)
# set1.clear()
# print(set1)
# print(dir(set1))
# lst = [1,2]
# help(lst.remove)


#集合数学运算
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
#取交集
# print(set1&set2) #{4, 5}
# print(set1.intersection(set2))

#取并集
# print(set1|set2)
# print(set1.union(set2))

#取差集
#取set1中有，但是set2中没有的元素
# print(set1-set2)
# print(set1.difference(set2))

#反交集
# print(set1^set2)
# print(set1.symmetric_difference(set2))


# set1 = {1,2,3,4,5}
# set2 = {4,5}
#判断是否是子集
# print(set1<set2)
# print(set1.issubset(set2))
#判断是否是超集
# print(set1>set2)
# print(set1.issuperset(set2))

