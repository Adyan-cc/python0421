

# x = 1
# y = 2
# z = 3
# if x:
#     a = y
# else:
#     a = z
# a = y if x else z
# print(a)

#比较a,b大小，将较大的值赋值给x
a = 3
b = 5
# if a<b:
#     x = b
# else:
#     x = a
# print(x)
x = a if a>b else b
print(x)