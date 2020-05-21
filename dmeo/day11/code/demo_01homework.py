# 1.
# 发表文章升级练习
# 需求：增加人类，使用人对象发表文章

class Database:
    """数据类型"""
    #保存文章的类属性
    article_dict = {}

class Person:
    """人物类型"""
    def __init__(self,name,age,nickname):
        """记录人物属性"""
        self.name = name
        self.age = age
        self.nickname = nickname

    def publish(self):
        # 发表文章
        title = input("请输入文章标题：")
        content = input("请输入文章内容：")
        #创建文章对象
        article = Article(title,self,content)
        article.save()

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

# per1 = Person("张伟强",20,"强哥")
# per1.publish()
# #查看文章数据
# for title,article in Database.article_dict.items():
#     print(f"标题：{title}\n作者：{article.author.nickname}\n文章内容：{article.content}")

# 2.
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
    """家具类"""
    def __init__(self,type,area):
        """记录家具类型和占用面积"""
        self.type = type
        self.area = area

    def __str__(self):
        return f"{self.type}占用的面积是{self.area}平米"

class House:
    """房子类型"""
    def __init__(self,address,area):
        """记录房子的地址，占地面积"""
        self.address = address #房子地址
        self.total_area = area  #房子总面积
        self.free_area = area #房子剩余面积

    def add_fur(self,fur):#传递一个家具对象进来
        """添加家具方法"""
        if self.free_area>fur.area: #房子的剩余面积大于家具面积
            print(f"{fur.type}添加成功！")
            self.free_area-=fur.area #剩余面积减去家具面积
        else:
            print(f"{fur.type}添加失败！")

    def __str__(self):
        return f"房子的地址:{self.address}、占地面积:{self.total_area}平米" \
               f"、剩余面积:{self.free_area}平米"

fur1 = Furniture("沙发",8)
print(fur1)
house1 = House("金州",40)
print(house1)
#房子添加家具
house1.add_fur(fur1)
house1.add_fur(fur1)
house1.add_fur(fur1)
house1.add_fur(fur1)
house1.add_fur(fur1)
print(house1)