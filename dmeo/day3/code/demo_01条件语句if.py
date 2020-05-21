
#单分支
#判断一个人是否可以去网吧
#如果大于等于18岁，可以去

# age = 15
# if age>=18:
#     print("可以去网吧")
# print("一天过去了！")

#双分支
#判断一个人是否可以去网吧
#如果大于等于18岁，可以去，否则回家写作业
# age = 15
# if age>=18:
#     print("可以去网吧嗨皮！")
# else: #else中不写条件语句
#     print("回家写作业！")
# print("一天过去了！")

#判断一个人是否可以去网吧
#如果大于等于18岁,并且是男生，可以去，否则回家写作业
# age = 19
# gender = 0
# if age>=18 and gender==1:
#     print("可以去网吧嗨皮！")
# else:
#     print("回家写作业！")
# print("一天过去了！")

# 案例操作：给贵妃熬粥的需求
#贵妃在一定条件下得分，另外一种条件被下毒
# import random  #随机一定范围内的整数
#
# # print(random.randint(1,10))
# score = 20
# x = random.randint(1,10)
# print(x)
# if x>6:
#     print("粥被人下毒了。。")
#     print("贵妃身亡")
# else:
#     print("贵妃身体无恙，可以继续在宫中享受")
#     print("加5分")
#     score+=5
# print(score)

#多分支
#需求：节日给女朋友送礼物
#情人节，送鲜花
#端午节：发红包
#国庆节：出去旅游
#其他：多喝热水
# holiday = input("请输入节日：")
# if holiday=="情人节":
#     print("送鲜花")
# elif holiday=="端午节":
#     print("发红包")
# elif holiday=="国庆节":
#     print("出去旅游")
# else:
#     print("多喝热水")


# 分支嵌套
#需求：买火车票回家，如果有火车票，可以进站，没有不可以进站
#进站后检查行李，如果刀具长度小于18cm，可以上火车，否则不可以上火车
has_ticket = input("请问是否有火车票（有/1,没有/0）")
if has_ticket=="0" or has_ticket=="1":
    if has_ticket=="1":
        print("可以进站！")
        knife = float(input("请输入刀具长度："))
        if knife<18:
            print("可上火车！")
     
        else:
            print("刀太长，无法带上火车")
    else:
        print("没有票，无法进站")
else:
    print("输入有误，终止操作！")