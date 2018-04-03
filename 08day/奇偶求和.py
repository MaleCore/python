a = 0
b = 0
c = 0
while a<100:
	a+=1
	if a%2==0:
		print(a)
		b+=a
	else:
		c+=a
print("偶数的和为%d"%b)
print("奇数的和为%d"%c)
