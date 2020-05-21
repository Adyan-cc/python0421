

#将班级所有学员的成绩存储在列表中
score = [65,75,68,57,83,90,82]
#由于试卷题目出错，第3题有问题，所有学员+5分
# for i in range(len(score)):
#     score[i] = score[i]+5
# print(score)

# new_score = []
# for i in score:
#     new_score.append(i+5)
# print(new_score)

#使用推导式完成每个学员的分数+5分
# new_score = [i+5 for i in score ]
# print(new_score)

#练习1:
# lst = [1,2,3,4,5]
# #将列表中的每个元素平方后放入一个新列表
# new_lst = []
# for i in lst:
#     new_lst.append(i*i)
# # new_lst = [i**2 for i in lst]
# print(new_lst)

#练习2:
# lst = [1,2,3,4,5]
# #求出列表中是奇数的值，放入到一个新列表
# new_lst = [i for i in lst if i%2==1]
# print(new_lst)

#练习3:
# lst = [1,2,3,4,5]
#求出列表中所有大于2的偶数，平方后放入新列表
# new_lst = []
# for i in lst:
#     if i>2 and i%2==0:
#         num = i*i
#         new_lst.append(num)

# new_lst = [i*i for i in lst if i>2 if i%2==0]
# print(new_lst)

#练习4:
# lst = [[1,2,3],[4,5,6],[7,8,9]]
#转换为一维列表
# new_lst = []
# for i in lst:
#     for j in i:
#         new_lst.append(j)

# new_lst = [j for i in lst for j in i]
# print(new_lst)

#练习5:
# lst = [[1,2,3],[4,5,6],[7,8,9]]
#取出1,4,7
#取出1,5,9
# new_lst = [i[0] for i in lst]
# new_lst = [lst[i][i] for i in range(len(lst))]
# print(new_lst)

#练习6：
#使用列表推导式，生成0-100范围内的质数
# lst = []
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         lst.append(i)
# print(lst)

lst2 = []
for i in range(2,101):
    # lst = []
    # for j in range(2,i):
    #     if i%j==0:
    #         lst.append(j)
    lst = [j for j in range(2,i) if i%j==0]
    if lst==[]:
        lst2.append(i)
# print(lst2)
lst_zhishu = [i for i in range(2,101) if [j for j in range(2,i) if i%j==0]==[]]
print(lst_zhishu)