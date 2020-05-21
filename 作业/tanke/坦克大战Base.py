"""
项目：坦克大战
时间：2020-05-13
作者：徐广军
使用软件及版本：Pycharm python3.6 pygame1.9
"""
import pygame
import sys
# V6.3 全局判断
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 500
# 主逻辑类
class MainGame:

    # V2游戏主窗口
    window = None
    # V5.1记录我方坦克
    P1 = None

    def create_tank(self): # V5.2
        """创建我方坦克"""
        # v5.2判断我方坦克是否创建
        if not MainGame.P1:
            MainGame.P1 = HeroTank(500,400) # 坦克初始位置

    def load_heor_tank(self): # v5.3
        """加载我方坦克"""
        # v5.3如果坦克就调用坦克贴图的方法
        if MainGame.P1 and MainGame.P1.live:
            MainGame.P1.display_tank()
            MainGame.P1.move()
        else:
            # v5.3如果坦克死了，删除坦克对象，删除贴图
            del MainGame.P1
            MainGame.P1 = None # v5.3恢复坦克初始化设置

    def start(self): # V2
        """开始游戏"""
        # V2调用窗口初始化
        pygame.display.init()
        # V2创建窗口 set_mode("窗口宽，窗口高")          # V6.3
        MainGame.window = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        # V2设置窗口标题
        pygame.display.set_caption("坦克大战v_1.0")

        # v5.4 调用坦克创建的方法
        self.create_tank()
        while True :
            # V2设置窗口背景 fill() 设置颜色 RGB 这里设置黑色
            MainGame.window.fill((0,0,0))
            # V2调用时间检测事件
            self.deal_event()
            # v5.5调用坦克贴图方法
            self.load_heor_tank()
            # V2刷新显示
            pygame.display.update()

    def deal_event(self): # V3
        """事件检测"""
        # V3鼠标放上窗口和敲击键盘可以观察到位置信息反馈
        # print(pygame.event.get())
        # V3获取新事件
        for event in pygame.event.get():
            # V3.1 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                sys.exit()  # 关闭程序
            # V3.2 按下键盘检测
            elif event.type == pygame.KEYDOWN:
                # print("按下键盘")
                # V3.2按下键盘反馈数据
                if event.key == pygame.K_LEFT:
                    print("左移动")
                elif event.key == pygame.K_RIGHT:
                    print("右移动")
            # 3. 鼠标点击检测
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("鼠标点击事件")

    def game_over(self):
        """结束游戏"""

# 基本坦克类
class BaseTank: # V4

    def __init__(self,x,y):
        self.x = x
        self.y = y
        """
        基本坦克类的属性
        x，y：坦克初始在游戏窗口的位置
        """
        # V4.1.加载图片文件，返回图片对象
        # V4.1.将坦克图片存储在字典中
        self.images = {
            "U":pygame.image.load("tank_img/p1tankU.gif"),
            "D":pygame.image.load("tank_img/p1tankU.gif"),
            "L":pygame.image.load("tank_img/p1tankU.gif"),
            "R":pygame.image.load("tank_img/p1tankU.gif"),
        }

        # V4.2.给初始化坦克一个方向
        self.direction = "U"
        # V4.3.根据坦克方向获取坦克图片
        self.image = self.images[self.direction]
        # V4.4.获取图片矩形区域
        self.rect = self.image.get_rect()
        # V4.5.根据传入的参数，决定坦克的位置
        self.rect.x = x # 坦克的x坐标
        self.rect.y = y # 坦克的y坐标
        # V4.6.移动速度
        self.speed = 3
        # V4.7.是否活着
        self.live = True

    def display_tank(self):
        """坦克图片的贴图方法"""

        # V4.8.先获取坦克图片
        self.image = self.images[self.direction]
        # V4.9.贴坦克图片
        MainGame.window.blit(self.image,self.rect)

    def move(self):
        """坦克移动的方法"""
        # v6.1 判断坦克的方向 是否向上 向上处理
        if self.direction == "U":
            # v6.2 边界判断
            if self.rect.y > 0 :
                self.rect.y -= self.speed
        elif self.direction == "D":
            # v6.2 边界判断         #v6.4
            if self.rect.y < (SCREEN_HEIGHT-self.rect.height) :
                self.rect.y -= self.speed
        elif self.direction == "L":
            # v6.2 边界判断
            if self.rect.x > 0 :
                self.rect.x -= self.speed
        elif self.direction == "R":
            # v6.2 边界判断         #v6.4
            if self.rect.x < (SCREEN_WIDTH - self.rect.width) :
                self.rect.x -= self.speed
    # 在加载我方坦克调用坦克移动放马 MainGame.P1.move()
    # 此时坦克只能向上移动

# 我方坦克类
class HeroTank(BaseTank):
    # V4.10.继承基本坦克类
    def __init__(self,x,y):
        super(HeroTank,self).__init__(x,y)
        self.speed = 2

# 敌方坦克类
class EnemyTank:
    pass

# 子弹类
class Bullet:
    pass

# 墙壁类
class wall:
    pass

# 创建对象

start = MainGame()
# 对象开始游戏
start.start()
