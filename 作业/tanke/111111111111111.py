"""
项目名称：坦克1.0
开发人员：刘江
开发时间：2020-05-13
"""
import random
import pygame
import time
import sys

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
ENEMY_TANK_COUNT = 10


# 主逻辑类
class MainGame:
    # 游戏主窗口
    window = None
    # 记录我方坦克
    P1 = None
    # 记录敌方坦克
    enemy_tank_list = []
    # 记录我方坦克发射子弹
    bullet_hero_list = []
    # 记录敌方坦克发射子弹
    bullet_enemy_list = []
    # 记录爆炸效果
    bomb_list = []
    # 记录墙壁列表
    wall_list = []

    def create_enemy_tank(self):
        """创建敌方坦克"""
        for i in range(ENEMY_TANK_COUNT):
            # 随机敌方坦克
            e_tank = EnemyTank(random.randint(0, 8) * 100, 100)
            # 创建敌方坦克后添加到主逻辑的敌方坦克列表中
            MainGame.enemy_tank_list.append(e_tank)

    def load_enemy_tank(self):
        """加载敌方坦克"""
        # 获取敌方坦克对象
        for e_tank in MainGame.enemy_tank_list:
            # 判断是否活着
            if e_tank.live:
                # 活着贴图
                e_tank.display_tank()
                # 让坦克移动
                e_tank.move()
                # 敌方坦克发射子弹
                e_tank.shot()
                # 调用撞墙的方法
                e_tank.hit_wall()
            else:
                MainGame.enemy_tank_list.remove(e_tank)

    def create_hero_tank(self):
        """创建我方坦克"""
        # 判段是否创建我方坦克
        if not MainGame.P1:
            MainGame.P1 = HeroTank(450, 600)

    def load_heor_tank(self):
        """加载我方坦克"""
        if MainGame.P1 and MainGame.P1.live:
            # 如果坦克活着就调用坦克贴图的方法
            MainGame.P1.display_tank()
            MainGame.P1.move()
            # 调用我方坦克撞墙
            MainGame.P1.hit_wall()
        else:
            # 删除坦克对象
            del MainGame.P1
            MainGame.P1 = None

    def load_bullet_hero(self):
        """加载我方子弹"""
        for b in MainGame.bullet_hero_list:
            # 判断子弹是否活着
            if b.live:
                # 贴子弹图片
                b.display_bullet()
                # 调用子弹移动方法
                b.move()
                # 调用子弹碰撞敌方坦克
                b.hit_enemy_tank()
                # 调用撞墙方法
                b.hit_wall()
            else:
                MainGame.bullet_hero_list.remove(b)

    def load_bullet_enemy(self):
        """加载敌方子弹"""
        # 取出子弹
        for b in MainGame.bullet_enemy_list:
            if b.live:
                b.display_bullet()
                b.move()
                if MainGame.P1 and MainGame.P1.live:
                    b.hit_haro_tank()  # 调用子弹碰撞我方坦克方法
                b.hit_wall()
            else:
                MainGame.bullet_enemy_list.remove(b)

    def load_bomb(self):
        """加载爆炸效果"""
        for bomb in MainGame.bomb_list:
            if bomb.live:
                bomb.display_bomb()
            else:
                MainGame.bomb_list.remove(bomb)

    def carate_wall(self):
        """创建墙壁"""
        for i in range(9):
            wall = Wall(i * 90, 500)
            MainGame.wall_list.append(wall)

    def load_wall(self):
        """加载墙壁方法"""
        for wall in MainGame.wall_list:
            if wall.hp > 0:
                wall.display_wall()
            else:
                MainGame.wall_list.remove(wall)

    def start(self):
        """开始游戏"""
        # 调用窗口初始化
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置窗口标题
        pygame.display.set_caption("坦克1.0")
        # 调用坦克
        self.create_hero_tank()
        # 调用敌方坦克
        self.create_enemy_tank()
        # 调用墙壁
        self.carate_wall()

        while True:
            # 窗口颜色
            MainGame.window.fill((0, 0, 0))
            self.deal_event()
            # 调用坦克贴图的方法
            self.load_heor_tank()
            # 调用加载敌方坦克方法
            self.load_enemy_tank()
            # 调用加载我方子弹的方法
            self.load_bullet_hero()
            # 调用加载敌方子弹的方法
            self.load_bullet_enemy()
            # 加载敌方子弹
            self.load_bomb()
            # 调用爆炸效果
            self.load_wall()
            # 调用加载墙壁的方法
            if not MainGame.P1:
                self.game_over()
            # 刷新
            pygame.display.update()
            time.sleep(0.1)

    def deal_event(self):
        '''事件检测'''
        # print(pygame.event.get())
        # 获取新事件
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 键盘按下事件
                # print('按下键盘')
                if event.key == pygame.K_LEFT:
                    print('左移')
                elif event.key == pygame.K_RIGHT:
                    print('右移')
                elif event.key == pygame.K_DOWN:
                    print('下移')
                elif event.key == pygame.K_UP:
                    print('上移')
                elif event.key == pygame.K_SPACE:
                    # print('发射子弹')
                    if MainGame.P1 and MainGame.P1.live:
                        if len(MainGame.bullet_hero_list) < 4:
                            # 创建子弹对象添加到我方子弹列表
                            bullet = MainGame.P1.shot()
                            MainGame.bullet_hero_list.append(bullet)
                        else:
                            print('一次只能发射4颗子弹')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('鼠标点击事件')

    def game_over(self):
        '''游戏结束'''
        MainGame.window.biit(pygame.image.load('tank_img/over.gif'), (450, 350))


