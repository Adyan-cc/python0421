
#定义字典
#定义空字典
# dic = {}
# dic = dict()
# print(type(dic))
#定义非空字典
# dic = {"name":"许博宁","age":18}
# #字典根据键取值
# print(dic["name"])

#key必须是不可变类型
# dic = {"name":"许博宁","age":18,[1]:"a"}
# print(dic)
#字典中的键不可重复，重复会覆盖
# dic = {"name":"许博宁","age":18,"name":"陈星航"}
# print(dic)

# 字典方法(增删改查)
#
# - 增加
#   - 通过key添加value值，如果key存在，则覆盖  ，   字典[key] = value
# dic = {"name":"许博宁","age":18}
#增加地址信息
# dic["address"] = "广西"
# dic["age"] = 20
# setdefault(), 指定key和value，指定 key 和 value,如果 key 存在则不覆盖    字典.setdefault(key,value)
# dic.setdefault("address","广西")
# dic.setdefault("age",20)
# print(dic)


# 删除 pop() 弹出，返回并输出指定键对应的值   字典.pop(键)
# dic = {"name":"许博宁","age":18}
#删除年龄信息
# dic.pop("age")
# dic.popitem()
# dic.clear()
# del dic
# del dic["age"]
# print(dic)

# 通过key修改value值，如果**key存在，则覆盖**  ，   字典[key] = value
# dic = {"name":"许博宁","age":18}
#将年龄信息改为 20
# dic["age"] = 20
# update(),传递一个字典，如果key相同，则覆盖，没有key则添加    字典1.update(字典2)
#将字典2中的内容更新到字典1
# dic2 = {"age":20,"weight":70}
# dic.update(dic2)
# print(dic)

# - 根据 key 查找 通过指定的 key 找对应的值 dict[‘key’]
# - keys 包含字典所有 key 的 dict_keys 对象,该对象可以转换为列表
# - values 包含字典所有的 value 的 dict_keys 对象,该对象可以转换为列表
# - get 以键取值，如果指定键不存在，默认返回 None,可以指定返回内容
# -  items 返回字典键值呈元组形式的格式
# -  len 测量字典，键值对的个数（整体）
# dic = {"name":"许博宁","age":18}
# ret1 = list(dic.keys())
# ret2 = list(dic.values())
# print(ret1)
# print(ret2)
#以get方法取出年龄信息，取不到，默认20岁
# dic = {"name":"许博宁","age":18}
# # dic = {"name":"许博宁"}
# print(dic.get("age",20))

#取出所有的键和值
# dic = {"name":"许博宁","age":18}
# print(list(dic.items()))
# print(len(dic))

#遍历字典
# dic = {"name":"许博宁","age":18}
#遍历所有的键
# for k in dic.keys():
#     print(k)
#直接遍历字典，取出的是键
# for i in dic:
#     print(i)

#遍历所有的值
# for v in dic.values():
#     print(v)

#遍历键值对
# for k,v in dic.items():
#     print(k)
#     print(v)

#判断键是否在字典中  in
# if "age" in dic:
#     print(True)


#练习1：
dic = {'001':{"name":"许博宁","age":18,"address":"广西","score":80},
       '002':{"name":"梁少天","age":22,"address":"茂名","score":85},
       '003':{"name":"朱益锋","age":25,"address":"广东","score":90},
       '004':{"name":"马礼庆","age":12,"address":"广西","score":83}}
#输出字典003对应的所有的key，value
# print(dic["003"])
# for k,v in dic["003"].items():
#     print(k,v)
#给所有广西人加10000块住房补贴
# for v in dic.values():
#     if v["address"]=="广西":
#         v["butie"] = 10000
# for k,v in dic.items():
#     print(k,v)
#输出年龄最小的一组信息
# min_age = dic["001"]["age"]
# dic2 = {}
# for k,v in dic.items():
#     if min_age>=v["age"]:
#         min_age = v["age"]
#         dic2.clear()
#         dic2[k] = v
# print(min_age)
# print(dic2)

# #使用dict()将其他数据转换为字典
# # lst = [("name","许博宁"),("age",18)]
# # dic = dict(lst)
# dic = dict(name="许博宁",age=18)
# print(dic)

#字典排序
dic2 = {'a':1,'d':4,"b":2,'c':3}
#直接对字典排序，是对键排序
# ret = sorted(dic2)
#对字典的值进行排序，dic2.values()
ret = sorted(dic2.values())
print(ret)