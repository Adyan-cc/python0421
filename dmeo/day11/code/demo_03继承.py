

class Vehicle:
    """交通工具"""
    def __init__(self,brand):
        self.brand = brand

    def move(self):
        """移动的方法"""
        print(f"{self.brand}开始移动")

class Plane(Vehicle):
    """飞机类型"""
    def move(self):
        """移动的方法"""
        print("飞机快速飞行中。。")

plane = Plane("波音747")
plane.move()


# # 继承可以隔代
# class Animal:
#     def eat(self):
#         print("吃东西")
#
# class Dog(Animal):
#     # def eat(self):
#     #     print("吃骨头")
#     pass
#
# class Hsq(Dog):
#     pass
#
# hsq = Hsq()
# # hsq.eat()
# #查看继承的父类
# print(Hsq.__base__) #<class '__main__.Dog'>
# print(Dog.__base__) #<class '__main__.Animal'>
# print(Animal.__base__) #<class 'object'>




# super()方法**
# - 子类和父类有相同的方法，如果子类想调用父类相同的方法，可以使用super()方法
# 坦克大战
# 敌方坦克和我方坦克开火方法类似但又不完全相同
# 把相同属性和方法定义在基本坦克类中，我方和敌方坦克继承基本坦克类
# 把不同的代码写在自己的开火方法中，调用自己开发方法中再调用父类开火方法

# class BaseTank:
#     """基本坦克类型"""
#     def fire(self):
#         """开火方法"""
#         print("坦克开火了，发射子弹（15行代码）")
#
# class HeroTank(BaseTank):
#     """英雄坦克类型"""
#     def fire(self):
#         """子类中有自己开火技能"""
#         print("英雄坦克，按下空格键，发射子弹(5行代码)")
#         #服用父类中发射子弹的代码
#         # BaseTank.fire(self)           #1.父类名.方法名(self)
#         # super(HeroTank, self).fire()  #2.super(当前类名,self).方法名()
#         super().fire()                  #3.super().fire()
#
# class EnemyTank(BaseTank):
#     """敌方坦克类型"""
#     def fire(self):
#         """子类中有自己开火技能"""
#         print("敌方坦克，随机发射子弹(7行代码)")
#         #服用父类中发射子弹的代码
#         BaseTank.fire(self)
#
# hero_tank = HeroTank()
# hero_tank.fire()
#
# enemy_tank = EnemyTank()
# enemy_tank.fire()


# **多继承**
# - 一个子类可以继承多个父类，就是多继承，并且拥有父类的属性和方法。例如：孩子可以继承父亲和母亲的特征
# - 如果子类和父类有相同的方法，就会调用子类的方法
#   - 思考：如果不同的父类存在着相同的方法，子类对象调用父类的时候，会调用哪个父类的方法？

# class Dog:
#     """狗的类型"""
#     def eat(self):
#         """吃的方法"""
#         print("吃粑粑")
# class God:
#     """神仙的类型"""
#     def eat(self):
#         """吃的方法"""
#         print("吃蟠桃")
#
# class Xtq(God,Dog):
#     """神仙狗类"""
#     pass
# xtq = Xtq()
# xtq.eat()
# print(Xtq.mro())



#多继承案例
# class A:
#     def func(self):
#         print("--A--")
#
# class B(A):
#     # def func(self):
#     #     print("--B--")
#     pass
#
# class C(A):
#     def func(self):
#         print("--C--")
# class D(B,C):
#     # def func(self):
#     #     print("--D--")
#     pass
#
# d = D()
# d.func()

# class A:
#     def func(self):
#         print("--A--")
# class B(A):
#     def func(self):
#         super(B, self).func()
#         print("--B--")
# class C(A):
#     def func(self):
#         super(C, self).func()
#         print("--C--")
# class D(B,C):
#     def func(self):
#         super(D, self).func()
#         print("--D--")
# d = D() #继承顺序 D-->B-->C-->A
# d.func()
# print(D.mro())


# __init__()`方法
#
# - 子类继承父类，如果子类不复写父类的`__init__()`方法，创建子类会自动调用父类的`__init__()`方法
# - 子类继承父类，如果子类复写了父类的`__init__()`方法，创建子类对象的时候不会再调用父类的`__init__()`方法

# #猫类和其他宠物类相比，有自己属性，昵称
# class Pet:
#     """宠物类型"""
#     def __init__(self,age):
#         """宠物初始化"""
#         self.age = age
#
#     def __str__(self):
#         return str(self.age)
#
# class Cat(Pet):
#     """猫类"""
#     def __init__(self,nickname,age):
#         super(Cat, self).__init__(age)
#         self.nickname = nickname
#
#     def __str__(self):
#         return f"{self.nickname},{self.age}"
# cat1 = Cat("tom",3)
# print(cat1)


# - 宠物类
#   - 属性：名字，健康值
#   - 方法：恢复健康
# - 医院类
#   - 属性：医院名称
#   - 方法：治疗宠物(调用宠物自我恢复的方法)
# - 狗类：继承宠物类
# - 猫类：继承宠物类

import time
class Pet:
    """宠物类"""
    def __init__(self,name,health):
        self.name = name #昵称
        self.health = health  #健康状态，小于60生病

    def recovery(self):
        """恢复健康的行为"""
        while self.health<60:
            self.health+=5
            print(f"{self.name}正在快速恢复中...")
            time.sleep(1)

    def __str__(self):
        return f"{self.name}的健康值是：{self.health}"

# class Hospital:
#     """医院类"""
#     def __init__(self,name):
#         self.name = name
#
#     def care(self,pet):
#         if isinstance(pet,Pet):
#             print(f"开始治疗{pet.name}")
#             pet.recovery()
#         else:
#             print("宠物医院只接受宠物治疗")



# class Cat(Pet):
#     """猫类"""
#     pass
#
# class Dog(Pet):
#     """狗类"""
#     pass
#
# class Person:
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
#
#     def recovery(self):
#         """恢复健康的行为"""
#         while self.health<60:
#             self.health+=5
#             print(f"{self.name}正在快速恢复中...")
#             time.sleep(1)

# cat1 = Cat("Tom",40)
# hospital = Hospital("南沙中心医院")
# hospital.care(cat1)
# print(cat1)

#宠物医院治疗人
# per1 = Person("小张",30)
# hospital.care(per1)

#使用isinstance可以判断对象是否是类的实例
# isinstance(对象，类)
#可以判断数据类型
# a = [1]
# print(isinstance(a,list))
# print(isinstance(a,str))





#抽象类
import abc
class Person(metaclass=abc.ABCMeta):
    """这是一个抽象类，不能实例化"""
    @abc.abstractmethod
    def eat(self):
        """这是一个抽象方法，子类必须实现"""
        print("吃饭")

    def breath(self):
        """这是普通方法"""
        print("呼吸")

class Student(Person):
    """学生类"""

    def eat(self):
        print("吃食堂")

    def sleep(self):
        print("睡宿舍")

stu = Student()
stu.sleep()
stu.eat()
stu.breath()