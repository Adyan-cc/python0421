# 1.求0-100范围内能被7整除但不带7的整数，并储存到列表中

# lst=[]
# for i in range(0,101):
#     if i%7==0 and i%10!=7 and 1//10!=7:
#         lst.append(i)
#         print(lst)

# 2.快递运费首重6元，超过则加收3元/kg(首重1kg，首重和后续不满1kg则按1kg计算),要求输入货物重量，计算运费。

# w=float(input('输入重量：'))
# if w==int(w):
#     m=6+(w-1)*3
# else:
#     m=6+int(w)*3
# print(m)


# 3.存在列表 a = [11, 22, 33], 如何向列表尾部添加新元素 44,如何删除列表中的元素 33

# a = [11,22,33]
# a.append(44)
# a.remove(33)
# print(a)

# 4.存在列表a = [6,5,4,19,17,11,13,43,55,66,77,14,87,26,22,34,39,88,76,21,96,33,51,52,53,54,81,76],列表中元素不重复，如何修改列表中的元素 22 为 55

# import random
# a = [6,5,4,19,17,11,13,43,55,66,77,14,87,26,22,34,39,88,76,21,96,33,51,52,53,54,81,76]
# i_22 = a.index(22)#快速索引22的位置
# print(i_22)

# print(a.index(22))
# a[14]=55
# print(a)


# 5. 比较两个列表中的元素,找出不相同的元素并保存在列表3中


# lst1 = ["Sun", "Mon", "Tue", "Wed", "Fri", "Sat"]
# lst2 = ["Sun", "Tue", "Thu", "Sat","Tom"]
# lst3 = []
# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)
#


# a = lst1 + lst2#我答
# for i in a:
#     if i.count(i)==1:
#         a.append(i)
# print(lst3)


# 6.使用列表嵌套，完成8名老师随机分配3个办公室,办公室人数无要求，输出哪个办公室有哪些老师？
#   老师可用a,b,c,d,e,f,g,h代替

# of=[[],[],[]]
# a=['a','b','c','d','e','f','g','h']
# import random # 随机模块
# #思路:遍历，取出，随机放入
# for t in a:
#     of_index = random.randint(0,2)#随机办公室
#     of[of_index].append(t)
# for ofs in of:
#     print(ofs)

# 7.完善商城项目用户注册、商城项目用户登录、修改登录密码，购买多个商品等

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
