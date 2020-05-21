

# - int(x)，将x转换为一个整数
#浮点数转换为整数，直接去掉小数点后面的数字
# num = 5.9
# num2 = int(num) #将num转换为int，赋值给num2
# print(num2)
# num3 = "5"
# num4 = int(num3)
# print(num4,type(num4))
#不是所有的字符串都可以转换为整型
# num5 = "a" #不可以转换
# num5 = "5.5" #不可以转换
# num6 = int(num5)
# print(num6)
# num7 = True
# num7 = False
# num8 = int(num7)
# print(num8)
# - float(x)，将x转换为一个小数
# num1 = 3
# num2 = float(num1)
# print(num2)
# num3 = "3.5"
# num3 = "3"
# num4 = float(num3)
# print(num4)


# - bool(x)，将x转换为一个布尔 True,False
# num1 = 5
# num1 = 0
# num2 = bool(num1) #非0或非空数据转换成布尔都是True
# print(num2)


# - str(x)，将x转换为一个字符串
# num1 = True
# print(type(num1))
# num2 = str(num1)
# print(num2,type(num2))

# - chr(x),将一个整数转换为一个字符
# print(chr(65),chr(97))
# - ord(x)，将一个字符转换为一个整数
# print(ord("A"))
# - eval(x)，将字符串中的有效 Python 表达式,并返回一个对象

# num = "3+5"
# print(num)
# print(eval(num))
#苹果5.5元/斤，买了3斤，花了多少钱？
# price = input("请输入苹果的单价（元/斤）：")
# # price = int(price)
# # price = float(price)
# price = eval(price)
# weight = input("请输入苹果的重量：")
# # weight = int(weight)
# # weight = float(weight)
# weight = eval(weight)
# money = price*weight
# print("苹果",price,"元/斤，买了",weight,"斤，花了",money,"元钱")

# a,b = 1,2
# num1 = eval(input("请输入一个数："))
# num2 = eval(input("请输入另一个数："))
# # print(num1+num2)
# print(num1,num2)

#制作一个简易的计算器
# print("~~~~~~~~~~~~~~~~~~~")
# print("这里是加法计算器，输入两个数字，可以计算和")
# print("~~~~~~~~~~~~~~~~~~~")
# num1 = input("请输入一个数字：")
# num2 = input("请输入第二个数字：")
# result = eval(num1)+eval(num2)
# print("计算的结果是：",result)