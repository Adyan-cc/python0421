"""
项目名称：坦克大战v_1.0
开发人员：刘江
开发时间：2020-05-14
"""

import random
import pygame
import time
import sys

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
ENEMY_TANK_COUNT = 2000
pygame.init()


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
        # 创建多辆坦克
        for i in range(ENEMY_TANK_COUNT):
            # 随机敌方坦克的坐标
            e_tank = EnemyTank(random.randint(0, 8) * 100, 100)
            # 创建敌方坦克后添加到主逻辑的敌方坦克列表中
            MainGame.enemy_tank_list.append(e_tank)

    def load_enemy_tank(self):
        """加载敌方坦克"""
        # 获取每一辆敌方坦克对象
        for e_tank in MainGame.enemy_tank_list:
            # 判断坦克是否活着
            if e_tank.live:
                # 如果活着，贴坦克图片
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
        # 判断是否创建了我方坦克
        if not MainGame.P1:
            MainGame.P1 = HeroTank(450, 630)  # 坦克的初始位置

    def load_heor_tank(self):
        """加载我方坦克"""
        if MainGame.P1 and MainGame.P1.live:
            # 如果坦克活着就调用坦克贴图的方法
            MainGame.P1.display_tank()
            MainGame.P1.move()
            # 调用我方坦克是否撞墙方法
            MainGame.P1.hit_wall()
        else:
            # 如果坦克死了，就删除坦克对象
            del MainGame.P1
            MainGame.P1 = None

    def load_bullet_hero(self):
        """加载我方坦克发射的子弹"""
        # 取出每一颗子弹
        for b in MainGame.bullet_hero_list:
            # 判断子弹是否活着
            if b.live:
                # 贴子弹图片
                b.display_bullet()
                # 调用子弹移动的方法
                b.move()
                b.hit_enemy_tank()  # 调用子弹碰撞敌方坦克的方法
                b.hit_wall()  # 调用撞墙方法
            else:
                MainGame.bullet_hero_list.remove(b)
                # del b

    def load_bullet_enemy(self):
        """加载敌方子弹"""
        # 取出每一颗子弹
        for b in MainGame.bullet_enemy_list:
            if b.live:
                b.display_bullet()
                b.move()
                if MainGame.P1 and MainGame.P1.live:
                    b.hit_hero_tank()  # 调用子弹碰撞我方坦克方法
                b.hit_wall()
            else:
                MainGame.bullet_enemy_list.remove(b)

    def load_bomb(self):
        """加载爆炸效果的方法"""
        for bomb in MainGame.bomb_list:
            if bomb.live:
                bomb.display_bomb()
            else:
                MainGame.bomb_list.remove(bomb)

    def create_wall(self):
        """创建墙壁方法 墙壁60*60  窗口900"""
        for i in range(9):
            wall = Wall(i * 105, 500)
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
        pygame.display.set_caption("坦克大战v_1.0")
        # 调用创建坦克的方法
        self.create_hero_tank()
        # 调用创建敌方坦克的方法
        self.create_enemy_tank()
        # 调用创建墙壁的方法
        self.create_wall()
        # 调用音乐
        self.shiwang()

        while True:
            # 窗口背景颜色
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
            # 调用加载爆炸效果的方法
            self.load_bomb()
            # 调用加载墙壁的方法
            self.load_wall()
            if not MainGame.P1:
                self.game_over()

            # 刷新
            pygame.display.update()
            time.sleep(0.01)

    def deal_event(self):
        """事件检测"""
        # print(pygame.event.get())
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 键盘按下事件
                # print("按下键盘")
                if event.key == pygame.K_LEFT:
                    print("左移")
                elif event.key == pygame.K_RIGHT:
                    print("右移")
                elif event.key == pygame.K_SPACE:
                    # print("发射子弹")
                    if MainGame.P1 and MainGame.P1.live:
                        if len(MainGame.bullet_hero_list) < 30:
                            # 创建一个子弹对象，添加到我方子弹列表中
                            bullet = MainGame.P1.shot()
                            MainGame.bullet_hero_list.append(bullet)
                        else:
                            print("一次最多可以发射三颗子弹")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print("鼠标点击事件")
                pass

    def shiwang(self):
        pygame.mixer.music.load("tank_img/bg1.wav") # 背景
        pygame.mixer.music.play(-1)


    def game_over(self):
        """结束游戏"""
        pygame.mixer.music.stop()
        MainGame.window.blit(pygame.image.load("tank_img/over.gif"), (250, 200))


