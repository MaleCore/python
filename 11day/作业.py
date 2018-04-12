a = []
c = 0
while c<3:
	b = {}
	b["名字"] = input("输入名字:")
	b["年龄"] = int(input("输入年龄:"))
	b["QQ"] = input("输入性别:")
	b["体重"] = int(input("输入体重"))
	a.append(b)
	c+=1

for i in a:
	for j,v in i.items():
		print("%s:%s"%(j,v))
