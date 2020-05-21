import os
import sys
import time

import random

# 定义一个列表，保存一个用户
u1 = ["admin", "123456", "昵称1"]
u2 = ["user1", "123", "昵称2"]
u3 = ["manager", "123456", "管理员"]
# 定义一个列表  保存所有用户
user = [u1, u2, u3]
# 展示界面

while True:
    os.system("cls")
    print("                欢迎进入PY1808电子商城                  ")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("                    1.用户登录                          ")
    print("                    2.新用户注册                        ")
    print("                    3.退出登录                          ")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # 提示用户输入选项
    login_c = input("<首页>\n请输入您的选项:")
    if login_c == "1":
        # 登陆
        while True:
            # 用户输入密码
            user_ID = input("请输入您的账号:")
            user_Password = input("请输入您的密码:")
            for users in user:
                if user_ID == users[0] and user_Password == users[1]:
                    print("账号密码输入正确，登录成功！")
                    input("按任意键进入商城首页>>>>")
                    time.sleep(1)
                    break
            else:
                input("账号或密码错误！！按任意键进入继续.")
                continue
            break
        while True:
            os.system("cls")
            print("尊敬的用户:", users[2])
            print("                      欢迎进入PY1808电子商城                     ")
            print("*****************************************************************")
            print("                         1.购物:进入超市                         ")
            print("                         2.休闲:游戏天地                         ")
            print("                         3.饮食:美食商城                         ")
            print("                         4.返回登录主界面                        ")
            print("                         5.退出电子商城系统                      ")
            print("*****************************************************************")
            # 首页提示用户输入选项
            index_c = input("<登陆首页>请输入您的选项:")
            if index_c == "1":
                # 进入超市首页
                while True:
                        os.system("cls")
                        print("                      欢迎进入PY1808商城超市                     ".center(68))
                        print("*****************************************************************".center(68))
                        print("                    1.干果类                    ".center(68))
                        print("                    2.酒水类                    ".center(68))
                        print("                    3.蔬菜类                    ".center(68))
                        print("                    4.退出系统                    ".center(68))
                        print("*****************************************************************".center(68))
                        choice4 = input("请输入您的选项:")
                        if choice4 == "1":
                            print("功能完善ing...按任意键继续>>>")
                            continue
                        elif choice4 == "2":
                            print("功能完善ing...按任意键继续>>>")
                            continue
                        elif choice4 == "3":
                            print("功能完善ing...按任意键继续>>>")
                            continue
                        elif choice4 == "4":
                            print("功能完善ing...按任意键继续>>>")
                            break
                        else:
                            print("您的输入有误!!!按任意键继续>>>")
                        # 商品信息
                        # 定义一个商品列表
                        goods1 = ["商品编号:01", "商品名称:百威啤酒", "价格:10元", "制造商:百威英博啤酒公司", "保质期:2年"]
                        goods2 = ["商品编号:02", "商品名称:可乐", "价格:2.5元", "制造商:百事可乐", "保质期:2年"]
                        goods3 = ["商品编号:03", "商品名称:牛奶", "价格:5元", "制造商:蒙牛集团", "保质期:45天"]
                        goods4 = ["商品编号:04", "商品名称:联想拯救者Y7000", "价格:8900元", "制造商:联想集团", "保修期:2年"]
                        goods5 = ["商品编号:05", "商品名称:华为荣耀20", "价格:6999元", "制造商:华为集团", "保修期:2年"]
                        goods = [goods1, goods2, goods3, goods4, goods5]
                        price = [10,2.5,5,8900,6999]
                        x = int(input("请输入商品编号:"))
                        print(goods[x])
                        if x == "0":
                            print(goods1)
                        elif x == "1":
                            print(goods2)

                        elif x == "2":
                            print(goods3)

                        elif x == "3":
                            print(goods4)
                        elif x == "4":
                            print(goods5)
                        # 是否选择购买？
                        y = int(input("请输入价格编号:"))
                        print("请付款购买:")
                        # 提示用户输入相应金额进入购买
                        pay = float(input("请输入金额:"))
                        print(price[y])
                        # print(type(price1))
                        price1 = [y]
                        if pay >= float(price1):
                            print("#付款完成，购买成功#")
                            zhao_ling = int(pay) - int(price1)
                            # 打印小票信息
                            print("######小票信息######")
                            print(goods[x])
                            print("实际付款金额", pay)
                            print("找零", zhao_ling)
                            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
                            print('\n', nowTime)
                        elif pay < float(price):
                            print("#付款失败，请重新付款#")

                            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
                            print('\n', nowTime)
            elif index_c == "2":
                while True:
                    os.system("cls")
                    print("                      欢迎进入PY1808游戏商城                     ")
                    print("*****************************************************************")
                    print("                           1.老虎棒子鸡                           ")
                    print("                           2.石头剪刀布                           ")
                    print("                           3.退出游戏商城                          ")
                    print("*****************************************************************")
                    # 提示用户输入选项
                    choose = input("请输入您的选项:")
                    if choose == "1":
                        print("# 老虎棒子鸡")
                        print("# 尊敬的用户，欢迎进入游戏环节")
                        print("# 游戏中，主要是人机大战")
                        print("# 系统会自动出招")
                        print("# 玩家根据提示，输入自己的出招[0 老虎   1 棒子  2 鸡  3 虫]")
                        print("# 系统经过计算，会展示游戏结果！根据结果给予奖励！")
                        # 玩家出招

                        while True:
                            player1 = int(input("请输入您的招数(0老虎 1棒子 2鸡 3虫子):"))
                            if player1 > 3 or player1 < 0:
                                input("您的输入有误，请按任意键重新输入>>>>")
                                continue
                            else:
                                player1 = int(player1)
                                # 电脑出招
                                print("系统正在出招中...3")
                                time.sleep(1)
                                print("系统正在出招中...2")
                                time.sleep(1)
                                print("系统正在出招中...1")
                                time.sleep(1)
                                print("系统已经出招[请根据提示继续操作]")
                                computer1 = random.randint(0, 3)
                                # 判断输赢
                                print("系统正在卖力的处理中，请稍等....")
                                time.sleep(2)
                                if (player1 == 0 and computer1 == 2) \
                                        or (player1 == 1 and computer1 == 0) \
                                        or (player1 == 2 and computer1 == 3) \
                                        or (player1 == 3 and computer1 == 1) \
                                        or (player1 == 0 and computer1 == 3):
                                    print("Congratulations, 玩家获胜..")
                                elif (player1 == 0 and computer1 == 1) \
                                        or (player1 == 1 and computer1 == 3) \
                                        or (player1 == 2 and computer1 == 0) \
                                        or (player1 == 3 and computer1 == 2):
                                    print("SORRY，你输了，扣除1积分。")
                                else:
                                    print("平局，不会扣除积分。")
                                # while True:
                                choice1 = input("游戏结束,是否继续？Y/N")
                                if choice1 == "N":
                                    break
                                else:
                                    continue
                    elif choose == "2":
                        zhao_shu = ["石头", "剪刀", "布"]
                        while True:
                            computer2 = random.choice(zhao_shu)
                            player2 = input("请输入您的招数(石头/剪刀/布):")
                            if player2 not in zhao_shu:
                                input("您输入的招数有误，请重新操作！！")
                                continue
                            else:
                                if (player2 == "石头" and computer2 == "剪刀") \
                                        or (player2 == "剪刀" and computer2 == "布") \
                                        or (player2 == "布" and computer2 == "石头"):
                                    print("玩家获胜")
                                elif computer2 == player2:
                                    print("平局")
                                else:
                                    print("电脑获胜")
                                print("游戏信息:玩家出招[%s] 电脑出招[%s]" % (player2, computer2))
                                choice2 = input("游戏结束,是否继续？Y/N")
                                if choice2 == "N":
                                    break
                                else:
                                    continue
                    elif choose == "3":
                        input("请按任意键返回登录界面....")
                        break
                    else:
                        input("您的输入有误，请按任意键继续>>>>")
                        continue
            elif index_c == "3":
                while True:
                    os.system("cls")
                    print("                      欢迎进入PY1808饮食商城                     ")
                    print("*****************************************************************")
                    print("                           1.东方饮食                           ")
                    print("                           2.西方饮食                           ")
                    print("                           3.退出饮食商城                          ")
                    print("*****************************************************************")
                    # 提示用户输入选项
                    choice3 = input("请输入您的选项:")
                    if choice3 == "1":
                        input("功能完善ing....按任意键继续")
                        continue
                    elif choice3 == "2":
                        input("功能完善ing....按任意键继续")
                        continue
                    elif choice3 == "3":
                        input("按任意键退出饮食商城>>>>>")
                        break
                    else:
                        input("您的输入有误!!!按任意键继续")
                        continue
            elif index_c == "4":
                input("请按任意键返回登录界面....")
                break
            elif index_c == "5":
                input("即将退出电子商城系统...按任意键继续")
                sys.exit(1)
            else:
                input("您的输入有误，请按任意键返回登录界面....")
                continue
    elif login_c == "2":
        # 新用户注册
        while True:
            user_ID = input("请输入你要注册的账号：")
            user_Password = input("请输入注册账号的密码：")
            user_nicheng = input("请创建此账号的昵称:")
            if len(user_ID) > 0 and len(user_Password) > 0 and len(user_nicheng) > 0:
                users = [user_ID, user_Password, user_nicheng]
                user.append(users)
                input("注册成功！按任意键进入登录首页")
                break
            else:
                input("注册失败！按任意键继续.")
                continue
    elif login_c == "3":
        input("谢谢惠顾")
        sys.exit(1)
    else:
        input("您的输入有误，请按任意键继续....")

