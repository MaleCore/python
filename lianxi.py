'''
import random
random.randint(1,100)
n = random.randint(1,100)
print("生成的随机数字是")
i = 0
while True:
	num = int(input("请输入你猜测的数字"))
	i += 1
	if num > n:
		print("猜大了")
	elif num < n:
		print("猜小了")
	else:
		print("猜对了")
		break
print("一共猜了%d次"%i)
if i<=5:
	print("你太聪明了,这么快就猜对了")
'''
'''
for a in range(1,10):
	for b in range(1,a+1):
		print("%d*%d=%d"%(a,b,a*b),end = "\t")
	print(" ")
'''
'''
l = []
for i in range(3):
	x = int(input("integer:\n"))
	l.append(x)
	l.sort()
print(l)
'''
dict = {"name":"zzzz","age":7,"class":"first"}
print(dict)




















