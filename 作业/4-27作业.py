"""
学生选课系统
时间：2020-4-27
版本：1.0.0.1
作者：刘江
"""
# 1.将字符串‘my name is zhangWeiqiang’中的每个单词输出一样，要求单词首字母大写效果如下
# content = "my name is zhangqeiqiang" #My Name Is ZhangWeiqiang

# content = 'my name is zhangWeiqiang'
# print(content.title())

# 2.判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# n = input("请输入任一自然数:")
# l = len(n)
# j = 0
# for i in range(l):
#     if n[i] == n[-(i + 1)]:
#         pass
#     else:
#         j = j + 1
# if j == 0:
#     print("yes")
# else:
#     print("no")
#
# 3.键盘接收传入的字符串，统计大写字母的个数、小写字母的个数、数字的个数、其它字符的个数
#

# 4.句子反转
# - 题目描述：
# 给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，>单词用空格分割, 单词之间只有一个空格，前后没有空格。
# 比如： （1） “hello xiao mi”-> “mi xiao hello”

# lst = 'hello xiao mi'
# ret = lst.split(" ")
# ret.reverse()
# str=""
# for i in ret:
#     str=str+i+' '
# print(str.strip)

# 5.完成学生管理系统
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



#没写完
course_lst = ["Python","java","web","unity","UI"]
users = [
    ['2','2','2'],
    ["1", "1", "1"]
]
username_1 = '1'
password_2 = '2'
while True:
    print("= " * 3,"欢迎学生选课主界面","= " * 3)
    print(" "*8,'1.用户注册')
    print(" "*8,'2.用户登录')
    print(" "*8,'3.管理员登录')
    print(" "*8,'4.退出系统')
    print("= " * 15)
    choose = input("请输入功能选项：")
    if choose=="1":
        username = input("请输入注册账号：")
        password = input("请输入注册密码：")
        user = [username, password]
        users.append(user)
        input("注册成功，按任意键返回登录菜单")

    elif choose=="2":
        username = input("请输入账号：")
        password = input("请输入密码：")

        if username in users:
            if username == username[0] and password == username[1]:
                input("登录成功，按任意键继续")
                break

        else:
            input("账号或者密码有误，请重新登录")
        print(" = 尊敬的用户欢迎来到选课系统 = ")

    elif choose=="3":
        inuser = input('管理员账户:')
        inpasswd = input('管理员密码:')
        if inuser == username_1 and inpasswd == password_2:
            print('管理员登录成功！')
            print("= " * 3, "欢迎管理员操作界面", "= " * 3)
            print(" " * 8, '1.添加课程信息')
            print(" " * 8, '2.删除课程信息')
            print(" " * 8, '3.查看课程信息')
            print(" " * 8, '4.退出系统')
            print("= " * 15)
        choose_1 = input('请选择你的操作:')
        if choose_1 == '1':
            print("= " * 3, "添加课程信息", "= " * 3)
            course_1 = input('请添加课程名称:')
            for course_1 in course_lst:   #有bug不走if
                print(course_1)
                print('该课程%s已经存在'%(course_1))
                course_lst.append(course_1)
                print('添加课程%s成功!'%(course_1))
            else:
                input('按任意键返回')

        elif choose_1 =='2':
            print("= " * 3, "删除课程信息", "= " * 3)
            delete = input('删除课程名称:')
            course_lst.remove(delete)
            print('删除会员%s成功!' % delete)
        elif choose_1 =='3':
            pass
        elif choose_1 =='4':
            pass

    elif choose=="4":
        input('任意键退出系统')
        break
    else:
        input("输入有误，请重新输入,按任意键继续。。。")
