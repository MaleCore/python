def math():
	for a in range(1,10):
		for b in  range(1,a+1):
			print("%d*%d=%d"%(b,a,a*b),end="\t")
		print(" ")
math()
