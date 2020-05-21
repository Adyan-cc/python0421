'''
学生选课系统
时间;2020-4-27
版本：1.0.0
作者：刘江
'''
# 开头文档写出 普通用户、课程的保存方式
#管理员 事先设置好管理员账号密码
#管理员功能：查看有哪些课程,Python，java，web，unity，UI
            #增加或删除课程内容，增加 软件测试课程，删除UI课程
# 用户
    # 注册 ：用户名和密码注册，没有注册过用户的才可以注册成功
    # 登录 ：用户名和密码登录，登录成功进入选课界面
    # 修改登录密码：输入旧密码，再输入新密码
    # 查看：查看已选的课程
    # 选课程：进行选课，选完课记录下来，下次查看可以看到

# 1.封装函数，可以判断一个数字是否为偶数
# def peven(n):
#     num = n
#     if (num % 2) == 0:
#         print("{0} 是偶数".format(num))
#     else:
#         print("{0} 是奇数".format(num))
# n=int(input('输入一个数：'))
# peven(n)

#
# 2.封装函数，可以实现1-n之间所有偶数的打印
# def fun1(n):
# 	for i in range(2,n+1,2)
# # 	print (i,end=' ')
# n=int(input('输入一个数：'))
# fun1(n)
#
# 3.封装函数，可以判断一个整数是否为质数

# def fun1(n):
#     for i in range(2, n):
#         if n%i ==0:
#             print(" %d是质数"%n)
#             return False
#     else:
#         print("%d不是质数"%n)
# n=int(input('输入一个数：'))
# fun1(n)
#
#
# 4.封装函数，查出传入列表奇数索引的元素并插入到新的列表中
#
# 5.青蛙一次能跳一个或两个台阶，问：有n个台阶，青蛙跳上去有几种跳法？
#
# 6.学员选课系统函数式编程改造(将登录、注册，选课，修改密码等功能封装成函数)

#课程储存
kechen_neimu = ["Python","java","web","unity","UI"]
# 学生账户储存
xuesheng_mima ={'Adyan':{'name':'Adyan','mimma':'123','kecheng':[]
}}
# 管理员账户
Administrator = {"administrators":"1","administratorsmi":"2"}
import time


#学生操作：
#学生注册
def zhu_ce():
    '学生注册账户'
    print("欢迎来到注册界面！")
    name = input("请输入注册用户名：")
    mimma = input("请输入注册密码：")
    # 判断用户名是否已存在，已存在则不允许注册
    if name not in xuesheng_mima:  # 用户名不存在
        xuesheng_mima[name] = {"name": name, "pwd": mimma, "course": []}
        input("注册成功，按任意键继续。。。")
    else:  # 用户名已存在
        input("用户名已存在，按任意键继续。。。")
# 学生登录
def den_lu():
    '学生登录'
    flag = 0
    print("欢迎来到登录界面！")
    name:str = input("请输入登录用户名：")
    pwd = input("请输入登录密码：")
    if name in xuesheng_mima:  # 说明登录名在保存的user_dic中
        # 用户名和密码匹配
        if name == xuesheng_mima[name]["name"] and pwd == xuesheng_mima[name]["pwd"]:
            print("登录成功")
            flag = 1
        else:
            print("密码错误")
    else:
        print("用户名不存在,正在返回。。。。。")
        time.sleep(2)
        return
    xueshenxuanke_jiemian(name)
# 学生选课
def xueshenxuanke_jiemian(name):
    while True:
        denlu_jiem()
        choose = input("请输入功能选项：")
        if choose == '1':
            ca_kan(name)#有问题
        elif choose == '2':
            xuan_ke(name)
        elif choose == '3':
            xiugai_mima(name)#有问题
        elif choose == '4':
            break
# 学生修改密码
def xiugai_mima(name):
    pwd_error = 0
    while True:
        print("欢迎进入修改密码界面！")
        old_pwd = input("请输入旧密码：")
        # 判断旧密码是否正确
        if old_pwd == xuesheng_mima[name]["pwd"]:
            pwd = input("请输入新密码：")
            pwd2 = input("请确认新密码：")
            if pwd == pwd2:
                xuesheng_mima[name]["pwd"] = pwd
                input("修改成功，按任意键继续。。")
                break
            else:
                input("两次密码不一致，请重新输入，按任意键继续。。")
        else:
            if pwd_error >= 3:
                input("输入错误次数过多，已退出，按任意键继续")
                break
            input("密码有误，请重新输入，按任意键继续。。")
            pwd_error += 1
