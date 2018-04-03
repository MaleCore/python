hight = float(input("请输入身高"))
weight = float(input("请输入体重"))
bmi = float(weight/(hight**2))

if bmi < 18.5:
	print("过轻")
if bmi > 18.5 and bmi < 25:
	print("正常")
if bmi > 25 and bmi <= 28:
	print("过重")
if bmi > 28 and bmi <= 32:
	print("肥胖")
if bmi > 32:
	print("严重肥胖")
