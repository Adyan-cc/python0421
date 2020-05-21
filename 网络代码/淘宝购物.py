#刚创建账户所拥有的钱
money = 0

#定义商品列表
goods_list = [
{'name':'iphone','price':4500,'count':40},
{'name':'电脑','price':7000,'count':100},
{'name':'平板','price':5000,'count':60},
{'name':'羽绒服','price':500,'count':80},
{'name':'西服','price':1000,'count':90},
{'name':'运动鞋','price':200,'count':120},
{'name':'vivo','price':2000,'count':200},
{'name':'自行车','price':2100,'count':300}]

#创建空的购物车
shoppingCar = []

#创建订单列表
order = []

#注册账户
def register():
	print('→'*8,'注册账号','←'*8)
	global account
	global password
	account = input('请输入账号')
	password = input('请输入密码')
	password1 = input('请确认密码')
	while True:
		if password == password1:
			print('→'*8,'注册成功','←'*8)
			log_in()
			break
		else:
			password = input('请重新输入密码')
			password1 = input('请确认密码')

#登录
def log_in():
	print('~'*10,'登录账号','~'*10)
	while True:
		user_account = input('请输入您的账号')
		user_password = input('请输入您的密码')
		if user_account != account:
			print('账号有误')
		elif user_account == account and user_password != password:
			print('密码有误')
		else:
			print('~'*10,'登录成功','~'*10)
			show_menu()
			break

#展示商品列表
def show_name():
	print('='*30)
	a = 0
	for i in range(0,len(goods_list)):
		for key in goods_list[i].keys():
			if key == 'name':
				a += 1
				print(goods_list[i][key], end = '\t')
		if a % 4 ==0 :
			print('')
	print('='*30)

#选择操作
def show_menu():
	while True:
		print('※'*20)
		print('请选择您要执行的操作：')
		print('1、查询商品')
		print('2、查看购物车')
		print('3、查看订单')
		print('4、其他功能')
		print('5、退出系统')
		print('※'*20)
		choice = int(input())
		if choice == 1:
			show_name()
			search_shopping()
		elif choice == 2:
			show_shoppingCar()
		elif choice == 3:
			show_order()
		elif choice == 4:
			other()
		else:
			print('欢迎下次光临！')
			break

#添加商品至购物车
def add_shopping(name,price,count,total):
	dict = {}
	dict['name'] = name
	dict['price'] = price
	dict['count'] = count
	dict['total'] = total
	shoppingCar.append(dict)

#展示购物车
def show_shoppingCar():
	global money
	NeedMoney = 0
	for i in range(0,len(shoppingCar)):
		for key in shoppingCar[i].keys():
			print('*'*30)
			if key == 'name':
				print('商品名称:'+shoppingCar[i][key])
			elif key == 'price':
				print('商品单价:%d'%shoppingCar[i][key])
			elif key == 'count':
				print('商品数量:%d'%shoppingCar[i][key])
			elif key == 'total':
				print('商品总价:%d'%shoppingCar[i][key])
				NeedMoney += shoppingCar[i][key]
				print('一共需花费%d元'%NeedMoney)
	if money >= NeedMoney:
		money -= NeedMoney
		pay_shopping()
		print('一共花费%d元'%NeedMoney)
	else:
		print('余额不足')
		charge_money()

#清空购物车
def pay_shopping():
	print('是否支付 yes / no')
	user = input('')
	if user == 'yes':
		print('支付成功')
		order.extend(shoppingCar)
		shoppingCar.clear( )

#设置充值密码
def charge_pwd():
	global charge_password
	global money
	print('❀'*30)
	charge_password2 = input('请输入密码')
	charge_password1 = input('请确认密码')
	while True:
		if charge_password1 == charge_password2:
			charge_password = charge_password1
			print('❀'*10,'设置成功','❀'*10)
			show_menu()
			break

