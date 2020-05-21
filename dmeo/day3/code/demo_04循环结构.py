
#下班太晚，和女朋友说一万次对不起
# print("对不起！")

#相同或者相似的事情可以用循环解决
# num = 1
# while num<=10000:
#     print("对不起！-",num)
#     num+=1

#输出1-10之间的数字
# num = 1
# while num<=10:
#     print(num,end=' ')
#     num+=1

#售票：一个窗口一天售出10张票，卖完下班
# ticket = 10
# while ticket>0:
#     print("卖出一张票：",ticket,"号票")
#     ticket-=1

#循环从控制台输入5个数，输出最大值
# a, b, c, d, e = 1, 5, 3, 2, 4
# max_num = a
# if max_num<b:
#     max_num = b
# if max_num<c:
#     max_num = c
# if max_num<d:
#     max_num = d
# if max_num<e:
#     max_num = e
# print(max_num)

count = 1
max_num = False
while count<=5:
    num = int(input("请输入数字："))
    if count==1: #第一次输入
        max_num = num
    else:
        if max_num<num:
            max_num=num
    count+=1
print(max_num)