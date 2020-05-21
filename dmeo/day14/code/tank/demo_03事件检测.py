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
  
  
  """

import pygame
import time
import sys

class MainGame:
    #游戏主窗口
    window = None

    def start(self):
        """开始游戏"""
        # 调用窗口初始化
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((900,500))
        # 设置窗口标题
        pygame.display.set_caption("坦克大战v_1.0")
        while True:
            #窗口背景颜色
            MainGame.window.fill((0,0,0))
            self.deal_event()
            #刷新
            pygame.display.update()
            time.sleep(0.5)

    def deal_event(self):
        """事件检测"""
        # print(pygame.event.get())
        for event in pygame.event.get():
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("点击关闭窗口按钮")
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                # print("按下键盘")
                if event.key==pygame.K_LEFT:
                    print("左移")
                elif event.key==pygame.K_RIGHT:
                    print("右移")
            elif event.type==pygame.MOUSEBUTTONDOWN:
                print("鼠标点击事件")

    def game_over(self):
        """结束游戏"""
        pass

# - 基本坦克类
class BaseTank:
    pass

# - 我方坦克类
class HeroTank:
    pass

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