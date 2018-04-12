def jisuanqi(x,y,fuhao):
	if fuhao == "+":
		z = x+y
		print("和是%0.2d"%z)
	elif fuhao == "-":
		z = x-y
		print("差是%0.2d"%z)
	elif fuhao == "*":
		z = x*y
		print("积是%0.2d"%z)
	elif fuhao == "/":
		z = x/y
		if y != 0:
			print("商是%0.2d"%z)
		else:
			print("输入有误")
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请输入一个数字"))
	z = input("选择+-*/")


	jisuanqi(x,y,z)
