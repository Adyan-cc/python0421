
# num = 5
# def func(name,age):
#     num1 = 10
#     ret = locals()
#     print(ret)
# func("张伟强",20)
# ret = globals()
# print(ret)

# 命名空间加载顺序:内置->全局-->局部
# print("hello world")
# name = "张伟强"
# # print(name)
# def func():
#     name = "张威"
#     print(name)

# 命名空间查找顺序：局部-->全局-->内置
# name = "张伟强"
# id = 3
# def func2():
#     # id = 10
#     print(id)
# func2()

#嵌套函数：当前函数-->父函数-->全局-->内置
# id = 10
def func1():
    # id = 20
    def func2():
        # id = 30
        print(id)
    func2()
func1()