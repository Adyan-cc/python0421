# 注意：先完成课堂讲解案例，再尽量完成下列练习
#
# 1.输入一个考试分数，判断考试结果是否为通过，如果分数>= 60,通过，
# 否则，结果为不通过(使用双分支和三元条件表达式各做一遍)
# score = int(input("请输入一个分数："))
# # if score>=60:
# #     print("通过")
# # else:
# #     print("不通过")
# ret = "通过" if score>=60 else "不通过"
# print(ret)
# 2.求1-100之间所有偶数的和
# num = 1
# sum_num = 0
# while num<=100:
#     if num%2==0:
#         sum_num+=num
#     num+=1
# print(sum_num)

# num = 2
# sum_num = 0
# while num<=100:
#     sum_num+=num
#     num+=2
# print(sum_num)
# 3.计算100到200范围内能被7或者9整除但不能同时被这两者整除的数的个数。
# num = 100
# count = 0
# while num<=200:
#     if (num%7==0 or num%9==0) and num%63!=0:
#         # print(num,end=' ')
#         count+=1
#     num+=1
# print(count)
# 4.50到70之间偶数的平均值
# num = 50
# count = 0
# sum_num = 0
# while num<=70:
#     sum_num+=num
#     count+=1
#     num+=2
# print(sum_num/count)
# 5.输出100-200范围内的所有质数
# num = 100
# while num<=200:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         print(num,end=' ')
#     num+=1

# 6.2019年  中国GDP：15.54万亿美元  美国GDP：21.41万亿美元
# 假设未来一段时间中国GDP增长率6.1%，美国增长率2%，问在哪一年中国GDP超越美国？
#100
#第二天增长10%
#第二天的营业额：100*0.1+100   100*（1+0.1）
#中国GDP增长：15.54*(1+0.061)
#美国GDP增长：21.41*(1+0.02)
# China_gdp = 15.54
# America_gdp = 21.41
# year = 2019
# while China_gdp<America_gdp:
#     China_gdp*=(1+0.061)
#     America_gdp*=(1+0.02)
#     year+=1
# print(year)
# 7.一个球从100米高度自由落下，每次落地后弹回原来高度的一半，
# 求它在第10次落地前，离地多高，第10次落地时共经过多少米？
#   1     2     3    4
#h 100    50   25    12.5
#s 100   200   250   275

# h = 100
# s = 100
# count = 1 #第一次落地
# while count<100:
#     h /=2
#     s = s+h*2
#     count+=1
# print(h,s)




# 8.输入一个整数，分解质因数，如输入8，输出 2 2 2
# 	输入30 ，输出2 3 5
# n = 8
#将n除以2，如果可以整除,n = n/2,即8/2=4,    将4除以2，如果可以整除,n = n/2，即4/2=2.。。
#将30除以2，如果可以整除,n = n/2,即30/2=15,   将15除以2，不能整除，则除数自增变为2+1=3，将15除以3.。。
n = 6
i = 2
while n>1:
    if n%i==0:
        n/=i
        print(i,end=' ')
    else:
        i+=1

# 9.完善昨天最后一题，购物商城项目菜单跳转、商城项目内测用户登录
# 完善游戏的页面跳转和上下级菜单切换

