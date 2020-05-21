
#break
#输出1-10，当输出6的时候停止
#初始值
# num = 1
# #循环条件
# while num<=10:
#     print("输出一个数字：", num)
#     if num==6:
#         break
#     #改变初始值
#     num+=1

# continue
#刘德华的演唱会门票，10张票，售票处留两张(3,4)vip票,1号票售出即可下班
# ticket = 10
# while ticket>0:
#     if ticket==3 or ticket==4:
#         print("预留的vip门票，不收售卖")
#         ticket -= 1
#         continue
#     print("已售出门票：",ticket,"号票")
#     ticket-=1
# print("下班啦！")


# 猜拳游戏
#人和电脑猜拳，判断输赢
#人出拳使用0,1,2代替石头，剪刀，布
#电脑出拳：随机0,1,2
#平局重新开一局
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~欢迎来到猜拳游戏~~~")
print("~~~您将和电脑猜拳，游戏十分公正，请放心~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
import random
import time
error = 0
while True:
    #人出拳
    person = input("请你出拳：（0/石头，1/剪刀，2/布）")
    #电脑随机出拳
    computer = random.randint(0,2)
    print("电脑出拳是：",computer)
    #进行判断
    if person=="1" or person=="2" or person=="0":
        print("正在判断输赢。。。。")
        time.sleep(1)
        if person=="0" and computer==1 or person=="1" and computer==2 or person=="2" and computer==0:
            if person=="0":
                print("你出拳是：石头，电脑出拳：剪刀，恭喜你赢啦！")
            elif person=="1":
                print("你出拳是：剪刀，电脑出拳：布，恭喜你赢啦！")
            else:
                print("你出拳是：布，电脑出拳：石头，恭喜你赢啦！")
            break
        elif person==str(computer):
            print("平局啦,再来一局！")
        else:
            print("不好意思，你弱爆了！")
            break
    else:
        print("出拳错误，请重新出拳！")
        error+=1
        if error==3:
            print("错误次数超过三次，终止游戏！")
            break