# 学生查看课程
def ca_kan(name):
    if xuesheng_mima[name]["course"]:
        print("已选的课程：", xuesheng_mima[name]["course"])
        input("按任意键继续。。。")
    else:
        input("没有选中任何课程，按任意键继续。。。")
# 学生选课
def xuan_ke(name):
    print("欢迎来到增加课程界面")
    for i, j in enumerate(kechen_neimu):
        print("%s:%s" % (i+1, j))
    choose= int(input("请输入要增加的课程名称："))
    if 1 <= choose <= len(kechen_neimu):
        # 取出课程
        course = kechen_neimu[choose - 1]
        # 如果已经选过此课程
        if course in xuesheng_mima[name]["course"]:
            print("已选过此课程")
            input("按任意键继续。。。")
        else:
            xuesheng_mima[name]["course"].append(course)
            print("选课成功，您选择的课程是:%s" % course)
            input("按任意键继续。。。")
# 学生删除课程
def shancu_kecheng():
    print("欢迎来到删除课程界面")
    print({i + 1: kechen_neimu[i] for i in range(len(kechen_neimu))})
    num = int(input("请输入要删除的课程编号："))
    if 1 <= num <= len(kechen_neimu):
        ret = kechen_neimu.pop(num - 1)
        input("删除%s成功，按任意键继续" % ret)
    else:
        print("输入编号有误，无法删除，按任意键继续。。。")
#管理员操作:
# 管理员登录
def Den_lu():
    flag = 0
    print("欢迎来到管理员界面")
    name = input("请输入管理员用户名：")
    pwd = input("请输入管理员密码：")
    if name == Administrator[name] and pwd == Administrator[pwd]:
        print("登录成功")
        flag = 1
    else:
        print('输入错误，任意键请重新输入。。。')

    # 管理员修改
    while True:
        print("1.查看课程")
        print("2.增加课程")
        print("3.删除课程")
        print("4.返回上一级")
        choose = input("请输入功能选项：")
        if choose == '1':
            Ca_kan()
        elif choose == '2':
            zhen_jia()
        elif choose == '3':
            shan_chu()
        elif choose == '1':
            break
# 管理员查看
def Ca_kan():#C大写管理员查看
    print("欢迎来到查看课程界面")
    print("目前有以下课程")
    for i in range(len(kechen_neimu)):
        print("{} : {}".format(i + 1, kechen_neimu[i]))
# 管理员增加
def zhen_jia():
    print("欢迎来到增加课程界面")
    course_name = input("请输入要增加的课程名称：")
    if course_name in kechen_neimu:
        input("课程已存在，请勿重复添加")
    else:
        kechen_neimu.append(course_name)
        input("课程添加成功，按任意键继续")
# 管理员删除
def shan_chu():
    print("欢迎来到删除课程界面")
    print({i + 1: kechen_neimu[i] for i in range(len(kechen_neimu))})
    num = int(input("请输入要删除的课程编号："))
    if 1 <= num <= len(kechen_neimu):
        ret = kechen_neimu.pop(num - 1)
        input("删除%s成功，按任意键继续" % ret)
    else:
        print("输入编号有误，无法删除，按任意键继续。。。")

# 首页展示
def shou_ye():
    while True:
        print("欢迎学生选课主界面")
        print("~*" * 15)
        print("        1.用户注册           ")
        print("        2.用户登录           ")
        print("        3.管理员登录           ")
        print("        4.退出系统           ")
        print("~*" * 15)
        choose = input("请输入功能选项：")
        if choose=='1':
            zhu_ce()
        elif choose=='2':
            den_lu()
        elif choose=='3':
            Den_lu()
        elif choose=='4':
            break
#登录界面
def denlu_jiem():
    print("欢迎来到选课界面！")
    print("        1.查看选课          ")
    print("        2.进入选课           ")
    print("        3.修改密码           ")
    print("        4.返回上一级           ")

#调用系统首页
print(shou_ye())