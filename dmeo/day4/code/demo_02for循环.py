
#将字符串中的字符依次取出来，赋值给临时变量i
for i in "python":
	print(i)
    # print(111)

#range()
# print(list(range(1, 5)))
# for i in range(1,5):
#     print(i,end=' ')
# for i in range(1,5,2):
#     print(i,end=' ')
# for i in range(5,1,-2):
#     print(i,end=' ')
# for i in range(5):
#     print(i,end=' ')

# 求1-100之间所有偶数的和
# sum_num = 0
# for i in range(2,101,2):
#     # print(i,end=' ')
#     sum_num+=i
# print(sum_num)

# 输出100-200范围内的所有质数
#for循环中的代码正常执行结束，走else，没有正常结束，如遇到break，则不走else

for i in range(100,201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i,end=' ')
