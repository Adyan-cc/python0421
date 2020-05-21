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
  - 游戏应该在无限循环中"""

import pygame
import time

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
            #刷新
            pygame.display.update()

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