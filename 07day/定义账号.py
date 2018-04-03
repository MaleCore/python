acc = "123456"
pwd = "abc"
account = input("请输入一个账号")
passwd = input("请输入一个密码")

if account == acc and passwd == pwd:
	print("登录成功")
if account != acc and passwd == pwd:
	print("账号错误")
if account == acc and passwd != pwd:
	print("密码不对")
if account != acc and passwd != pwd:
	print("账号和密码错误")
