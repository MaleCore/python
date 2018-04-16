def jisuanqi(x,y,z):
	if z == 1:
		return x+y
	elif z == 2:
		return x-y
	elif z == 3:
		return x*y
	elif z == 4:
		if y != 0:
			return x/y
		else:
			print("输入有误")
	elif z == 5:
		return x**y
	else:
		print("输入错误")
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请输入一个数字"))
	z = int(input("输入符号1(+),2(-),3(*),4(/),5(**):"))
	jieguo = jisuanqi(x,y,z)
	print(jieguo)
