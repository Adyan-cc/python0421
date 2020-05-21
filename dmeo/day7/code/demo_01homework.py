# 1.将字符串‘my name is zhangWeiqiang’中的每个单词输出一样，要求单词首字母大写效果如下
# content = "my name is zhangqeiqiang" #My Name Is Zhangweiqiang
# content = "my name is zhangqeiqiang"
# new_content = content.title()
# print(new_content)
# 2.判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# num = input("请输入一个整数：")
# if num.isdigit():
#     if num==num[::-1]:
#         print("是回文数")
#     else:
#         print("不是回文数")
# else:
#     print("不是回文数")


# 3.键盘接收传入的字符串，统计大写字母的个数、小写字母的个数、数字的个数、其它字符的个数
# content =  "I'm Zhang,18 years old"
# upper_count = 0
# lower_count = 0
# digit_count = 0
# other_count = 0
# for i in content:
#     if i.isupper():
#         upper_count+=1
#     elif i.islower():
#         lower_count+=1
#     elif i.isdigit():
#         digit_count+=1
#     else:
#         other_count+=1
# print("大写字母:%d,小写字母:%d,数字:%d,其它字符:%d"
#       %(upper_count,lower_count,digit_count,other_count))


# 4.句子反转
# 给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，单词用空格分割,
# 单词之间只有一个空格，前后没有空格。
# 比如： （1） “hello xiao mi”-> “mi xiao hello”
# content = "hello xiao mi"
# lst = content.split(' ')
# lst.reverse()
# print(lst)
# string = ""
# for i in lst:
#     string=string+i+' '
# print(string.strip())

#join()方法：可以将列表中的字符串拼接起来
# 格式：  拼接字符.join(列表)
# lst = ["a","b","c"] # a*b*c
# ret = "*".join(lst)
# print(ret)

content = "hello xiao mi"
lst = content.split(" ")[::-1]
ret = " ".join(lst)
print(ret)




# 5.完成学生管理系统
# 开头文档写出 普通用户、课程的保存方式


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
Administrator = {"name":"admin","pwd":"admin"}
while True:
    print("欢迎学生选课主界面")
    print("~*" * 15)
    print("        1.用户注册           ")
    print("        2.用户登录           ")
    print("        3.管理员登录           ")
    print("        4.退出系统           ")
    print("~*" * 15)
    choose = input("请输入功能选项：")
    if choose=="1":
        print("欢迎来到注册界面！")
        name = input("请输入注册用户名：")
        pwd = input("请输入注册密码：")
        #判断用户名是否已存在，已存在则不允许注册
        if name not in user_dic: #用户名不存在
            user_dic[name] = {"name":name,"pwd":pwd,"course":[]}
            input("注册成功，按任意键继续。。。")
        else:#用户名已存在
            input("用户名已存在，按任意键继续。。。")

    elif choose=="2":
        flag = 0
        print("欢迎来到登录界面！")
        name: str = input("请输入登录用户名：")
        pwd = input("请输入登录密码：")
        if name in user_dic: #说明登录名在保存的user_dic中
            #用户名和密码匹配
            if name==user_dic[name]["name"] and pwd==user_dic[name]["pwd"]:
                print("登录成功")
                flag=1
            else:
                print("密码错误")
        else:
            print("用户名不存在")
        #登录成功，走下面的代码
        if flag:
            while True:
                print("欢迎来到选课界面！")
                print("        1.查看选课          ")
                print("        2.进入选课           ")
                print("        3.修改密码           ")
                print("        4.返回上一级           ")
                choose = input("请输入功能选项：")
                # 查看已有的选课
                if choose == "1":
                    if user_dic[name]["course"]:
                        print("已选的课程：",user_dic[name]["course"])
                        input("按任意键继续。。。")
                    else:
                        input("没有选中任何课程，按任意键继续。。。")
                #进入选课
                elif choose == "2":
                    print("请选择课程：")
                    for i,j in enumerate(course_lst,1):
                        print("%s:%s"%(i,j))
                    choose = int(input("请输入课程编号："))
                    #用户输入编号在范围内
                    if 1<=choose<=len(course_lst):
                        #取出课程
                        course = course_lst[choose-1]
                        #如果已经选过此课程
                        if course in user_dic[name]["course"]:
                            print("已选过此课程")
                            input("按任意键继续。。。")
                        else:
                            user_dic[name]["course"].append(course)
                            print("选课成功，您选择的课程是:%s"%course)
                            input("按任意键继续。。。")
                    else:
                        print("编号不在范围内。。。")
                        input("按任意键继续。。。")
                elif choose == "3":
                    pwd_error = 0
                    while True:
                        print("欢迎进入修改密码界面！")
                        old_pwd = input("请输入旧密码：")
                        #判断旧密码是否正确
                        if old_pwd==user_dic[name]["pwd"]:
                            pwd = input("请输入新密码：")
                            pwd2 = input("请确认新密码：")
                            if pwd==pwd2:
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
                            pwd_error+=1
                elif choose == "4":
                    break
                else:
                    input("输入有误，请重新输入,按任意键继续。。。")

    elif choose=="3":
        flag = 0
        print("欢迎来到管理员界面")
        name = input("请输入管理员用户名：")
        pwd = input("请输入管理员密码：")
        if name==Administrator["name"] and pwd==Administrator["pwd"]:
            print("登录成功")
            flag = 1
        if flag:
            while True:
                print("1.查看课程")
                print("2.增加课程")
                print("3.删除课程")
                print("4.返回上一级")
                choose = input("请输入功能选项：")
                if choose=="1":
                    print("欢迎来到查看课程界面")
                    print("目前有以下课程")
                    for i in range(len(course_lst)):
                        print("{} : {}".format(i+1,course_lst[i]))
                    input("按任意键继续。。。。")
                elif choose=="2":
                    print("欢迎来到增加课程界面")
                    course_name = input("请输入要增加的课程名称：")
                    if course_name in course_lst:
                        input("课程已存在，请勿重复添加")
                    else:
                        course_lst.append(course_name)
                        input("课程添加成功，按任意键继续")
                elif choose=="3":
                    print("欢迎来到删除课程界面")
                    print({i+1:course_lst[i] for i in range(len(course_lst))})
                    num = int(input("请输入要删除的课程编号："))
                    if 1<=num<=len(course_lst):
                        ret = course_lst.pop(num-1)
                        input("删除%s成功，按任意键继续"%ret)
                    else:
                        print("输入编号有误，无法删除，按任意键继续。。。")
                elif choose=="4":
                    break

    elif choose=="4":
        print("已退出！")
        break
    else:
        input("输入有误，请重新输入,按任意键继续。。。")

















