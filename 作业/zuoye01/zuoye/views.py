'''界面模块'''
from unicodedata import name

from 作业.zuoye01.zuoye.sevices import check_select_course, into_select_course, alter_pwd, admin_check_course, \
    admin_add_course, admin_delete_course


# 管理员界面
def admin_show_menu():
    print("1.查看课程")
    print("2.增加课程")
    print("3.删除课程")
    print("4.返回上一级")


def show_menu():
    while True:
        admin_show_menu()
        choose = input("请输入功能选项：")
        if choose == "1":
            admin_check_course()
        elif choose == "2":
            admin_add_course(name)
        elif choose == "3":
            admin_delete_course(name)
        elif choose == "4":
            break


# 学生操作界面
def show_select_course():
    print("欢迎来到选课界面！")
    print("        1.查看选课          ")
    print("        2.进入选课           ")
    print("        3.修改密码           ")
    print("        4.返回上一级           ")


def select_course(name):
    while True:
        show_select_course()
        choose = input("请输入功能选项：")
        # 查看已有的选课
        if choose == "1":
            check_select_course(name)
        # 进入选课
        elif choose == "2":
            into_select_course(name)
        # 修改密码
        elif choose == "3":
            alter_pwd(name)
        elif choose == "4":
            break
        else:
            input("输入有误，请重新输入,按任意键继续。。。")


# 主界面
def show_mune():
    print("欢迎学生选课主界面")
    print("~*" * 15)
    print("        1.用户注册           ")
    print("        2.用户登录           ")
    print("        3.管理员登录           ")
    print("        4.退出系统           ")
    print("~*" * 15)


def shou_ye():
    while True:
        show_mune()
        choose = input("请输入功能选项：")
        if choose == '1':
            from 作业.zuoye01.zuoye.sevices import register
            register()
        elif choose == '2':
            from 作业.zuoye01.zuoye.sevices import login
            login()
        elif choose == '3':
            from 作业.zuoye01.zuoye.sevices import admin_login
            admin_login()
        elif choose == '4':
            user_exit()


# 退出程序
def user_exit():
    print("已退出")
    exit(1)
