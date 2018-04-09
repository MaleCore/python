import random
c = random.randint(1,100)
i = 1
while i<=10:
	a = int(input("请输入猜测的数字:"))
	if a>c:
		print("大了")
	if a<c:
		print("小了")
	elif a==c:
		print("准了")
		break
	i+=1
