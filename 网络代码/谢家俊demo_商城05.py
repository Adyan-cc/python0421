"""

商城项目综合开发，将数据，如注册用户信息等存储到列表或字典中
变化：用字典保存了user注册用户信息
作者：谢家俊
时间：2020/4/26
版本：v 1.5
"""

# 用户账号密码存储库
user = {"xie": {"账号": "xie", "密码": "123"}}
# 商城物品，【商品名称，单价】
goods = [["华为mate40", 4999], ["小米11", 3999], ["iphone12", 8999]]

while True:
    """商城登陆界面"""
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("        1.用户登陆           ")
    print("        2.用户注册           ")
    print("        3.退出系统           ")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    # 用户输入选项
    choose = input("请输入选项")

    if choose == "1":
        """用户登陆"""
        account = input("请输入账号:")
        password = input("请输入密码:")
        # 判断用户登陆的情况
        if user.get(account) == {"账号": account, "密码": password}:
            # 用get（）函数获取value值，否则如果key键不存在程序会报错
            print("登陆成功，进入首页")

            """首页界面"""
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
            print("        1.进入购物商城          ")
            print("        2.返回登陆界面          ")
            print("        3.修改密码         ")
            print("        4.退出系统          ")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
            # 用户输入选项
            choose_2 = input("请输入选项:")
            if choose_2 == "1":
                goods_num = 0  # 商品编号
                for i in goods:
                    goods_num += 1
                    print("编号", goods_num, i)

                """用户购买商品"""
                choose_num = int(input("请输入要购买的商品编号"))
                buy_sum = int(input("请输入要购买的数量"))
                # 应付金额
                money = goods[choose_num-1][1]*buy_sum
                print("应付金额时", money, "元")
                pay = int(input("请付款"))
                print("购买商品成功", goods[choose_num-1][0], "数量", buy_sum, "找零",pay-money)
                exit(1)
            elif choose_2 == "2":
                input("按任意键返回登陆界面")
                continue
            elif choose_2 == "3":
                """修改密码"""
                password1 = input("请输入旧密码")
                if password1 == password:
                    psw_new = input("请输入新密码")
                    user[account]["密码"] = psw_new  # 修改密码
                    input("密码修改成功，按任意键返回登陆界面")
                else:
                    input("密码错误，按任意键返回登陆界面")
                    continue
            elif choose_2 == "4":
                print("系统退出")
                exit(1)
            else:
                print("输入错误，系统退出")
                exit(1)

        else:
            input("登陆失败，账号或密码错误，按任意键返回登陆界面")

    elif choose == "2":
        while True:
            print("~*~*~*~用户注册界面~*~*~*~*")
            account = input("请输入账号：")
            password = input("请输入密码")
            psw_2 = input("请再输入密码")

            """判断账号是否已经存在"""
            for key_user in user.keys():
                if account == key_user:
                    input("账号已存在，按任意键重新注册")
                    break
            else:
                if password == psw_2:  # 判断密码两次输入是否一致
                    user[account] = {"账号": account, "密码": password}
                    break
                else:
                    input("密码不一致，按任意键重新注册")
                    continue
        input("恭喜注册成功，按任意键返回登陆界面")

    elif choose == "3":
        print("系统退出")
        exit(1)