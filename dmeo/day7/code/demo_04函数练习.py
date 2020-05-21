

#将注册功能封装成函数
#保存课程内容
course_lst = ["Python","java","web","unity","UI"]
#保存用户
user_dic = {"zhang":{"name":"zhang","pwd":"123","course":[]}}
Administrator = {"name":"admin","pwd":"admin"}
def register():
    print("欢迎来到注册界面！")
    name = input("请输入注册用户名：")
    pwd = input("请输入注册密码：")
    #判断用户名是否已存在，已存在则不允许注册
    if name not in user_dic: #用户名不存在
        user_dic[name] = {"name":name,"pwd":pwd,"course":[]}
        input("注册成功，按任意键继续。。。")
    else:#用户名已存在
        input("用户名已存在，按任意键继续。。。")
register()
print(user_dic)