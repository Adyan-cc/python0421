

# string1 = "hello"
# string2 = string1
# string3 = "hello"
# print(id(string1),id(string2),id(string3))
# lst1 = [1,2,3]
# lst2 = lst1
# lst3 = [1,2,3]
# print(id(lst1),id(lst2),id(lst3))

# string = "hello world"
# #获取 e
# print(string[1])
# #获取d
# print(string[-1])

num_str = "0123456789"
# 1. 截取从 2 ~ 5 位置 的字符串
# print(num_str[2:6])
# 2. 截取从 2 ~ `末尾` 的字符串
# print(num_str[2:])
# 3. 截取从 `开始` ~ 5 位置 的字符串
# print(num_str[:6])
# 4. 截取完整的字符串
# print(num_str[:])
# 5. 从开始位置，每隔一个字符截取字符串
# print(num_str[::2])
# 6. 从索引 1 开始，每隔一个取一个
# print(num_str[1::2])
# 倒序切片
# -1 表示倒数第一个字符
# 7. 截取从 2 ~ `末尾 - 1` 的字符串
# print(num_str[2:-1])
# print(num_str[2:])
# 8. 截取字符串末尾两个字符
# print(num_str[-2:])
# 9. 字符串的逆序
# print(num_str[::-1])

# num = input("请输入一个整数：")
# print(num[::-1])

#字符串的遍历
# string = "hello world"
# for i in string:
#     print(i)
# else:
#     print("程序执行完了")

# - “+” ：将两个字符串合并成一个新的字符串
# - “*” :将一个字符串进行连续拼接
# string1 = "hello"
# string2 = "world"
# # string2 = 3
# ret1 = string1+string2
# ret2 = string1*3
# # print(ret1)
# print(ret2)

# 字符串的赋值语句
# - 可以使用多个变量接收值
# string = "zs"
# s1,s2 = string
string = "zsls"
s1,*s2 = string
print(s1)
print(s2)

a = 1,
print(a)