# 1.封装函数，可以判断一个数字是否为偶数
def is_oushu(num):
    """"""
    if num%2==0:
        return True
    else:
        return False


# print(is_oushu(5))
# 2.封装函数，可以实现1-n之间所有偶数的打印
def print_oushu(n):
    for i in range(2,n+1,2):
        print(i,end=' ')
# print_oushu(50)
# 3.封装函数，可以判断一个整数是否为质数
def is_zhishu(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True


# print(is_zhishu(1))
# 4.封装函数，查出传入列表奇数索引的元素并插入到新的列表中
lst = [1,2,3,4,5,6,7,8,9]
def func(lst):
    lst2 = []
    for i in range(1,len(lst),2):
        lst2.append(lst[i])
    return lst2
# lst2 = func(lst)
# print(lst2)


# 5.青蛙一次能跳一个或两个台阶，问：有n个台阶，青蛙跳上去有几种跳法？
"""
1   1  f(1)=1
2   2  f(2)=2
3   f(2)+f(1)=2+1=3
4   f(3)+f(2)=3+2=5
...
n  f(n-1)+f(n-2)
1 2 3 5 8 13...
"""
def jump(n):
    if n==1 or n==2:
        return n
    return jump(n-1)+jump(n-2)

# print(jump(35))

def jump2(n):

    a,b = 1,2
    for i in range(n-1):
        a,b = b,a+b
    print(a)
# jump2(5)






# 6.学员选课系统函数式编程改造(将登录、注册，选课，修改密码等功能封装成函数)


"""
学生选课系统
时间：
版本：
作者：
"""
# 管理员 事先设置好管理员账号密码
# 管理员功能：
#     查看有哪些课程,Python，java，web，unity，UI
#     增加或删除课程内容，增加 软件测试课程，删除UI课程
# 用户
#     注册 ：用户名和密码注册，没有注册过用户的才可以注册成功
#     登录 ：用户名和密码登录，登录成功进入选课界面
#     修改登录密码：输入旧密码，再输入新密码
#     查看：查看已选的课程
#     选课程：进行选课，选完课记录下来，下次查看可以看到

#保存课程内容
course_lst = ["Python","java","web","unity","UI"]
#保存用户
user_dic = {"zhang":{"name":"zhang","pwd":"123","course":[]}}
Administrator = {"name":"1","pwd":"2"}

import random
#验证码
def yzm(f):
    def yzmm():
        checkcode = ''
        for i in range(4):
            current = random.randrange(0, 4)
            if current == i:
                tep = chr(random.randint(65, 71))
            else:
                tep = random.randint(0, 9)
            checkcode += str(tep)
        print(checkcode)
        s = checkcode
        N = input('请输入验证码')
        if s == N:
            print("验证码正确")
            f()
        else:
            print("验证码错误，请重新输入")
    return yzmm
#主菜单显示
def show_menu():
    print("欢迎学生选课主界面")
    print("~*" * 15)
    print("        1.用户注册           ")
    print("        2.用户登录           ")
    print("        3.管理员登录           ")
    print("        4.退出系统           ")
    print("~*" * 15)
#注册
def register():
    print("欢迎来到注册界面！")
    name = input("请输入注册用户名：")
    pwd = input("请输入注册密码：")
    # 判断用户名是否已存在，已存在则不允许注册
    if name not in user_dic:  # 用户名不存在
        user_dic[name] = {"name": name, "pwd": pwd, "course": []}
        input("注册成功，按任意键继续。。。")
    else:  # 用户名已存在
        input("用户名已存在，按任意键继续。。。")
#展示学生登录菜单
def show_stu_login():
    print("欢迎来到选课界面！")
    print("        1.查看选课          ")
    print("        2.进入选课           ")
    print("        3.修改密码           ")
    print("        4.返回上一级           ")
#查看已有的选课
def stu_check_course(name):
    if user_dic[name]["course"]:
        print("已选的课程：", user_dic[name]["course"])
        input("按任意键继续。。。")
    else:
        input("没有选中任何课程，按任意键继续。。。")
#修改密码
def alter_pwd(name):
    pwd_error = 0
    while True:
        print("欢迎进入修改密码界面！")
        old_pwd = input("请输入旧密码：")
        # 判断旧密码是否正确
        if old_pwd == user_dic[name]["pwd"]:
            pwd = input("请输入新密码：")
            pwd2 = input("请确认新密码：")
            if pwd == pwd2:
                user_dic[name]["pwd"] = pwd
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
#登录
def login():
    flag = 0
    print("欢迎来到登录界面！")
    name = input("请输入登录用户名：")
    pwd = input("请输入登录密码：")
    if name in user_dic:  # 说明登录名在保存的user_dic中
        # 用户名和密码匹配
        if name == user_dic[name]["name"] and pwd == user_dic[name]["pwd"]:
            print("登录成功")
            flag = 1
        else:
            print("密码错误")
    else:
        print("用户名不存在")
    # 登录成功，走下面的代码
    if flag:
        while True:
            show_stu_login()
            choose = input("请输入功能选项：")
            # 查看已有的选课
            if choose == "1":
                stu_check_course(name)
            # 进入选课
            elif choose == "2":
                into_select_course(name)
            #修改密码
            elif choose == "3":
                alter_pwd(name)
            elif choose == "4":
                break
            else:
                input("输入有误，请重新输入,按任意键继续。。。")
#管理员菜单
def show_admin_menu():
    print("1.查看课程")
    print("2.增加课程")
    print("3.删除课程")
    print("4.返回上一级")
#管理员查看课程
def admin_check_course():
    print("欢迎来到查看课程界面")
    print("目前有以下课程")
    for i in range(len(course_lst)):
        print("{} : {}".format(i + 1, course_lst[i]))
    input("按任意键继续。。。。")
#管理员
def admin():
    flag = 0
    print("欢迎来到管理员界面")
    name = input("请输入管理员用户名：")
    pwd = input("请输入管理员密码：")
    if name == Administrator['name']and pwd == Administrator['pwd']:
        print("登录成功")
        flag = 1
    if flag:
        while True:
            show_admin_menu()
            choose = input("请输入功能选项：")
            if choose == "1":
                admin_check_course()
            elif choose == "2":
                admin_add_course()
            elif choose == "3":
                admin_delete_course()
            elif choose == "4":
                break
#退出
def exit_func():
    print("已退出！")
    exit(1)

def warm_tip():
    input("输入有误，请重新输入,按任意键继续。。。")

def show_login():
    while True:
        show_menu()
        choose = input("请输入功能选项：")
        if choose=="1":
           register() #注册
        elif choose=="2":
            login() #登录
        elif choose=="3":
            admin() #管理员
        elif choose=="4":
            exit_func()
        else:
            warm_tip()
show_login()

#进入选课
@yzm
def into_select_course():
    print("请选择课程：")
    for i, j in enumerate(course_lst, 1):
        print("%s:%s" % (i, j))
    choose = int(input("请输入课程编号："))
    # 用户输入编号在范围内
    if 1 <= choose <= len(course_lst):
        # 取出课程
        course = course_lst[choose - 1]
        # 如果已经选过此课程
        if course in user_dic[name]["course"]:
            print("已选过此课程")
            input("按任意键继续。。。")
        else:
            user_dic[name]["course"].append(course)
            print("选课成功，您选择的课程是:%s" % course)
            input("按任意键继续。。。")
    else:
        print("编号不在范围内。。。")
        input("按任意键继续。。。")
into_select_course()

#管理员删除课程
@yzm
def admin_delete_course():
    print("欢迎来到删除课程界面")
    print({i + 1: course_lst[i] for i in range(len(course_lst))})
    num = int(input("请输入要删除的课程编号："))
    if 1 <= num <= len(course_lst):
        ret = course_lst.pop(num - 1)
        input("删除%s成功，按任意键继续" % ret)
    else:
        print("输入编号有误，无法删除，按任意键继续。。。")

#管理员增加课程
@yzm
def admin_add_course():
    print("欢迎来到增加课程界面")
    course_name = input("请输入要增加的课程名称：")
    if course_name in course_lst:
        input("课程已存在，请勿重复添加")
    else:
        course_lst.append(course_name)
        input("课程添加成功，按任意键继续")


