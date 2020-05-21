"""
学生信息录入系统
    开发步骤
    1、定义一个首页界面[告诉我们要做什么]
    2、定义变量~保存所有小伙伴
    3、通过用户输入的选项，执行判断
    4、实现各项的功能
    5、测试功能运行是否正确
    6、BUG完善
"""
import os

# 保存直播大厅所有伙伴的列表
students = list()

while True:
    # 首页
    os.system("cls")
    print("        直播大厅")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("          1、查看所有小伙伴")
    print("          2、录入个人信息")
    print("          3、查看个人信息")
    print("          4、退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")

    # 用户输入选项
    c = input("请输入您的选项:")
    if c == "1":
        # 遍历所有小伙伴
        for stu in students:
            print("小伙伴：", stu)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("查看完成按任意键返回首页.")
    
    elif c == "2":
        # 提示用户输入姓名
        while True:
            name = input("请输入昵称：")
            if name in students:
                input("该昵称已经存在，请使用其他昵称录入")
            else:
                # 保存昵称:列表的末尾追加
                students.append(name)
                input("录入完成，按任意键返回首页...")
                break

    elif c == "3":
        # 提示用户输入要查看的昵称
        nickname = input("请输入要查看的昵称：")
        # 成员成员运算符，判断昵称是否包含在列表中[True/False]
        if nickname in students:
            print("该成员已经在大厅中.")
        else:
            print("该昵称代表的成员没有在大厅中.")
        input("查看个人信息，正在升级中...")

    elif c == "4":
        input("退出系统，保存好个人数据，按任意键退出")
        exit(1)

