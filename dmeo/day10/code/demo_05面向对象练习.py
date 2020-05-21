

# 老张开车去东北
#
# ```
# 需求：发动车辆，输入姓名，车型，到达的目的地（面向过程）
# 定义车辆发动函数，驾驶函数，到达目的地函数
# ```
import time


def start():
    """驾驶员"""
    name = input("请输入姓名：")
    print("用户：",name)
    #调用车辆驾驶函数
    driver(name)

def driver(name):
    """驾驶"""
    car = input("请输入车的型号")
    print(f"{name}驾驶{car}，准备出发。。。")
    area = input("请输入要到达的目的地")
    #调用到达目的地函数
    run(area)

def run(area):
    """车行驶到达目的地"""
    for i in range(10):
        time.sleep(0.5)
        print("->",end='')
    print("经过跋山涉水，到达目的地",area)
# start()

# 面向对象开车
# 老张开车去东北
# """
# 人类
#     属性：姓名，年龄，性别
#     方法：开车 (传递一个车对象，直接调用车行驶的方法，不需要关系车是如何行驶的)
# 车类
#     属性：品牌，颜色
#     方法：行驶
# 地点类
#     属性：省市县
# """
class Person:
    """人的类型"""
    def __init__(self,name,age,gender):
        """属性初始化方法"""
        self.name = name
        self.age = age
        self.gender = gender

    def driver(self,car):
        """开车，人的行为"""
        print(f"{self.name}准备出发")
        #调用车对行驶的方法
        car.run("东北")

class Car:
    def __init__(self,brand,color):
        """属性初始化方法"""
        self.brand = brand
        self.color = color

    def run(self,area):
        print(f"{self.color}的{self.brand}发动了，准备去{area}")

# #创建出所有参数问题的对象
per1 = Person("老张",50,"男")
qirui = Car("瑞虎5x","灰色")
per1.driver(qirui)
#
# aodi = Car("奥迪A6","白色")
# per2 = Person("老王",45,"男")
# per2.driver(aodi)


#发表文章练习
"""
文章有标题，作者，内容，可以保存，数据保存在类属性中
数据类型：可以保存数据
文章类型：
    属性：标题，作者，内容
    方法：保存
"""

class Database:
    """数据类型"""
    #保存文章的类属性
    article_dict = {}

class Article:
    def __init__(self,title,author,content):
        """实例属性初始化"""
        self.title = title
        self.author = author
        self.content = content

    def save(self):
        """保存文章数据"""
        #字典根据键保存值的方法  self是当前文章对象
        Database.article_dict[self.title] = self

#发表文章
title = input("请输入文章标题：")
author = input("请输入文章作者：")
content = input("请输入文章内容：")

#创建文章对象
article = Article(title,author,content)
#保存文章
article.save()

#查看文章数据
for title,article in Database.article_dict.items():
    print(f"标题：{title}\n文章内容：{article.content}")