
#有代码实现吃饭的需求
#吃早饭
# print("洗菜")
# print("做饭")
# print("吃饭")
# print("收拾碗筷")

# count = 1
# while count<=3:
#     print("洗菜")
#     print("做饭")
#     print("吃饭")
#     print("收拾碗筷")
#     count+=1

# 改需求，早饭和中饭之间学Python，中饭和晚饭之间学java
# 循环无法解决代码块何时何地执行

# def 函数名([参数])：
# 	"""文档注释：描述函数的作用"""
# 	函数中的代码
# 	[return ]
print("start")
def eat():
    """这是实现吃饭的功能"""
    print("洗菜")
    print("做饭")
    print("吃饭")
    print("收拾碗筷")
#调用函数
eat()
# eat()
print("finish")

#带参数，不带返回值得函数  输出两个数的和