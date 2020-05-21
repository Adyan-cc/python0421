"""
用户注册+用户登录简易版
    原有的简易版用户登录
    增加一个功能：用户注册
"""
import os

# 系统中存在两个用户
users = [
    ["admin", "123456"],  # 第一个用户
    ["wenwenc9", "111111"]    # 第二个用户
]

while True:
    # 登录菜单
    os.system("cls")
    print("■"*20)
    print("     1、用户登录")
    print("     2、用户注册")
    print("     3、退出系统")
    print("■"*20)

    #用户输入选项
    c = input("请输入您的选项：")
    if c == "1":
        # 用户登录:直接使用demo06中的登录代码
        # 复制粘贴代码时，一定要注意缩进的问题~自己找不出错误：老师
        while True:
            #  用户登录
            os.system("cls")
            print("用户登录")
            username = input("请输入账号：")
            password = input("请输入密码：")

            # 将用户输入的数据组装成列表
            u = [username, password]

            # 使用成员运算符进行了判断
            if u in users:
                input("登录成功，按任意键进入首页")
                print("中公直播大厅-首页界面")
                input("首页功能正在升级中，按任意键返回登录界面...")
                break
            else:
                input("登录失败，按任意键重新登录")

            break
        #####################################
    elif c == "2":
        # 简易版用户注册
        # 提示用户输入账号，输入密码
        username = input("请输入注册账号：")
        password = input("请输入注册密码：")
        # 将用户输入的数据，组装成一个列表
        user = [username, password]
        # 将用户数据，添加到系统用户中：末尾追加一个新用户
        users.append(user)
        input("注册成功，按任意键返回登录菜单")

    elif c == "3":
        input("系统将退出，保存好个人数据，按任意键结束")
        exit(1)
    else:
        input("没有这个选项，按任意键继续.")


