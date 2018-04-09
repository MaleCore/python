cards = [{"name":"没头脑","age":20},{"name":"不高兴","age":21},{"name":"葫芦娃","age":25}]
for i in cards:
	for k,v in i.items():
		print("%s的值是%s"%(k,v))
