money = int(input("请输入身价"))
face = int(input("请输入颜值"))
height = float(input("请输入身高"))

if (height >= 180 and money >= 100000000 and face >= 90):
	print("高富帅")
elif (height >= 170 and money >= 1000000 and face >= 80):
	print("帅")
elif (height <= 170 and money <= 1000000 and face <= 60):
	print("小康")
else :
	print("乞丐")
