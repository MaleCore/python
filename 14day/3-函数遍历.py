def city():
	list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
	for i in list:
		for a,b in i.items():
			for d,c in b.items():
				print(a,d,c)
city()
