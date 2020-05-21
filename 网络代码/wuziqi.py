# coding=gbk
import pygame  # ����pygame��Ϸģ��
import time
import sys
from pygame.locals import *

initChessList = []  # ���������������
initRole = 1  # 1��������壻 2���������
resultFlag = 0  # �����־

class StornPoint():
    def __init__(self ,x ,y ,value):
        '''
        :param x: ����x������
        :param y: ����y������
        :param value: ��ǰ���������ӣ�0:û������ 1:���� 2:����
        '''
        self.x = x  # ��ʼ����Ա����
        self.y = y
        self.value = value

def initChessSquare(x ,y):  # ��ʼ������
    for i in range(15):       # ÿһ�еĽ��������
        rowlist = []
        for j in range(15):   # ÿһ�еĽ��������
            pointX = x+ j * 40
            pointY = y + i * 40
            sp = StornPoint(pointX, pointY, 0)
            rowlist.append(sp)
        initChessList.append(rowlist)


def eventHander():  # ���������¼�
    for event in pygame.event.get():
        global initRole
        if event.type == QUIT:  # �¼�����Ϊ�˳�ʱ
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:  # ��������ʱ
            x, y = pygame.mouse.get_pos()  # ��ȡ�������λ������
            i = 0
            j = 0
            for temp in initChessList:
                for point in temp:
                    if x >= point.x - 10 and x <= point.x + 10 and y >= point.y - 10 and y <= point.y + 10:
                        if point.value == 0 and initRole == 1:  # ������λ��Ϊ�գ���������Ϊ����
                            point.value = 1  # �����ʱ������Ϊ����
                            judgeResult(i, j, 1)
                            initRole = 2  # �л���ɫ
                        elif point.value == 0 and initRole == 2:  # ������λ��Ϊ�գ���������Ϊ����
                            point.value = 2  # �����ʱ������Ϊ����
                            judgeResult(i, j, 2)
                            initRole = 1  # �л���ɫ
                        break
                    j += 1
                i += 1
                j = 0


def judgeResult(i, j, value):  # �����ж�
    global resultFlag
    flag = False
    for x in range(j - 4, j + 5):  # ������û�г���5�����ڱ�Ե������һ�������Ƿ�������ӵ�����һ����
        if x >= 0 and x + 4 < 15:
            if initChessList[i][x].value == value and \
                    initChessList[i][x + 1].value == value and \
                    initChessList[i][x + 2].value == value and \
                    initChessList[i][x + 3].value == value and \
                    initChessList[i][x + 4].value == value:
                flag = True
                break
                pass
    for x in range(i - 4, i + 5):  # ������û�г���5�����ڱ�Ե������һ�������Ƿ�������ӵ�����һ����
        if x >= 0 and x + 4 < 15:
            if initChessList[x][j].value == value and \
                    initChessList[x + 1][j].value == value and \
                    initChessList[x + 2][j].value == value and \
                    initChessList[x + 3][j].value == value and \
                    initChessList[x + 4][j].value == value:
                flag = True
                break
                pass

    # ���ж϶�������ĶԽ�����Ӯ x ���ᣬ y������ �� i ���� j ���У���б�򣩣��ڱ�Ե������һ�������Ƿ�������ӵ�����һ����
    for x, y in zip(range(j + 4, j - 5, -1), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y - 1][x + 1].value == value and \
                    initChessList[y - 2][x + 2].value == value and \
                    initChessList[y - 3][x + 3].value == value and \
                    initChessList[y - 4][x + 4].value == value:
                flag = True

    # 2���ж���������ĶԽ�����Ӯ x ���ᣬ y������ �� i ���� j ���У���б�򣩣��ڱ�Ե������һ�������Ƿ�������ӵ�����һ����
    for x, y in zip(range(j - 4, j + 5), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y + 1][x + 1].value == value and \
                    initChessList[y + 2][x + 2].value == value and \
                    initChessList[y + 3][x + 3].value == value and \
                    initChessList[y + 4][x + 4].value == value:
                flag = True

    if flag:  # �������������֤����������
        resultFlag = value  # ��ȡ������������ɫ
        print("����Ӯ" if value == 1 else "����Ӯ")


# �����ز�
def main():
    global initChessList, resultFlag
    initChessSquare(27, 27)
    pygame.init()  # ��ʼ����Ϸ����
    screen = pygame.display.set_mode((620, 620), 0, 0)  # ������Ϸ���� # ��һ��������Ԫ�飺���ڵĳ��Ϳ�
    pygame.display.set_caption("����er������")  # �����Ϸ����
    background = pygame.image.load("tank_img/asd.png")  # ���ر���ͼƬ
    whiteStorn = pygame.image.load("tank_img/blast4.gif")  # ���ذ���ͼƬ
    blackStorn = pygame.image.load("tank_img/blast4.gif")  # ���غ���ͼƬ
    resultStorn = pygame.image.load("tank_img/ewq.png")  # ���� Ӯ ʱ��ͼƬ
    rect = blackStorn.get_rect()

    while True:
        screen.blit(background, (0, 0))
        for temp in initChessList:
            for point in temp:
                if point.value == 1:  # ����������Ϊ1ʱ�����ư���
                    screen.blit(whiteStorn, (point.x - 18, point.y - 18))
                elif point.value == 2:  # ����������Ϊ2ʱ�����ƺ���
                    screen.blit(blackStorn, (point.x - 18, point.y - 18))

        if resultFlag > 0:
            initChessList = []  # �������
            initChessSquare(27, 27)  # ���³�ʼ������
            screen.blit(resultStorn, (200, 200))  # ���ƻ�ʤʱ��ͼƬ
        pygame.display.update()  # ������ͼ

        if resultFlag > 0:
            time.sleep(3)
            resultFlag = 0  # �ÿ�֮ǰ�Ļ�ʤ���
        eventHander()  # ����֮ǰ������¼�����


if __name__ == '__main__':
    main()  # �������������ƴ���
    pass