# - 基本坦克类
class BaseTank:
    def __init__(self, x, y):
        """基本坦克类的属性"""
        # 加载图片文件，返回图片对象
        # 将坦克图片储存在字典中
        self.images = {
            "U": pygame.image.load("tank_img/p1tankU.gif"),
            "D": pygame.image.load("tank_img/p1tankD.gif"),
            "L": pygame.image.load("tank_img/p1tankL.gif"),
            "R": pygame.image.load("tank_img/p1tankR.gif"),
        }
        # 给初始化坦克一个方向
        self.direction = "U"
        # 根据坦克方向获取坦克图片
        self.image = self.images[self.direction]
        # 获取图片矩形区域
        self.rect = self.image.get_rect()
        # 根据传入的参数，决定坦克的位置
        self.rect.x = x  # 坦克的x坐标
        self.rect.y = y  # 坦克的y坐标
        # 移动速度
        self.speed = 3
        # 是否活着
        self.live = True

    def display_tank(self):
        """贴坦克图片的方法"""
        # 先获取坦克图片
        self.image = self.images[self.direction]
        # 贴坦克图片
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        """坦克移动的方法"""
        if self.direction == "U":  # 坦克的方向
            if self.rect.y > 0:  # 坦克的y坐标在边界内就一直移动
                self.rect.y -= self.speed
        elif self.direction == "D":  # 坦克的方向
            if self.rect.y < SCREEN_HEIGHT - self.rect.height:  # 坦克的y坐标在边界内就一直移动
                self.rect.y += self.speed
        elif self.direction == "L":  # 坦克的方向
            if self.rect.x > 0:  # 坦克的x坐标在边界内就一直移动
                self.rect.x -= self.speed
        elif self.direction == "R":  # 坦克的方向
            if self.rect.x < SCREEN_WIDTH - self.rect.width:  # 坦克的x坐标在边界内就一直移动
                self.rect.x += self.speed

    def back(self):
        """坐标还原的方法"""
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


# - 我方坦克类
class HeroTank(BaseTank):
    def __init__(self, x, y):
        super(HeroTank, self).__init__(x, y)
        self.speed = 2

    def move(self):
        """我方坦克移动方法"""
        # 键盘长按事件，获取键盘上所有按键状态，按下1，没按0
        keys_status = pygame.key.get_pressed()
        # print(keys_status)
        if keys_status[pygame.K_UP]:  # 按键“上”被按下
            self.direction = "U"  # 修改方向属性
            super(HeroTank, self).move()  # 调用父类中移动方法
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
class EnemyTank(BaseTank):
    def __init__(self, x, y):
        super(EnemyTank, self).__init__(x, y)
        # 将敌方坦克图片储存在字典中
        self.images = {
            "U": pygame.image.load("tank_img/enemy1U.gif"),
            "D": pygame.image.load("tank_img/enemy1D.gif"),
            "L": pygame.image.load("tank_img/enemy1L.gif"),
            "R": pygame.image.load("tank_img/enemy1R.gif"),
        }
        # 随机方向
        self.direction = self.random_direction()
        # 根据方向取出对应的图片
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(1, 2)
        # 记录步数（每个方向走的步数）
        self.step = 50
        # 发射子弹的计算器
        self.count = 1

    def random_direction(self):
        directons = ["U", "D", "L", "R"]
        return random.choice(directons)

    def move(self):
        """敌方坦克移动"""
        if self.step > 0:
            super(EnemyTank, self).move()
            self.step -= 1
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


