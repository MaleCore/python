def sum(a,b):
	c = a+b
	print(c)

def sum1(a,b,*args,**kwargs):
	all_sum = 0
	c = a+b
	print(args)
	print(kwargs)
	all_sum+=c
	for i in args:
		all_sum+=i
	for i in kwargs.values():
		all_sum+=i

	print(all_sum)

sum(1,2)
#sum1(1,2,3,4,5,date6)
t = (3,4,5)
d = {"date":6}
sum1(1,2,*t,**d)




