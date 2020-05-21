'''
学生选课系统
时间;2020-4-27
版本：1.0.0
作者：刘江
'''
# 开头文档写出 普通用户、课程的保存方式
# 管理员 事先设置好管理员账号密码
# 管理员功能：查看有哪些课程,Python，java，web，unity，UI
# 增加或删除课程内容，增加 软件测试课程，删除UI课程
# 用户
# 注册 ：用户名和密码注册，没有注册过用户的才可以注册成功
# 登录 ：用户名和密码登录，登录成功进入选课界面
# 修改登录密码：输入旧密码，再输入新密码
# 查看：查看已选的课程
# 选课程：进行选课，选完课记录下来，下次查看可以看到
# 学生选课系统添加功能 ，学生选课，管理员增加、删除课程前需要验证，输入4位验证码才可以执行后续功能

# 保存课程内容
course_lst = ["Python", "java", "web", "unity", "UI"]
# 保存用户
user_dic = {"zhang": {"name": "zhang", "pwd": "123", "course": []}}
Administrator = {"name": "1", "pwd": "2"}

import random
import time
#首页
def shouye():
    pass
#验证码
def yanzhengma():
    pass
#主界面
def zhujiemian():
    pass
#学生选课主界面
def xueshengzhuye():
    pass
#ch



#管理员主界面
def guanlizhuye():
    pass