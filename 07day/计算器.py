def a():
	x = float(input("请输入一个数字"))
	y = float(input("请输入一个数字"))

	fuhao = input("请输入+-*/")

	if fuhao == "+":
		print(x+y)
	elif fuhao == "-":
		print(x-y)
	elif fuhao == "*":
		print(x*y)
	elif fuhao == "/":
		print(x/y)
a()
