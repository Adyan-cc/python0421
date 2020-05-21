"""
案例操作：多用户登录

    单个用户？账号+密码+昵称
        用户 = [账号, 密码, 昵称]
        user1 = ["admin", "123", "管理员"]
        user2 = ["wenwenc9", "111", "稳稳c9"]

    多个用户？
        users = [user1, user2]
        等价于
        users = [ ["admin", "123", "管理员"], ["wenwenc9", "111", "稳稳c9"]]
 
    用户登录：
        用户输入：账号 + 密码
        此时，~不能使用成员运算符了！【问题的重点】
            ["admin", "123"] in users   False[缺少昵称]
        这时候，我们就必须得遍历整个列表users~判断账号+密码是否正确
"""
import os

# 系统中的所有用户
users = [ 
    ["admin", "123", "管理员"],
    ["wenwenc9", "111", "wenwne"]
]

# 定义变量~判断用户登录成功(True)或者失败(False)
# 程序刚开始运行的时候，没有用户登录，所以默认False
ok = False
# 登录后的昵称: 没有用户登录的时候~ 没有昵称
n = ""

while True:
    # 多用户登录
    username = input("请输入账号：")
    password = input("请输入密码：")

    # 判断登录是否成功:遍历所有用户
    for u in users:
        # 第一次循环：u -> ["admin", "123", "大牧"]
        if username == u[0] and password == u[1]:
            input("登录成功，按任意键继续")
            ok = True # 登录成功
            n = u[2]     # 记录昵称
            break
    # [所有数据全部遍历完了]~没有发现正确的账号+密码，登录失败
    else:
        input("账号或者密码有误，请重新登录")
        ok = False

    # ok的目的：根据用户登录是否成功，判断要不要展示首页
    if ok == True:
        # 用户登录了，展示首页
        print("    欢迎进入游戏首页界面")
        print("尊敬的用户", n, "，欢迎进入xx游戏")
        input(" 首页功能正在升级中，按任意键继续")
