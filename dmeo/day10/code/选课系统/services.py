
from data import *
from views import *
import random
#验证码
def verify_code(func):
    def inner(name):
        code = str(random.randint(1000,9999))
        # print(code)
        input_code = input("需要填写验证码%s\n************:"%code)
        if code==input_code:
            func(name)
        else:
            input("验证码输入有误，按任意键继续。。。")
    return inner

def register():
    print("欢迎来到注册界面！")
    name = input("请输入注册用户名：")
    pwd = input("请输入注册密码：")
    # 判断用户名是否已存在，已存在则不允许注册
    if name not in user_dic:  # 用户名不存在
        user_dic[name] = {"name": name, "pwd": pwd, "course": []}
        input("注册成功，按任意键继续。。。")
        return main()
    else:  # 用户名已存在
        input("用户名已存在，按任意键继续。。。")
        return main()


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
            input("密码错误,按任意键继续。。。")
            return main()
    else:
        input("用户名不存在,按任意键继续。。。")
        return main()
    # 登录成功，走下面的代码
    if flag:
        select_course(name)

def check_select_course(name):
    if user_dic[name]["course"]:
        print("已选的课程：", user_dic[name]["course"])
        input("按任意键继续。。。")
    else:
        input("没有选中任何课程，按任意键继续。。。")

@verify_code
def into_select_course(name):
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
@verify_code
def alter_pwd(name):
    pwd_error = 0
    print("欢迎进入修改密码界面！")
    old_pwd = input("请输入旧密码：")
    # 判断旧密码是否正确
    if old_pwd == user_dic[name]["pwd"]:
        pwd = input("请输入新密码：")
        pwd2 = input("请确认新密码：")
        if pwd == pwd2:
            user_dic[name]["pwd"] = pwd
            input("修改成功，按任意键继续。。")
        else:
            input("两次密码不一致，请重新输入，按任意键继续。。")
    else:
        if pwd_error >= 3:
            input("输入错误次数过多，已退出，按任意键继续")
        input("密码有误，请重新输入，按任意键继续。。")
        pwd_error += 1


#选课选项菜单
user_select_dic = {
    "1":"check_select_course",  #注册
    "2":"into_select_course",     #登录
    "3":"alter_pwd",  #管理员
    "4":"main"
}
def select_course(name):
    while True:
        show_select_course()
        choose = input("请输入功能选项：")
        # 查看已有的选课
        operate = user_select_dic.get(choose)
        if operate:
            func = eval(operate)
            if func!=main:
                func(name)
            else:
                func()
        else:
            input("输入有误，请重新输入，按任意键继续。。")

def admin_show_menu():
    print("1.查看课程")
    print("2.增加课程")
    print("3.删除课程")
    print("4.返回上一级")
    admin()

def admin_check_course():
    print("欢迎来到查看课程界面")
    print("目前有以下课程")
    for i in range(len(course_lst)):
        print("{} : {}".format(i + 1, course_lst[i]))
    input("按任意键继续。。。。")
    admin_show_menu()

def admin_add_course():
    print("欢迎来到增加课程界面")
    course_name = input("请输入要增加的课程名称：")
    if course_name in course_lst:
        input("课程已存在，请勿重复添加")
        admin_show_menu()
    else:
        course_lst.append(course_name)
        input("课程添加成功，按任意键继续")
        admin_show_menu()

def admin_delete_course():
    print("欢迎来到删除课程界面")
    print({i + 1: course_lst[i] for i in range(len(course_lst))})
    num = int(input("请输入要删除的课程编号："))
    if 1 <= num <= len(course_lst):
        ret = course_lst.pop(num - 1)
        input("删除%s成功，按任意键继续" % ret)
        admin_show_menu()
    else:
        print("输入编号有误，无法删除，按任意键继续。。。")
        admin_show_menu()

def admin_login():
    print("欢迎来到管理员界面")
    name = input("请输入管理员用户名：")
    pwd = input("请输入管理员密码：")
    if name == Administrator["name"] and pwd == Administrator["pwd"]:
        print("登录成功")
        admin_show_menu()
    else:
        input("登录失败，按任意键继续。。")
        main()

#管理员选项菜单
admin_dic = {
    "1":"admin_check_course",  #注册
    "2":"admin_add_course",     #登录
    "3":"admin_delete_course",#管理员
    "4":"admin_back",} #返回上一级

def admin_back():
    main()


def admin():
    choose = input("请输入功能选项：")
    operate = admin_dic.get(choose)
    if operate:
        func = eval(operate)
        func()
    else:
        input("输入有误，请重新输入，按任意键继续。。")
        admin()

def user_exit():
    print("已退出")
    exit(1)

#选项菜单
index_dic = {
    "1":"register",  #注册
    "2":"login",     #登录
    "3":"admin_login",#管理员
    "4":"user_exit",} #退出
def main():
    show_mune()
    choose = input("请输入功能选项：")
    operate = index_dic.get(choose)
    if operate:
        func = eval(operate)
        func()
    else:
        input("输入有误，请重新输入，按任意键继续。。")
        return main()
main()