# 基本坦克类
class BasicTank:
    def __init__(self, x, y):
        """基本坦克类的属性"""
        # 加载图片文件，返回图片对象
        self.images = {
            'U': pygame.image.load('tank_img/p1tankU.gif'),
            'D': pygame.image.load('tank_img/p1tankD.gif'),
            'L': pygame.image.load('tank_img/p1tankL.gif'),
            'R': pygame.image.load('tank_img/p1tankR.gif'),
        }
        # 给坦克初始化一个方向
        self.direction = 'U'
        # 根据堂客方向获取图片
        self.image = self.images[self.direction]
        # 获取图片区域
        self.rect = self.image.get_rect()
        # 根据传入的参数，决定坦克位置
        self.rect.x = x
        self.rect.y = y
        # 移动速度
        self.speed = 30
        # 是否活着
        self.live = True

    def display_tank(self):
        """坦克图片的方法"""
        # 获取图片
        self.image = self.images[self.direction]
        # 贴图（指定坐标，将图片绘制到窗口）
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        # 坦克移动
        if self.direction == 'U':  # 坦克的方向
            if self.rect.y > 0:  # 坦克的y坐标在边界内
                self.rect.y -= self.speed
        elif self.direction == 'D':  # 坦克的方向
            if self.rect.y < SCREEN_HEIGHT - self.rect.height:  # 坦克的y坐标在边界内
                self.rect.y += self.speed
        elif self.direction == 'L':  # 坦克的方向
            if self.rect.x > 0:  # 坦克的y坐标在边界内
                self.rect.x -= self.speed
        elif self.direction == 'R':  # 坦克的方向
            if self.rect.x < SCREEN_WIDTH - self.rect.height:  # 坦克的y坐标在边界内
                self.rect.x += self.speed

    def back(self):
        """坐标还原"""
        self.rect.x = self.oldx
        self.rect.y = self.oldy

    def hit_wall(self):
        """坦克撞墙"""
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                self.back()

    def shot(self):
        bullet = Bullet(self)
        return bullet


# 我方坦克类
class HeroTank(BasicTank):
    def __init__(self, x, y):
        super(HeroTank, self).__init__(x, y)
        self.speed = 2

    def move(self):
        """我方坦克移动"""
        # 键盘长安事件，获取键盘所有按键状态，按下1，没按0
        keys_status = pygame.key.get_pressed()
        if keys_status[pygame.K_UP]:  # 按键“上”被按下
            self.direction = 'U'  # 修改方向属性
            super(HeroTank, self).move()  # 调用父类中移动方法
        elif keys_status[pygame.K_DOWN]:
            self.direction = 'D'
            super(HeroTank, self).move()
        elif keys_status[pygame.K_LEFT]:
            self.direction = 'L'
            super(HeroTank, self).move()
        elif keys_status[pygame.K_RIGHT]:
            self.direction = 'R'
            super(HeroTank, self).move()


