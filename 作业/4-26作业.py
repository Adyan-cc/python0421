#
# 1.存在字典 info = {'name':'张三'},给字典增加性别信息，值为“男”。
# 	清空整个字典
# 	根据键获取字典的性别信息，获取不到默认是男性
# 	删除整个字典

# info = {'name':'张三'}
# info["male"] = "男"
# print(info)
# info.clear()
# print(info)
# print(info.get("male",'男'))
# del info

# 2.使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），
# 这些信息来自 键盘的输入
#
# name_dict = {}
# while True:
#     info_list = []
#     name_1 = input("请输入姓名：")
#     age_1 = int(input("请输入年龄："))
#     sex_1 = input("请输入性别(男/女)：")
#     score_1 = float(input("请输入QQ："))
#     weixin_1 = input("请输入微信：")i
#     address_1 =input("请输入地址：")
#     car_dict={'name':name_1,'age':age_1,'sex':sex_1,'score':score_1,'weixin':weixin_1,'weixin':weixin_1,'address':address_1}
#     print(car_dict)
# lst = ['姓名','年龄','学号','QQ','微信','住址']
# info_dic={}
# for i in lst:
#     string='请输入'+i
#     ret = input(string)
#     info_dic[i]=ret
# print(info_dic)


# 3.字典dict1 = {'name':'小明','age':18,'weight':180,'score':150}，交换键和值并输出
#
# dict1 = {'name':'小明','age':18,'weight':180,'score':150}
# # dict2={}
# # for i,j in dict1.items():
# # #     dict2.update({j:i})
# #     dict2[j]=i#新的
# # print(dict2)

# 4.循环录入3个学生的学生信息(姓名，年龄，性别，分数)，存储到合理的容器中
# (可以使用字典或者列表)
# 如：[{'姓名': '李白', '年龄': '25', '性别': '男', '分数': '100'}, {'姓名': '貂蝉', '年龄': '20', '性别': '女', '分数': '99'}, {'姓名': '吕布', '年龄': '33', '性别': '男', '分数': '35'}]
#

# 5.列表 lst=['hello','world','python','java','web', 'UI', 'linux', 'unity']
# 请以字符串为键，长度为值建立字典。
#

# 6.生成如下格式字典，格式如下:{'a':97,'b':98,'c':99...}
#
# dic1={}
# for i in range(97,123):
#     dic1.update({chr(i):i})
# print(dic1)


# 7.使用列表推导式输出一个10以内的偶数的平方的列表
#
# lst1=[i*i for i in range(2,11,2)]
# print(lst1)


# 8.商城项目综合开发，将数据，如注册用户信息等存储到列表或字典中

# 导航页面
import random
import time
_mi=[]
username = '1'
password = '2'
while True:
    print('= ' * 13)
    print(' ' * 7, '购物商城')
    print('= ' * 13)
    print(' ' * 6, '1、会员登录')
    print(' ' * 6, '2、用户注册')
    print(' ' * 6, '3、密码更改')
    print(' ' * 6, '4、退出系统')
    print('= ' * 13)
# 提示用户输入选项 choice~选择
    choice = input("请输入您的选项(1/2/3)：")
    if choice == "1":
        while True:

            user_username = input('请输入您的账号')
            user_password = input('请输入您的密码')
            if user_username != username:
                print('账号有误')
            elif user_username == username and user_password != password:
                print('密码有误')
            else:
                print('~' * 10, '登录成功', '~' * 10)
            break
        break
#注册账户
    elif choice == "2":
        print('= ' * 13)
        print(' ' * 8, '注册账户', ' ' * 8)
        account = input('请输入账号')
        password = input('请输入密码')
        password1 = input('请确认密码')
        while True:
                if password == password1:
                    _mi.append(account)
                    _mi.append(password1)
                    print(' ' * 8, '注册成功', ' ' * 8)
                    time.sleep(3)
                    break
                else:
                    password = input('请重新输入密码')
                    password1 = input('请确认密码')
                break
#修改密码
    elif choice == "3":
        print('=' * 30)
        a = input('输入新密码')
        b = input('确认密码')
        print('=' * 30)
        if a == b:
            password = b
            print('请重新登录,正在返回登陆页面。。。')
            time.sleep(3)
        else:
            print('重新输入，正在返回首页')
            input('按任意键返回首页')

    elif choice == "4":
    # 退出程序？怎么退出?
        print('谢谢惠顾，客观下次光临噢')
    elif choice != "4":
        print('输入错误，从新开始。。。。')
    elif choice != "3":
        print('输入错误，从新开始。。。.')
    elif choice != "2":
        print('输入错误，从新开始。。。。')
    elif choice != "1":
        print('输入错误，从新开始。。。。')
else:
    input("没有这个选项，是不是按错了？按任意键退出系统")

print('= ' * 13)
print(' ' * 6, '4、购物商城')
print(' ' * 6, '3601:衣服')
print(' ' * 6, '3602:裤子')
# 提示用户输入选项 choice~选择
choice = input("  请输入编号\n（3601、3602）：")
print('= ' * 13)
if choice =="3601":
    name = "衣服"
    numb = "3601"
    quantity = 9999
    price = 88
    # 1.运行脚本展示一个商品的信息
    print("商品名称：" +name)# 3. 提示购买的商品名称
    print("商品编号：" +name)# 2.提示用户要购买的商品编号
    print("现有库存：", quantity, "件")#quantity数量
    print("商品单价：", price, "元/件")#price单价
elif choice =="3602":
    name = "裤子"
    numb = "3602"
    quantity = 9999
    price = 80
    # 1.运行脚本展示一个商品的信息
    print("商品名称：" +name)# 3. 提示购买的商品名称
    print("商品编号：" +numb)# 2.提示用户要购买的商品编号
    print("现有库存：", quantity, "件")#quantity数量
    print("商品单价：", price, "元/件")#price单价
else:
    print()
buy_quantity = int(input("请输入您购买的件数："))# 4.提示用户购买的数量
allGoods_money = buy_quantity * price#allGoods所有货物金额=buy_quantit * yprice购买数量*价格
print("您总共买了%s件商品，\n需要付款%d元" % (buy_quantity, allGoods_money))# 5.显示用户购买的商品信息，如商品名，购买数量，商品单价，付款金额
buy_money = int(input("请您付款："))# 6.提示付款
while buy_money < allGoods_money:#while循环结构
    buy_money = int(input("你的余额不足，\n请重新付款："))
print('= ' * 13)
print("谢谢您的光临！")# 7.付款后给出订单信息
print("您的账单：")
print("商品名称：" + name)
print("商品编号：" + numb)
print("购买数量：", buy_quantity, "只")
print("商品单价：", price, "元/件")
print("总共消费：", allGoods_money, "元")
print("找余：", buy_money - allGoods_money, "元")
print('= ' * 13)