# - 子弹类
class Bullet:
    bgm_num =1
    def __init__(self, tank):
        # 图片
        self.image = pygame.image.load("tank_img/tankmissile.gif")
        # 是否活着
        self.live = True
        # 移动速度
        self.speed = 5
        # 子弹方向和坦克方向一致
        self.direction = tank.direction
        # 设置子弹位置
        self.rect = self.image.get_rect()
        self.rect.x = tank.rect.centerx - self.rect.width // 2  # 子弹中心就是坦克中心
        self.rect.y = tank.rect.centery - self.rect.height // 2

    def display_bullet(self):
        """子弹贴图方法"""
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        """子弹移动方法"""
        # 子弹方向朝上，应向上移动
        if self.direction == "U":
            # 在边界内，子弹正常移动，超出边界不移动
            if self.rect.centery > -self.rect.height // 2:
                self.rect.centery -= self.speed
            else:
                self.live = False
        elif self.direction == "D":
            # 在边界内，子弹正常移动，超出边界不移动
            if self.rect.centery < SCREEN_HEIGHT + self.rect.height // 2:
                self.rect.centery += self.speed
            else:
                self.live = False
        elif self.direction == "L":
            # 在边界内，子弹正常移动，超出边界不移动
            if self.rect.centerx > -self.rect.width:
                self.rect.centerx -= self.speed
            else:
                self.live = False
        elif self.direction == "R":
            # 在边界内，子弹正常移动，超出边界不移动
            if self.rect.centerx < SCREEN_WIDTH + self.rect.width // 2:
                self.rect.centerx += self.speed
            else:
                self.live = False

    # 我方子弹是否打中敌方坦克
    def hit_enemy_tank(self):
        # 将创建的子弹和每一辆敌方坦克进行碰撞检测
        for e_tank in MainGame.enemy_tank_list:
            # 进行一对一的冲突检测
            if pygame.sprite.collide_rect(self, e_tank):
                # 如果相撞，则修改子弹和敌方坦克的生存属性
                self.live = False
                e_tank.live = False
                # 创建爆炸效果对象，添加到爆炸效果列表中
                bomb = Bomb(e_tank)
                MainGame.bomb_list.append(bomb)



    # 敌方子弹是否打中我方坦克
    def hit_hero_tank(self):
        if pygame.sprite.collide_rect(self, MainGame.P1):
            # 如果相撞，则修改子弹和我方坦克的生存属性
            self.live = False
            MainGame.P1.live = False
            # 创建爆炸效果对象，添加到爆炸效果列表中
            bomb = Bomb(MainGame.P1)
            MainGame.bomb_list.append(bomb)
            pygame.mixer.music.load("tank_img/add.wav"),  # 死亡音乐
            pygame.mixer.music.play(-1)
            time.sleep(1)
    # 子弹和墙壁碰撞（子弹类中新增与墙壁的碰撞方法）
    def hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                self.live = False
                # 墙壁生命值减少
                wall.hp -= 1

    def __del__(self):
        print("子弹被删除")


# - 墙壁类
class Wall:
    def __init__(self, x, y):
        self.image = pygame.image.load("tank_img/walls.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 5

    def display_wall(self):
        MainGame.window.blit(self.image, self.rect)


# - 爆炸类
class Bomb:
    def __init__(self, tank):
        self.images = [
            pygame.image.load("tank_img/blast0.gif"),
            pygame.image.load("tank_img/blast1.gif"),
            pygame.image.load("tank_img/blast2.gif"),
            pygame.image.load("tank_img/blast3.gif"),
            pygame.image.load("tank_img/blast4.gif"),
            pygame.image.load("tank_img/blast5.gif"),
            pygame.image.load("tank_img/blast6.gif"),
            pygame.image.load("tank_img/blast7.gif")

        ]
        # 根据索引取爆炸图片
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = tank.rect
        self.live = True


    def display_bomb(self):
        """贴爆炸效果图"""
        if self.image_index < len(self.images):
            self.image = self.images[self.image_index]
            MainGame.window.blit(self.image, self.rect)
            self.image_index += 1
            pygame.mixer.music.load("tank_img/blast.wav")
            pygame.mixer.music.play(-1)
        else:
            self.live = False
            self.image_index = 0

# 音乐类
# class Music:
#     def __init__(self,add, blast, bg1):
#         self. = add
#
#     def music_background(self):
#         self.images = {
#
#             pygame.mixer.music.load("tank_img/blast.wav"),  # 爆炸音乐
#
#         }



game = MainGame()
game.start()
