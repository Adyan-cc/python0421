"""
用户信息登记系统
    讲解
        while循环
        for循环
        适用场景
"""
# 下回预告：一个变量中保存多个数据-列表[]
names = []
# 多个人登记姓名：while循环
while True:
   # 用户输入姓名
   n = input("请输入您的姓名(Q登记完成退出)：")
   if n == "Q":
        break
   # 保存一个用户：把一个数据添加到列表中
   names.append(n)

# 查看系统中都有哪些用户：for循环
for x in names:
    print("登记的用户：", x)

print("---------------------") # 章成
print(names)