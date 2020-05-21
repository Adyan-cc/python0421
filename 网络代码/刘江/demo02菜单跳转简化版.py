"""
菜单跳转简化版
"""

while True:
    # 登录页面
    print("我在登录页面(1进入首页/2注册/3退出)")
    n1 = input("请输入选项")
    if n1 == "1":

        while True:
            # 首页界面
            print("我在首页界面(1返回登录/2退出)")
            n2 = input("请输入选项:")
            if n2 == "1":
                print("返回登录界面")
                break
            elif n2 == "2":
                exit(1)
    elif n1 == "2":
        print("注册")
    elif n1 == "3":
        exit(1)