#充值金额
def charge_money():
	global money
	print('是否充值   yes / no')
	user = input('')
	if user == 'yes':
		while True:
			user = input('请输入密码')
			if user == charge_password:
				while True:
					chargeMoney = int(input('请输入充值金额'))
					if chargeMoney % 100 != 0:
						print('请输入充值金额')
					else:
						money += chargeMoney
						print('充值成功')
						break
				break
			else:
				print('密码有误')

#添加至订单
def add_order(name,price,count,total):
	dict = {}
	dict['name'] = name
	dict['price'] = price
	dict['count'] = count
	dict['total'] = total
	order.append(dict)

#展示订单
def show_order():
	cost_money = 0
	#总共花费的钱
	for i in range(0,len(order)):
		for key in order[i].keys():
			print('*'*50)
			if key == 'name':
				print('商品名称:'+order[i][key])
			elif key == 'price':
				print('商品单价:%d'%order[i][key])
			elif key == 'count':
				print('商品数量:%d'%order[i][key])
			elif key == 'total':
				print('商品总价:%d'%order[i][key])
				cost_money += order[i][key]
	print('总共花费%d元'%cost_money)

#查找商品
def search_shopping():
	name = input('请输入您要查询的名称：')
	isExist = False
	for i in range(0,len(goods_list)):
		if isExist:
			isExist = False
			break
		dict = goods_list[i]
		if dict['name'] == name:
			print('商品名称：'+name)
			print('商品单价：%d'%dict['price'])
			print('商品库存：%d'%dict['count'])
			if dict['count'] != 0 :
				print('请选择一下功能：\n1、购买\n2、添加至购物车\n3、返回上一项')
				choice = int(input())
				if choice == 1:
					buy_shopping(dict)
					isExist = True
				elif choice == 3:
					search_shopping()
				elif choice == 2:
					num = int(input('请选择添加至购物车的数量：'))
					while True:
						if num > dict['count']:
							print('超出总量限制，请重新输入！')
							num = int(input('请选择添加至购物车的数量：'))
						else:
							add_shopping(dict['name'],dict['price'],num,dict['price']*num)
							isExist = True
							print('添加成功')
							break
				else:
					print('输入有误，再见！')
		else:
			if i == len(goods_list)-1:
				print('该商品不存在，请重新选择功能！')

#购买商品
def buy_shopping(dict):
	global money
	if dict['count'] == 0:
		print('该商品已售空，请选择其他商品')
	else:
		while True:
			num = int(input('请输入购买的数量：'))
			if num <= dict['count']:
				needMoney = num * dict['price']
				if money < needMoney:
					print('余额不足，请充值或修改购买数量！')
				else:
					money -= needMoney
					dict['count'] -= num
					print('购买成功！')
					add_order(dict['name'],dict['price'],num,dict['price']*num)
				break
			else:
				print('库存不足，请重新输入')

#其他功能
def other():
	print('△'*30)
	print('请选择您要执行的操作：')
	print('1、充值')
	print('2、更改登录密码')
	print('3、更改充值密码')
	print('4、查看余额')
	choice = int(input())
	if choice == 1:
		print('是否选择设置充值密码　yes/ no')
		a = input()
		if a == 'yes' :
			charge_pwd()
		else:
			charge_money()
	elif choice == 2:
		change_password()
	elif choice == 3:
		changeCPWD()
	elif choice == 4:
		print('余额为%d元'%money)

#更改登录密码
def change_password():
	global password
	while True:
		print('☆'*30)
		a = input('输入新密码')
		b = input('确认密码')
		print('☆'*30)
		if a == b:
			password = a
			print('请重新登录')
			log_in()
			break
		else:
			print('重新输入')

#更改支付密码
def changeCPWD():
	global charge_password
	while True:
		print('◇'*30)
		a = input('输入新密码')
		b = input('确认密码')
		print('◇'*30)
		if a == b:
			charge_password = a
			break
		else:
			print('重新输入')


register()
