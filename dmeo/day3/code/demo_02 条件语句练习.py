

#1.两个人住酒店，有一个带了身份证就可以入住，否则不可以
# is_id_card1 = True
# is_id_card2 = False
# if is_id_card1 or is_id_card2:
#     print("可以入住")
# else:
#     print("不可以入住")
#2.判断一个年份是否是闰年
#能被4整除但是不能被100整除：普通闰年
#能被400整除：世纪闰年
#其他：平年
# year = int(input("请输入一个年份："))
# if year%4==0 and year%100!=0:
#     print("普通闰年")
# elif year%400==0:
#     print("世纪闰年")
# else:
#     print("平年")

#3.猜拳游戏
#人和电脑猜拳，判断输赢
#人出拳使用0,1,2代替石头，剪刀，布
#电脑出拳：随机0,1,2
# print("~~~~~~~~~~~~~~~~~~~~~~~~")
# print("~~~欢迎来到猜拳游戏~~~")
# print("~~~您将和电脑猜拳，游戏十分公正，请放心~~~")
# print("~~~~~~~~~~~~~~~~~~~~~~~~")
# import random
# import time
# #人出拳
# person = input("请你出拳：（0/石头，1/剪刀，2/布）")
# #电脑随机出拳
# computer = random.randint(0,2)
# print("电脑出拳是：",computer)
# #进行判断
# if person=="1" or person=="2" or person=="0":
#     print("正在判断输赢。。。。")
#     time.sleep(3)
#     if person=="0" and computer==1 or person=="1" and computer==2 or person=="2" and computer==0:
#         if person=="0":
#             print("你出拳是：石头，电脑出拳：剪刀，恭喜你赢啦！")
#         elif person=="1":
#             print("你出拳是：剪刀，电脑出拳：布，恭喜你赢啦！")
#         else:
#             print("你出拳是：布，电脑出拳：石头，恭喜你赢啦！")
#     elif person==str(computer):
#         print("平局啦！")
#     else:
#         print("不好意思，你弱爆了！")
# else:
#     print("出拳错误，终止游戏！")

#4.个税计算器
#纳税起征点:5000元,扣完五险一金不足5000不需要纳税
#五险一金:社保10.5%,公积金12%
total_money = float(input("请输入工资总额："))
wxyj = total_money*0.225
should_money = total_money-wxyj-5000 #应纳税所得额
if should_money<=0:
    print("工资太少，没资格纳税！")
    nashui = 0
else:
    if 0<should_money<1500:
        nashui = should_money*0.03
    elif 1500<should_money<=4500:
        # nashui = (should_money-1500)*0.1+1500*0.03
        nashui = should_money*0.1-105
    elif 4500<should_money<=9000:
        nashui = should_money*0.2-555
    else:
        nashui = should_money*0.25-1005
result_money = total_money-wxyj-nashui
print("税前工资是",total_money,"到手工资是",result_money)