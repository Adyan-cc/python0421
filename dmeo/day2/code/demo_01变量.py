"""
变量的使用
时间：
作者
版本：
"""
# qq_num = 1512211 #将等号右边的数据赋值给左边的变量
# qq_pwd = 12138
# print(id(qq_pwd))
# print(qq_num)
#可以使用变量接收用户输入的数据
# qq_num = input("请输入qq账号：") #字符串
# print(qq_num)

# 首次赋值会被定义，再次赋值会改变变量的指向
# qq_pwd = "zhangwei12138"
# # print(qq_num,qq_pwd)
# print(id(qq_pwd))

#多个单词定义变量
#分别定义 姓和名
#下划线命名法
# first_name = "刘"
# last_name = "江"
#大驼峰命名法：每个单词首字母大写
# FirstName = "刘"
# LastName = "江"
#小驼峰命名法：除首单词外，后续单词首字母大写
# firstName = "刘"
# lastName = "江"

#查看关键字
# import keyword
#
# print(keyword.kwlist)

#判断标识符是否符合规范
#fromNo12,form#12,my_Bloolean,my-Boolean
#2ndobj,_name,_1name,test!,(haha),"name"

#连续赋值
# a = 1
# b = 2
# c = 3
# a,b,c = 1,2,3
# print(a,b,c)

#共享引用
# a = 3
# b = a
# print(a,b)

#变量练习
#苹果5.5元/斤，买了3斤，花了多少钱？
# price = 5.5
# weight = 3
# money = price * weight
# #将“=”右边的计算结果赋值给“=”左边的变量
# print("苹果",price,"元/斤，买了",weight,"斤，花了",money,"元钱？")