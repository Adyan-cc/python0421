"""
多用户登录，简易版
    单独一个用户怎么表示？包含账号+密码
    用户 = [账号, 密码]
    user1 = ["admin", "123456"]
    user2 = ["wenwen", "111111"]

    多个用户怎么表示？
    users = [user1, user2]  1
    等价
    users = [ ["admin", "123456"], ["wenwen", "111111"] ]

    简易版登录怎么实现？ 懂 5  看不懂 1
        用户输入了：admin, 123456
          把输入的数据组装成列表 登录的用户 ["admin", "123456"]
          通过成员运算符直接判断 登录的用户 in users
            [True登录成功/False登录失败]
"""
import os

# 系统中存在两个用户
users = [
    ["admin", "123456"],  # 第一个用户
    ["wenwne", "111111"]    # 第二个用户
]

while True:
    #  用户登录
    os.system("cls")
    print("    ~用户登录")
    username = input("请输入账号：")
    password = input("请输入密码：")

    # 将用户输入的数据组装成列表
    u = [username, password]

    # 使用成员运算符进行了判断
    if u in users:
        input("登录成功，按任意键进入首页")
        print(" 直播大厅-首页界面")
        input("首页功能正在升级中，按任意键继续...")
    else:
        input("登录失败，按任意键重新登录")
