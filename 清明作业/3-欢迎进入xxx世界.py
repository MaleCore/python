acc = "123456"
pwd = "123456"
account = input("请输入账号")
passwd = input("请输入密码")
if account == acc and passwd == pwd:
	print("欢迎来到虚拟世界")
elif account != acc and passwd != pwd:
	print("登录失败")
