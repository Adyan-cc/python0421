# 1.求0-100范围内能被7整除但不带7的整数，并储存到列表中
#被7整除，n%7==0
#不带7：个位数不带7  n%10!=7
        #十位数不带7  n//10!=7
# lst = []
# for i in range(0,101):
#     if i%7==0 and i%10!=7 and i//10!=7:
#         lst.append(i)
# print(lst)
# print([i for i in range(0,101) if i%7==0])


# 2.快递运费首重6元，超过则加收3元/kg(首重1kg，首重和后续不满1kg则按1kg计算),要求输入货物重量，计算运费。
#6 +(weight-1)*3
# weight = float(input("请输入货物的重量："))
# #如果货物重量正好是整数
# if weight==int(weight):
#     money = 6+(weight-1)*3
# #如果货物重量是小数
# # 2.1    6+（3-1）*3
# else:
#     money = 6+int(weight)*3
# print("运费是：",money,"元")

# 3.存在列表 a = [11, 22, 33], 如何向列表尾部添加新元素 44,如何删除列表中的元素 33
# a = [11, 22, 33]
# a.append(44)
# a.remove(33)
# print(a)

# 4.存在列表a = [6,5,4,19,17,11,13,43,55,66,77,14,87,26,22,34,39,88,76,21,96,33,51,52,53,54,81,76],
# 列表中元素不重复，如何修改列表中的元素 22 为 55
# a = [6,5,4,19,17,11,13,43,55,66,77,14,87,26,22,34,39,88,76,21,96,33,51,52,53,54,81,76]
# for i in range(len(a)):
#     if a[i]==22:
#         a[i]=55
# print(a)
#获取22对应的索引
# index_22 = a.index(22)
# print(index_22)
# #根据索引修改值
# a[index_22] = 55
# print(a)

# 5. 比较两个列表中的元素,找出不相同的元素并保存在列表3中
# lst1 = ["Sun", "Mon", "Tue", "Wed", "Fri", "Sat"]
# lst2 = ["Sun", "Tue", "Thu", "Sat","Tom"]
# lst3 = []
# #遍历lst1，找出lst1里有，但是lst2没有的元素
# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)
# for j in lst2:
#     if j not in lst1:
#         lst3.append(j)
# print(lst3)


# 6.使用列表嵌套，完成8名老师随机分配3个办公室,办公室人数无要求，输出哪个办公室有哪些老师？
#   老师可用a,b,c,d,e,f,g,h代替
#使用三个列表代表三个办公室
# offices = [[],[],[]]
# teachers = ["a","b","c","d","e","f","g","h"]
# import random
# #遍历老师列表，取出每一位老师的同时，随机一个办公室，放入老师
# for t in teachers:
#     #随机一个办公室索引
#     off_index = random.randint(0,2)
#     #根据办公室索引，取出办公室，放入老师
#     offices[off_index].append(t)
# for office in offices:
#     print(office)

# 7.完善商城项目用户注册、商城项目用户登录、修改登录密码，购买多个商品等
#中公点餐系统
lst = [] #储存用户名和密码
while True:
    print("*"*30)
    print("     欢迎来到中公点餐系统      ")
    print("     1.注册        ")
    print("     2.登录        ")
    print("     3.退出        ")
    print("*" * 30)
    choice = input("请输入功能选项：")
    if choice=="1":
        print("*" * 30)
        print("     欢迎来到注册界面     ")
        name = input("请输入注册用户名：")
        while True:
            pwd1 = input("请输入密码：")
            pwd2 = input("请确认密码：")
            if pwd1==pwd2:
                print("注册成功")
                lst.append([name,pwd1])
                break
            else:
                print("两次密码不一致，请重新输入")
    elif choice=="2":
        print("*" * 30)
        print("     欢迎来到登录界面     ")
        name = input("请输入用户名：")
        pwd = input("请输入密码：")
        for i in lst:
            if i[0]==name and i[1]==pwd:
                print("登录成功")
                break
        else:
            print("用户名或密码错误")
        if i[0] == name and i[1] == pwd:
            while True:
                print("*" * 30)
                print("     欢迎来到点餐界面      ")
                print("请输入序号选择商家")
                print("     1.煲仔饭        ")
                print("     2.皇冠烧腊        ")
                print("     3.楚留香大碗饭        ")
                print("     4.返回上一级菜单        ")
                choice = input("请输入功能选择：")
                if choice=="1":
                    pass
                elif choice=="2":
                    pass
                elif choice=="3":
                    pass
                elif choice=="4":
                    print("返回上一级菜单")
                else:
                    print("输入有误，请重新输入")
    elif choice=="3":
        print("已退出")
        break
    else:
        print("输入有误，请重新输入")
        input("按任意键回车继续。。。。")