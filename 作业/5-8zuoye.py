# 1.
# 发表文章升级练习
# 需求：增加人类，使用人对象发表文章
#

# 发表文章练习
"""
文章有标题，作者，内容，可以保存，数据保存在类属性中
数据类型：可以保存数据
文章类型：
    属性：标题，作者，内容
    方法：保存
人类:
    属性：姓名，年龄
"""


#
# class Database:
#     """数据类型"""
#     #保存文章的类属性
#     article_dict = {}
#
# class Article:
#     def __init__(self,title,author,content,name,age):
#         """实例属性初始化"""
#         self.title = title
#         self.author = author
#         self.content = content
#
#
#     def save(self):
#         """保存文章数据"""
#         #字典根据键保存值的方法  self是当前文章对象
#         Database.article_dict[self.title] = self
#
# class Person:
#     '''人的类型'''
#     def __init__(self,name,age):
#         '''属性初始化'''
#         self.name = name
#         self.age = age
#
#     def publish(self)
#         title = input("请输入文章标题：")
#         author = input("请输入文章作者：")
#         content = input("请输入文章内容：")
# #发表文章
# name = input('请输入姓名：')
# age = input('请输入年龄：')
#
#
# #创建文章对象
# article = Article(title, author, content,name,age,)
# article1 = Person(name,age)
# #保存文章
# article.save()
#
# #查看文章数据
# for title,article in Database.article_dict.items():
#     print(f"标题：{title}\n作者：{name}\n年龄：{age}\n文章内容：{article.content}")
# #
# # 2.
# 搬家具规则：
# 1.家具分不同的类型，并占用不同的面积
# 2.输出家具信息时，显示家具的类型和家具占用的面积
# 3.房子有自己的地址和占用的面积
# 4.房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
# 5.输出房子信息时，可以显示房子的地址、占地面积、剩余面积
#
# 家具类：
#     属性：类型，占用面积
#     方法：打印方法
# 房子类:
#     属性：地址，占用面积，剩余面积
#     方法：添加家具，打印方法
# 如：沙发8平米，南沙金州房子40平米
# 房子添加沙发，添加成功，房子在金州，占地面积40平米，剩余面积32平米
class Furniture:
    '''沙发类型'''

    def __init__(self, sofa, sofa_size):
        '''属性初始化'''
        self.sofa = sofa
        self.sofa_size = sofa_size

    def __str__(self):
        return f'{sofa}占用面积，{sofa_size}'

class House:
    '''房子类型'''

    def __init__(self, address, house_size):
        '''属性初始化'''
        self.address = address
        self.house_size = house_size

    def r(self, house_size, sofa_size):
        num1 = float(house_size)
        num2 = float(sofa_size)
        res = float(num1)- float(num2)
    def __str__(self):
        return (f'房子添加:{sofa}，\n添加{sofa}成功，\n房子在{address}，\n占地面积{house_size}平方，\n剩余面积{res}平方')


sofa = input('请输入添加物品名称:')
sofa_size = input('请输入沙发大小：')
house_size = input('请输入房子大小：')
address = input('请输入地址：')



