# 算数运算符：+，-，*，/，//，%，**
# int*int=int,   int/int=float,  int*float = float
# 优先级：幂最高，先乘除，再加减，有()先算括号里面的
# print(18//7) #取的是商 2
# print(18%7)  #取余数 4


# 判断一个数12是否是偶数
# print(12%2) #余数是0说明是偶数

# print(2**3)
# print(16**0.5)

# 输入一个三位数整数，逆序输出 368-->863
# 368 = 3*100+6*10+8*1
# num = 368
# num = int(input("请输入一个三位数："))
# gws = num%10  #取出个位数 8
# sws = num//10%10 #取出十位数 6
# bws = num//100 #取出百位数 3
# new_num = gws*100+sws*10+bws*1
# print("逆序后的结果是-->",new_num)

# 赋值运算符：=，把“=”右边的结果赋值给左边的变量
# a = 5
# b = 8
# 如何将a,b的值交换
# 把a的值赋值给c
# 把b的值赋值给a
# 把c的值赋值给b
# c = a
# a = b
# b = c
# 直接交换
# a,b = b,a
# print(a,b)

# 复合赋值运算符 +=，-=，*=，/=，//=，%=，**=
# num1 = 5
# num2 = 3
#
# num1 += num2 # num1 = num1+num2
# print(num1)

# 逻辑运算符：and，or，not
#优先级：not>and>or
# x = True
# y = False
# print(x and y) #False
#所有的为真才是真，返回最后一个真
#只要有一个假就是假，返回第一个假
# a = 5
# b = 3
# c = 0
# d = False
# print(a and b)
# print(a and c and b)
# print(a and b and c and d)

# or有一个为真就是真,返回第一个真
#所有的是假才为假，返回最后一个假
# x = True
# y = False
# print(x or y)
# a = 5
# b = 3
# c = 0
# d = False
# # print(a or b or c or d)
# # print(c or d)
# # print(a and b and c or d) #False
# print(a and b or c or d) #3

# not取反
# x = False
# # print(not x)
# a = 5
# print(not a) #False
# print(not 0) #True

# a = 1
# b = 2
# c = 3
# d = 0
# print(a or b or c or d) #1
# print(a and b and c or d) #3
# print(a and not b or c and not d) #True
# print(a and not b and c and not d) #False  a and False and c and True


# 比较运算符：>,<,>=,<=,==,!=
#条件为真返回True，条件为假返回False
a = 1
b = 3
c = 3
d = 4
# print(a<b) #True
# print(b<c) #False
# print(b>c) #False
# print(b<=c) #True
# print(b==c) #True
# print(a!=b) #True
#连续比较
print(a<b<=c)#True
print(a<d>c) #True  a<d and d>c
print(1==2<3)#False 1==2 and 2<3