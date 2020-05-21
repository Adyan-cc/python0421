import pygame  # 导入pygame

# 初始化pygame库，让计算机硬件准备
pygame.init()


# --------窗口相关操作----------

# 创建窗口
window = pygame.display.set_mode((窗口宽，窗口高))

#窗口填充颜色
window.fill((0,0,0))

# 刷新界面  不刷新不会更新显示的内容
pygame.display.update()


# 设置窗口标题
pygame.display.set_caption("窗口标题")

# 设置窗口图标
image = pygame.image.load("res/game.ico")
pygame.display.set_icon(image)



# --------图像相关操作-----------

# 加载图片文件，返回图片对象
image = pygame.image.load("图片路径")

# 贴图（指定坐标，将图片绘制到窗口）
window.blit(image, (0, 0))

# 判断两个矩形是否相交，相交返回True, 否则返回False
flag = pygame.Rect.colliderect(rect1, rect2)

# 进行一对一的冲突检测
pygame.sprite.collide_rect(obj1,obj2)

# 获得图片矩形对象 -> Rect(x, y, width, height)  x,y默认都是左上角(0,0)
rect = image.get_rect()
# 获取图片的宽高
print(rect.width)

# 在原位置基础上，移动指定的偏移量 （x, y 增加）
rect.move_ip(num1, num2)

# 将图片对象按指定宽高缩放，返回新的图片对象
trans_image = pygame.transform.scale(image, (WINDOWWIDTH, WINDOWHEIGHT))



# --------事件相关操作-----------

# 获取新事件
for event in pygame.event.get():
	# 1. 鼠标点击关闭窗口事件
	if event.type == pygame.QUIT:
		print("点击关闭窗口按钮")
		sys.exit()  # 关闭程序
		pygame.quit()  # 退出pygame，清理pygame占用资源

	# 2. 键盘按下事件
        if event.type == pygame.KEYDOWN:
            # 判断用户按键
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("right")
            if event.key == pygame.K_SPACE:
                print("space")


# 3. 键盘长按事件
# 获取当前键盘所有按键的状态（按下/没有按下），返回bool元组  (0, 0, 0, 0, 1, 0, 0, 0, 0)
pressed_keys = pygame.key.get_pressed()

if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
	print("left")
if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
    print("right")


# ----------文本相关操作-------------

# 加载系统字体，返回字体对象
font_obj = pygame.font.SysFont('SimHei', 42)

# 加载自定义字体，返回字体对象
font_obj = pygame.font.Font("res/SIMHEI.TTF", 42)

三基色： Red Green Blue
0 - 255

# 设置文本，返回文本对象   render(文本内容， 抗锯齿，颜色)
text_obj = font.render("飞机大战", 1, (255, 255, 255))

# 设置文本的位置和尺寸   获取文本的Rect并修改Rect的中心点为 （300，300）
text_rect = text_obj.get_rect(centerx=300, centery=300)

# 在指定位置和尺寸绘制指定文字对象
window.blit(text_obj, text_rect)



# ---------音效相关操作------------

# 加载背景音乐
pygame.mixer.music.load("./res/bg2.ogg")
# 循环播放背景音乐
pygame.mixer.music.play(-1)
# 停止背景音乐
pygame.mixer.music.stop()

# 生成音效对象
boom_sound = pygame.mixer.Sound("./res/baozha.ogg")
# 播放音效
boom_sound.play()
# 停止音效
boom_sound.stop()




