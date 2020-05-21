"""
  时间：2020-04-23  21:00
  制作者：刘江
  版本:练习
  """

# #   1.输入一个考试分数，判断考试结果是否为通过，如果分数>= 60,通过，否则，结果为不通过(使用双分支和三元条件表达式各做一遍)
# score = float(input("输入分数"))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")
#
# score = float(input("输入分数"))
# print("及格") if score >= 60 else print("不及格")
#
# # 2.求1-100之间所有偶数的和
# x = 1
# sum_x = 0
# while x <= 100:
#     if x % 2 == 0:
#         sum_x += x
#     x += 1
# print(sum_x)
#
# # 3.计算100到200范围内能被7或者9整除但不能同时被这两者整除的数的个数。
# num = 100
# sum_num = 0
# while num <= 200:
#     if num % 7 == 0 and num % 9 == 0:
#         num += 1
#         continue
#     elif num % 7 == 0 or num %9 == 0:
#         num += 1
#         sum_num += 1
#         continue
#     else:
#         num += 1
# print(sum_num)
#
#
# # 4.50到70之间偶数的平均值
# #
# x = 50
# sum_x = 0  # 偶数的和
# num = 0  # 偶数的个数
# while x <= 70:
#     if x % 2 == 0:
#         sum_x += x
#         num += 1
#     x += 1
# print(sum_x/num)
# # 5.输出100-200范围内的所有质数
# #复杂
# x = 100
# num = 2  # 用作整除的循环
# while x <= 200:
#
#     while num <= x :
#         if x % num == 0 and x != num:
#             x += 1
#             num = 2
#             break
#         elif x % num != 0:
#             num += 1
#             continue
#         else:
#             num = 2
#             print(x)
#             x += 1
#             break
#
# # #
# # 6.2019年  中国GDP：15.54万亿美元  美国GDP：21.41万亿美元
# # 假设未来一段时间中国GDP增长率6.1%，美国增长率2%，问在哪一年中国GDP超越美国？
# #
#
#
# #
# # 7.一个球从100米高度自由落下，每次落地后弹回原来高度的一半，
# # 求它在第10次落地前，离地多高，第10次落地时共经过多少米？
# #
# #
# "不会"
# # 8.输入一个整数，分解质因数，如输入8，输出 2 2 2
# # 	输入30 ，输出2 3 5
#
# n=8
# #将n除以2，如果可以整除，n=n/2,即8/2  ..循环此句中
#
# num = int(input("请输入一个整数:"))
# # 定义除数变量
# x = 2
# if num == 1 or num == 0:
#     print(num)
# while x <= num:
#     if num % x == 0:
#         print(x)  # 打印出质因数
#         num = num/x
#     else:
#         x += 1
# # 9.完善昨天最后一题，购物商城项目菜单跳转、商城项目内测用户登录
# # 完善游戏的页面跳转和上下级菜单切换

print("=======================")
import random
username = 1111
password = 1112
while True:
    # 用户登录
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username=="1111" or password=="1112":
        print("登录成功")
        break
    else:
        print("密码或账户错误，\n请重新登录。。。")

print("=======================")
print("   购物商城     ")
print("  3601:衣服")
print("  3602:裤子")
# 提示用户输入选项 choice~选择
choice = input("  请输入编号\n（3601、3602）：")
print("=======================")
if choice =="3601":
    name = "衣服"
    numb = "3601"
    quantity = 9999
    price = 88
    # 1.运行脚本展示一个商品的信息
    print("商品名称：" +name)# 3. 提示购买的商品名称
    print("商品编号：" +numb)# 2.提示用户要购买的商品编号
    print("现有库存：", quantity, "件")#quantity数量
    print("商品单价：", price, "元/件")#price单价
elif choice =="3602":
    name = "裤子"
    numb = "3602"
    quantity = 9999
    price = 80
    # 1.运行脚本展示一个商品的信息
    print("商品名称：" +name)# 3. 提示购买的商品名称
    print("商品编号：" +numb)# 2.提示用户要购买的商品编号
    print("现有库存：", quantity, "件")#quantity数量
    print("商品单价：", price, "元/件")#price单价
else:
    print()
buy_quantity = int(input("请输入您购买的件数："))# 4.提示用户购买的数量
allGoods_money = buy_quantity * price#allGoods所有货物金额=buy_quantit * yprice购买数量*价格
print("您总共买了%s件商品，\n需要付款%d元" % (buy_quantity, allGoods_money))# 5.显示用户购买的商品信息，如商品名，购买数量，商品单价，付款金额
buy_money = int(input("请您付款："))# 6.提示付款
while buy_money < allGoods_money:#while循环结构
    buy_money = int(input("你的余额不足，\n请重新付款："))
print("========================")
print("谢谢您的光临！")# 7.付款后给出订单信息
print("您的账单：")
print("商品名称：" + name)
print("商品编号：" + numb)
print("购买数量：", buy_quantity, "只")
print("商品单价：", price, "元/件")
print("总共消费：", allGoods_money, "元")
print("找余：", buy_money - allGoods_money, "元")
print("========================")
