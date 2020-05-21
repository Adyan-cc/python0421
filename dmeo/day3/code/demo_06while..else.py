

#卖10张门票，有一定几率会下暴雨，
#如果下暴雨的概率超过30%，则提前下班
#如果没有，则卖完票正常下班
# import random
# ticket = 10
# while ticket>0:
#     percent = random.randint(1,100) #下雨的几率，概率超过50%，提前下班
#     if percent<=10:
#         print("下雨了，回家收衣服啦！")
#         break
#     print("售出门票：",ticket,"号票")
#     ticket-=1
# else:
#     print("卖完票了，正常下班！")


#输入一个数，判断是否是质数
#只能被1和本身整除的数
#7,27,1,2
#将这个数n除以2,3,4,5...n-1,如果都不能整除，说明是质数
n = int(input("请输入一个整数："))
if n>=2:
    #将18除以2,3,4,5...17
    i = 2
    while i<n:
        if n%i==0: #如果余数是0，说明可以整除
            print(n,"不是质数")
            break
        i+=1
    else:
        print(n,"是质数")
else:
    print(n, "不是质数")