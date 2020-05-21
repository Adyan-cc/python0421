import os


# 首页展示界面
def shou_ye():
    os.system("cls")
    print(' ='*10,'欢迎进入lc电子商城',' ='*10)
    print(' ='*30)
    print(' '*12,'1.用户登录')
    print(' '*12,'2.新用户注')
    print(' '*12,'3.退出登录')
    print(' ='*30)
#登录后选项页
def deng_lu(a=users):
    os.system("cls")
    print("尊敬的用户:", a[2])
    print(' ='*10,'欢迎进入lc电子商城',' ='*10)
    print(' ='*30)
    print(' '*12,'1.购物:进入超市')
    print(' '*12,'2.休闲:游戏天地')
    print(' '*12,'3.饮食:美食商城')
    print(' '*12,'4.返回登录主界面')
    print(' '*12,'5.退出电子商城系统')
    print(' ='*30)

#商品分类
def shangpin_fenlei():
    os.system("cls")
    print(' ='*10,'欢迎进入lc电子商城',' ='*10 .center(68))
    print(' =' * 30 .center(68))
    print(' '*12,'1.干果类'.center(68))
    print(' '*12,'2.酒水类'.center(68))
    print(' '*12,'3.蔬菜类'.center(68))
    print(' '*12,'4.退出系统'.center(68))
    print(' =' * 30 .center(68))

#游戏选择
def youxi_shouye():
    os.system("cls")
    print(' ='*10,'欢迎进入lc电子商城',' ='*10)
    print(' =' * 30)
    print(' '*12,'1.老虎棒子鸡')
    print(' '*12,'2.石头剪刀布')
    print(' '*12,'3.退出游戏商城')
    print(' =' * 30)

#美食选择
def meishi_xuanzhe():
    os.system("cls")
    print(' ='*10,'欢迎进入lc电子商城',' ='*10)
    print(' =' * 30)
    print(' '*12,'1.东方饮食')
    print(' '*12,'2.西方饮食')
    print(' '*12,'3.退出饮食商城')
    print(' =' * 30)