# 敌方坦克类
class EnemyTank(BasicTank):
    def __init__(self, x, y):
        super(EnemyTank, self).__init__(x, y)
        # 储存敌方坦克图片到字典中
        self.images = {
            'U': pygame.image.load('tank_img/enemy1U.gif'),
            'D': pygame.image.load('tank_img/enemy1D.gif'),
            'L': pygame.image.load('tank_img/enemy1L.gif'),
            'R': pygame.image.load('tank_img/enemy1R.gif'),
        }
        # "随机方向"
        self.direction = self.random_direction()
        # 取出对应图片
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(1, 2)
        # 记录步数
        self.step = 50
        # 发射子弹计数器
        self.count = 1

    def random_direction(self):
        directons = ["U", "D", "L", "R"]
        return random.choice(directons)

    def move(self):
        """敌方坦克移动"""
        if self.speed > 0:
            super(EnemyTank, self).move()
            self.speed -= 1
        else:
            # 重新生成方向
            self.direction = self.random_direction()
            # self.step = 50
            self.step = (5 - self.speed) * random.randint(40, 60)

    def shot(self):
        self.count += 1
        if self.count == 200:
            b = super(EnemyTank, self).shot()
            MainGame.bullet_enemy_list.append(b)
            self.count = 1


# 子弹类
class Bullet:
    def __init__(self, tank):
        # 子弹单图片
        self.image = pygame.image.load('tank_img/tankmissile.gif')
        # 是否活着
        self.live = True
        # 移动速度
        self.speed = 25
        # 方向
        self.direction = tank.direction
        # 设置子弹位置
        self.rect = self.image.get_rect()
        # 子弹中心
        self.rect.x = tank.rect.centerx - self.rect.width // 2
        self.rect.y = tank.rect.centery - self.rect.height // 2

    def display_bullet(self):
        """子弹贴图"""
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        """子弹的移动方法"""
        # 子弹方向向上移动
        if self.direction == 'U':
            # 子弹在边界内正常移动，超出不移动
            if self.rect.centery > -self.rect.height // 2:
                self.rect.centery -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            # 子弹在边界内正常移动，超出不移动
            if self.rect.centery < SCREEN_HEIGHT + self.rect.height // 2:
                self.rect.centery += self.speed
            else:
                self.live = False

        elif self.direction == 'L':
            # 子弹在边界内正常移动，超出不移动
            if self.rect.centerx > self.rect.width:
                self.rect.centerx -= self.speed
            else:
                self.live = False

        elif self.direction == 'R':
            # 子弹在边界内正常移动，超出不移动
            if self.rect.centerx < SCREEN_WIDTH + self.rect.width // 2:
                self.rect.centerx += self.speed
            else:
                self.live = False

    def hit_enemy_tank(self):
        # 我方子弹是否打中敌方坦克
        # 创建子弹和敌方每一辆坦克的碰撞检测
        for e_tank in MainGame.enemy_tank_list:
            # 进行一对一的冲突检测
            if pygame.sprite.collide_rect(self, e_tank):
                # 修改子弹坦克的生存属性
                self.live = False
                e_tank.live = False
                # 创建爆炸效果对象
                bomb = Bomb(e_tank)
                MainGame.bomb_list.append(bomb)

    def hit_hero_tank(self):
        # 敌方坦克是否打中我方坦克
        if pygame.sprite.collide_rect(self, MainGame.P1):
            self.live = False
            MainGame.P1.live = False
            # 创建爆炸效果
            bomb = Bomb(MainGame.P1)
            MainGame.bomb_list.append(bomb)

    def hit_wall(self):
        """子弹碰撞墙体方法"""
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                self.live = False
                wall.hp -= 1

    def __del__(self):
        print('子弹被删除')


# 墙壁类
class Wall:
    def __init__(self, x, y):
        self.image = pygame.image.load('tank_img/walls.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 5

    def display_wall(self):
        MainGame.window.blit(self.image, self.rect)


# 爆炸类
class Bomb:
    def __init__(self, tank):
        self.images = [
            pygame.image.load("tank_img/blast0.gif"),
            pygame.image.load("tank_img/blast1.gif"),
            pygame.image.load("tank_img/blast2.gif"),
            pygame.image.load("tank_img/blast3.gif"),
            pygame.image.load("tank_img/blast4.gif"),
            # pygame.image.load("tank_img/blast5.gif"),
            # pygame.image.load("tank_img/blast6.gif"),
            # pygame.image.load("tank_img/blast7.gif")
        ]
        # 根据索引取爆炸图片
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = tank.rect
        self.live = True

    def display_bomb(self):
        '''贴爆炸图'''
        if self.image_index < len(self.images):
            self.image = self.images[self.image_index]
            MainGame.window.blit(self.image, self.rect)
            self.image_index += 1
        else:
            self.live = False
            self.image_index = 0


m = MainGame()
m.start()
