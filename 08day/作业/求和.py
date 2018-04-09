a = 0
b = 0
while a < 99:
	a+=1
	if a%2 == 0:
		b-=a
	else:
		b+=a
print(b)
