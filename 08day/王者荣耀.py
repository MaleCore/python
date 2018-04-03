acc = "123456"
pwd = "123456"
count = 0
while True:
	account = input("请输入账号")
	passwd = input("请输入密码")
	if account == acc and passwd == pwd:
		print("登录成功")
		hero = int(input("请选择英雄:1代表ADC,2代表坦克,3代表法师"))
		if hero == 1:
			print("刘备")
		elif hero == 2:
			print("张飞")
		elif hero == 3:
			print("诸葛亮")
		break
	else:
		count+=1
		print("请重新输入%d次"%count)
		if count == 3:
			print("强制退出")
			break
