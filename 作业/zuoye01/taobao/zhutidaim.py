'''输入选择后的代码'''

# 登陆
def denlu_gongneng():
    while True:
        # 用户输入密码
        user_ID = input("请输入您的账号:")
        user_Password = input("请输入您的密码:")
        for users in user:
            if user_ID == users[0] and user_Password == users[1]:
                print("账号密码输入正确，登录成功！")
                input("按任意键进入商城首页>>>>")
                time.sleep(1)
                break
        else:
            input("账号或密码错误！！按任意键进入继续.")
            continue


# 新用户注册
def zhuce_gongneng():
    while True:
        user_ID = input("请输入你要注册的账号：")
        user_Password = input("请输入注册账号的密码：")
        user_nicheng = input("请创建此账号的昵称:")
        if len(user_ID) > 0 and len(user_Password) > 0 and len(user_nicheng) > 0:
            users = [user_ID, user_Password, user_nicheng]
            user.append(users)
            input("注册成功！按任意键进入登录首页")
            break
        else:
            input("注册失败！按任意键继续.")
            continue


#退出程序
def tuic_gongneng():
    input("谢谢惠顾")
    exit(1)

# 进入超市首页
# 干果类
def ganguo_gongneng():
    print("功能完善ing...按任意键继续>>>")
# 酒水类
def jiushui_gongneng():
    print("功能完善ing...按任意键继续>>>")
# 蔬菜类
def shucai_gongneng():
    print("功能完善ing...按任意键继续>>>")

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():

def zhuce_gongneng():