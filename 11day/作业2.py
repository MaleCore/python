list = []
name_list = []
count = 0
while True:
	if count == 3:
		break


	#输入
	dict = {}
	name = input("姓名")
	age = int(input("年龄"))
	sex = input("性别")
	qq = int(input("qq号"))
	weight = float(input("体重"))
	#字典赋值
	if name not in name_list:			
		dict["name"] = name
		dict["age"] = age
		dict["sex"] = sex
		dict["qq"] = qq
		dict["weight"] = weight
		list.append(dict)
		name_list.append(name)#一定要记录
		print(list)
		count+=1
	else:
		print("名字重复")
age_sum = 0
#遍历
for i in list:
	age_sum+=i.get("age")
	print(i)
print("年龄的平均值是%0.2f"%(age_sum/len(list)))





