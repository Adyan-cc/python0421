"""
项目名称：坦克大战v_1.0
开发人员：
开发时间：2020-05-13
"""

# 实现框架的搭建(类的设计)

# - 主逻辑类
"""
- 属性：游戏主窗口
- 方法：开始游戏
  - 窗口初始化
  - 设置窗口
  - 设置标题(坦克大战v_1.0)
  - 窗口背景
  - 游戏应该在无限循环中

- 获取新事件
  - pygame.event.get():
    - 鼠标点击窗口事件 pygame.QUIT
    - 键盘按下事件 pygame.KEYDOWN
- 键盘长按事件
  - pygame.key.getpressed()

#### 我方坦克分析

- 由于我方坦克和敌方坦克有相似属性和方法，所以可以定义基本坦克类，让我方坦克和敌方坦克继承基本坦克类
- 基本坦克类：
  - 属性：图片、方向、图片矩形区域、坦克位置、移动速度、是否活着
  - 方法：移动、贴图
- 参考代码（定义基本坦克类，让我方坦克类继承）


创建我方坦克，并加载图片

- 在主逻辑中，一开始就存在我方坦克，定义P类属性记录
- 先定义创建我方坦克的方法(create_hero_tank),再定义加载坦克图片的方法(load_hero_tank)
- 在开始游戏时，调用创建坦克对象的方法，在循环中加载坦克图片

  """

import pygame
import time
import sys

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 900

class MainGame:
    # 游戏主窗口
    window = None
    #记录我方坦克
    P1 = None

    def create_tank(self):
        """创建我方坦克"""
        #判断是否创建了我方坦克
        if not MainGame.P1:
            MainGame.P1 = HeroTank(500,400) #坦克的初始位置

    def load_heor_tank(self):
        """加载我方坦克"""
        if MainGame.P1 and MainGame.P1.live:
            #如果坦克活着就调用坦克贴图的方法
            MainGame.P1.display_tank()
            MainGame.P1.move()
        else:
            #如果坦克死了，就删除坦克对象
            del MainGame.P1
            MainGame.P1 = None


    def start(self):
        """开始游戏"""
        # 调用窗口初始化
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置窗口标题
        pygame.display.set_caption("坦克大战v_1.0")
        #调用创建坦克的方法
        self.create_tank()
        while True:
            # 窗口背景颜色
            MainGame.window.fill((0, 0, 0))
            self.deal_event()
            #调用坦克贴图的方法
            self.load_heor_tank()
            # 刷新
            pygame.display.update()
            time.sleep(0.02)

    def deal_event(self):
        """事件检测"""
        # print(pygame.event.get())
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # print("按下键盘")
                if event.key == pygame.K_LEFT:
                    print("左移")
                elif event.key == pygame.K_RIGHT:
                    print("右移")
                elif event.key==pygame.K_SPACE:
                    print("发射子弹")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("鼠标点击事件")

    def game_over(self):
        """结束游戏"""
        pass


# - 基本坦克类
class BaseTank:
    def __init__(self,x,y):
        """基本坦克类的属性"""
        # 加载图片文件，返回图片对象
        #将坦克图片储存在字典中
        self.images = {
            "U":pygame.image.load("tank_img/p1tankU.gif"),
            "D":pygame.image.load("tank_img/p1tankD.gif"),
            "L":pygame.image.load("tank_img/p1tankL.gif"),
            "R":pygame.image.load("tank_img/p1tankR.gif"),
        }
        #给初始化坦克一个方向
        self.direction = "U"
        #根据坦克方向获取坦克图片
        self.image = self.images[self.direction]
        #获取图片矩形区域
        self.rect = self.image.get_rect()
        #根据传入的参数，决定坦克的位置
        self.rect.x = x #坦克的x坐标
        self.rect.y = y #坦克的y坐标
        #移动速度
        self.speed = 3
        #是否活着
        self.live = True

    def display_tank(self):
        """贴坦克图片的方法"""
        #先获取坦克图片
        self.image = self.images[self.direction]
        #贴坦克图片
        MainGame.window.blit(self.image,self.rect)

    def move(self):
        """坦克移动的方法"""
        if self.direction=="U": #坦克的方向
            if self.rect.y>0: #坦克的y坐标在边界内就一直移动
                self.rect.y -= self.speed
        elif self.direction=="D": #坦克的方向
            if self.rect.y<SCREEN_HEIGHT-self.rect.height: #坦克的y坐标在边界内就一直移动
                self.rect.y += self.speed
        elif self.direction=="L": #坦克的方向
            if self.rect.x>0: #坦克的x坐标在边界内就一直移动
                self.rect.x -= self.speed
        elif self.direction=="R": #坦克的方向
            if self.rect.x<SCREEN_WIDTH-self.rect.width: #坦克的x坐标在边界内就一直移动
                self.rect.x += self.speed


# - 我方坦克类
class HeroTank(BaseTank):
    def __init__(self,x,y):
        super(HeroTank, self).__init__(x,y)
        self.speed = 2

    def move(self):
        """我方坦克移动方法"""
        # 键盘长按事件，获取键盘上所有按键状态，按下1，没按0
        keys_status = pygame.key.get_pressed()
        # print(keys_status)
        if keys_status[pygame.K_UP]: #按键“上”被按下
            self.direction = "U" #修改方向属性
            super(HeroTank, self).move() #调用父类中移动方法
        elif keys_status[pygame.K_DOWN]:
            self.direction = "D"
            super(HeroTank, self).move()
        elif keys_status[pygame.K_LEFT]:
            self.direction = "L"
            super(HeroTank, self).move()
        elif keys_status[pygame.K_RIGHT]:
            self.direction = "R"
            super(HeroTank, self).move()

# - 敌方坦克类
class EnemyTank:
    pass


# - 子弹类
class Bullet:
    pass


# - 墙壁类
class Wall:
    pass


# - 爆炸类
class Bomb:
    pass


game = MainGame()
game.start()