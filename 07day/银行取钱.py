acc = "123456"
pwd = "asd"
mon = 1000000
account = input("输入账号")
passwd = input("输入密码")

if account == acc and passwd == pwd:
	print("成功进入账户")
	money = float(input("请输入取款金额:"))
	if money <= mon:
		print("已取金额:%f，剩余金额:%f"%(money,mon))
	elif money > mon:
		print("余额不足")
else:
	print("非法用户")
