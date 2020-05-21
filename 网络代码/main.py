import pygame
from pygame.locals import *
from feijidazhan.plane import HeroPlane, EnemyPlane
import time


def start():#开始游戏
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 750), 0, 32)
    # 2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    #3. 创建一个飞机对象
    hero_plane = HeroPlane(screen)
    # 4. 创建一个敌人飞机
    enemy_plane = EnemyPlane(screen)
    # 5.把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        hero_plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()

        # 判断是否是点击了退出按钮
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    #控制飞机让其向左移动
                    hero_plane.move_Left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    # 控制飞机让其向右移动
                    hero_plane.move_Right()
                elif event.key == K_SPACE:
                    print('space')
                    hero_plane.launch_bullet()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)
        pygame.display.update()

if __name__=='__main__':
    start()