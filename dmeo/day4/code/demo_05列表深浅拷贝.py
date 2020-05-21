
#简单数据类型
# string1 = "hello"
# print(id(string1))
# string1 = "world"
# print(id(string1))

#复杂数据类型
# lst = [1,2]
# print(id(lst))
# print(id(lst[0]))
# print(id(lst[1]))
# lst.append(3)
# print(lst)

# a = [10]
# lst = [1,2,a]
# a.append(11)
# print(lst)


# 浅拷贝copy  列表.copy()
# lst = [1,2]
# lst2是lst的浅拷贝(拷贝了一层)
# lst2 = lst.copy()
# lst.append(3)
# # print(lst2)
# # lst2 = lst
# print(id(lst),id(lst2))

# a = [10]
# lst = [1,2,a]
# lst2 = lst.copy()
# a.append(11)
# print(lst2)

#深拷贝
import copy
a = [10]
lst = [1,2,a]
lst2 = copy.deepcopy(lst)
a.append(11)
print(lst2)
print(id(lst[2][0]))
print(id(lst2[2][0]))
