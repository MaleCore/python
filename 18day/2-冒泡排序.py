list = [10,2,4,1,44,25]
print(list)
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)










