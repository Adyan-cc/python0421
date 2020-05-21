
#练习1：
#使用递归函数求10的阶乘
# 10!=10*9*8*..*1
# 10！= 10 * 9！
# 9！ = 9 * 8！
#。。。。
# 2！= 2* 1!
def jiecheng(n):
    """求n的阶乘"""
    if n==1:
        return 1
    return n * jiecheng(n-1)
ret = jiecheng(3)
# print(ret)
#练习2：
# 使用递归函数求100+98+96+。。。+10
# def sum_num(n):
#     if n==10:
#         return 10
#     return n+sum_num(n-2)
# ret = sum_num(14)
# print(ret)
#练习3：
#将如下列表转换为一维列表
lst = [1,2,[3,4,[5,6,[7,[8,9]]]]]
#[1,2,3,4,5,6,7,8,9]
#如果是整数，就加入新列表，如果是列表，继续遍历
new_lst = []
def func(lst):
    for i in lst:
        # if type(i)==list:
        # if not str(i).isdigit():
        # if str(i).startswith("["):
        if isinstance(i,list):
            func(i)
        else:
            new_lst.append(i)
func(lst)
print(new_lst)


