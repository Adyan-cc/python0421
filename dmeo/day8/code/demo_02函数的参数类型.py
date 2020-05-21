
#不可变
# a = 1
# print(id(a))
# def func(b):
#     # print(id(b))
#     b = 10
#     print(id(b))
# func(a)
# print(a)

#可变
# lst = [10]
# print(id(lst))
# def func2(lst):
#     print(id(lst))
#     lst.append(20)
#     print(id(lst))
# func2(lst)
# print(id(lst))
# print(lst)


#练习
def func(name,lst=[]):
    lst.append(name)
    print(lst)
func("刘亦菲")
func("刘亦菲")
func("刘亦菲",[])
func("刘亦菲")
