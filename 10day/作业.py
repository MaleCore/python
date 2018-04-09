md = ["诸葛亮","庞统","司马懿","姜维","周瑜","陆逊","郭嘉"]
for i in md:
	print("邀请%s来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("*"*50)
print("%s去打仗不能来"%md[4])
md[4] = "曹操"
print("*"*50)
for i in md:
	print("邀请%s来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("*"*50)
md.insert(0,"刘备")
md.insert(4,"关羽")
md.append("张飞")
for i in md:
	print("邀请%s来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("*"*50)
print("*"*50)
for i in range (len(md)):
	if len(md) == 2:
		break
	print("%s,餐桌没来,不能邀请你了"%md[0:1])
	md.pop(0)
print("*"*50)
for i in md:
	print("%s,请按时来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
del md[0:2]
print(md)
print("*"*50)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("*"*50)
