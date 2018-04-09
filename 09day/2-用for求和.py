while True:
	a = int(input("请输入一个数字:"))
	b = int(input("请输入一个数字:"))
	sum = 0
	if a < b:
		for c in range(a,b+1):
			print(c)
			sum = sum + c
		print(sum)
		break
	else:
		print("重新输入")

