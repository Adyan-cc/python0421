

import curses
from random import randrange, choice
from collections import defaultdict
#from itertools import chain
#ascll值列表
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']  #不区分大小写情况，全部包容，ord（）返回字符的十进制整数
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']#几个按键动作
actions_dict = dict(zip(letter_codes, actions * 2)) #将动作和ascll值打包成元组对

def get_user_action(keyboard):
    """得到用户的响应动作"""
    char = "N"
	#没有动作时一直等待
    while char not in actions_dict:
        char = keyboard.getch()
		#返回响应的按键
    return actions_dict[char]

def transpose(field):
    """矩阵转置"""
    return [list(row) for row in zip(*field)]

def invert(field):
    """矩阵逆转"""
    return [row[::-1] for row in field]

class GameField(object):
    """游戏场景"""
    def __init__(self, height=4, width=4, win=2048):
        """初始化游戏窗口"""
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        """重置游戏"""
		#记录最高分
        if self.score > self.highscore:
            self.highscore = self.score
		#分数清零
        self.score = 0
		#遍历游戏区域,给整个区域全部赋值0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
		#生成2或者4
        self.spawn()
        self.spawn()

    def move(self, direction):
        """移动时候的变化"""
        def move_row_left(row):
            def tighten(row): # squeese non-zero elements together
                """将行中的非零部分补足为0"""
				#不是0的数
                new_row = [i for i in row if i != 0]
				#准换列表  比如  4 0 0 2  转换成4 2 0 0
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row
			#row是一个列表
            def merge(row):
                """数字合并"""
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
						#这个位置数字变为原来2倍
                        new_row.append(2 * row[i])
						#记录得分值
                        self.score += 2 * row[i]
                        pair = False
                    else:
						#判断临近的值是否相同
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
		#四种移动情况全部包含
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:                              \
                transpose(moves['Left'](transpose(field)))  #将向上转成向左来看，哦同时对应的区域的数字也要转到左边来
        moves['Down']  = lambda field:                              \
                transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        """胜利检验"""
		#当游戏区域中有数字大于胜利条件，那么就返回true
        return any(any(i >= self.win_value for i in row) for row in self.field)
        #return max(chain(*self.field)) > self.win_value
    def is_gameover(self):
        """失败检验"""
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        """屏幕显示部分，绘制游戏界面"""
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            """屏幕上显示对应字符"""
            screen.addstr(string + '\n')

        def draw_hor_separator():
            """画分隔符"""
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
			#如果没有counter属性就加上
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
			#将行全部显示分隔符
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            """画列中的 |"""
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
		#清除屏幕
        screen.clear()
		#显示得分
        cast('SCORE: ' + str(self.score))
		#显示最高分
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))
		#画好有游戏区域的分隔符和数据行
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
		#画最底边分隔符
        draw_hor_separator()
		#游戏赢显示赢的字符
        if self.is_win():
            cast(win_string)
        else:
			#游戏输显示输的字符
            if self.is_gameover():
                cast(gameover_string)
            else:
				#显示提示（帮助）字符
                cast(help_string1)
		#显示帮助字符2
        cast(help_string2)

    def spawn(self):
        """生成2 或4 数字，并赋值于游戏区域中"""
        new_element = 4 if randrange(100) > 89 else 2
		#在游戏区域中随机定位一个没有数字的点
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
		#将2或4赋值于这个点
        self.field[i][j] = new_element

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            """如果最左侧为0而且最左侧中的第二个数不是0，或两个数相等，那么是可以移动的"""
            def change(i): # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0: # Move
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # Merge
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))#如果括号中的列表或者元组中的元素都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
        #将上下左右异动情况全部分析出来
        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](transpose(field))
		#如果点击对应的方向，那么就会有相应的动作
        if direction in check:
            return check[direction](self.field)
        else:
            return False

def main(stdscr):
	#几种状态
    def init():
        #1、 重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        #2、画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        #读取用户输入得到action，判断是重启游戏还是结束游戏w
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #3、画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = get_user_action(stdscr)
		#切换状态
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): # move successful
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

	#状态
    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }
	#颜色使用默认设置
    curses.use_default_colors()

    # 设置终结状态最大数值为 2048
    game_field = GameField(win=2048)


    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()
	#运行
curses.wrapper(main)

