def system():
	padu = 0
	zid = {}
	xh = input("请输入学号")
	for i in lie:
		if xh == i["学号"]:
			padu = 1
			break
	if padu == 1:
		print("学号重复")
	else:

