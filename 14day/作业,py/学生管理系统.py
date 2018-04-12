def lu():
	padu = 0
	zid = {}
	xh = input('请输入学号:')
	for i in lie:
		if xh == i['学号']:
			padu = 1
			break
	if padu == 1:
		print('学号重复')
	else:
		name = input('请输入姓名:')
		shu = float(input('请输入数学成绩:'))
		yu = float(input('请输入语文成绩:'))
		ying = float(input('请输入英语成绩:'))
		ji = float(input('请输入计算机成绩:'))
		zid['学号'] = xh
		zid['姓名'] = name
		zid['数学成绩'] = shu
		zid['语文成绩'] = yu
		zid['英语成绩'] = ying
		zid['计算机成绩'] = ji
		lie.append(zid)
def cha():
	panduan = 0
	padu = input('请输入学号:')
	for i in lie:
		if padu == i['学号']:
			panduan = 1
			for j,v in i.items():
				print('%s:%s'%(j,v))
	if panduan == 0:
		print('查无此人')
def xiu():
	padu = 0
	xuehao = input('请输入学号:')
	for i in lie:
		if xuehao == i['学号']:
			padu = 1
			xm = input('请输入修改项1(学号),2(姓名),3(成绩)')
			if xm == '1':
				while True:
					pd = 0
					xxuehao = input('请输入新学号:')
					for k in lie:
						if xxuehao == k['学号']:
							pd = 1
							print('学号重复,请重新输入')
							break
					if pd == 0:
						yn = input('确认修改?y/n:')
						if yn == 'y':
							print('修改成功')
							i['学号'] = xxuehao
						elif yn == 'n':
							print('修改失败')
						else:
							print('选项错误')
						break
			elif xm == '2':
				xname = input('请输入新名字:')
				yn = input('确认修改?y/n:')
				if yn == 'y':
					print('修改成功')
					i['姓名'] = xname
				elif yn == 'n':
					print('修改失败')
				else:
					print('选项错误')
			elif xm == '3':
				xcj = input('1(数学),2(语文),3(英语),4(计算机)')
				if xcj == '1':
					xsx = float(input('输入新成绩:'))
					yn = input('确认修改?y/n:')
					if yn == 'y':
						print('修改成功')
						i['数学成绩'] = xsx
					if yn == 'n':
						print('修改失败')
					else:
						print('选项错误')
				elif xcj == '2':
					xyw = float(input('输入新成绩:'))
					yn = input('确认修改?y/n:')
					if yn == 'y':
						print('修改成功')
						i['语文成绩'] = xyw
					if yn == 'n':
						print('修改失败')
					else:
						print('选项错误')
				elif xcj == '3':
					xyy = float(input('输入新成绩:'))
					yn = input('确认修改?y/n:')
					if yn == 'y':
						print('修改成功')
						i['英语成绩'] = xyy
					if yn == 'n':
						print('修改失败')
					else:
						print('选项错误')
				elif xcj == '4':
					xjsj = float(input('输入新成绩:'))
					yn = input('确认修改?y/n:')
					if yn == 'y':
						print('修改成功')
						i['计算机成绩'] = xjsj
					if yn == 'n':
						print('修改失败')
					else:
						print('选项错误')
			else:
				print('选项错误')
	if padu == 0:
		print('查无此人')
def de():
	sc = input('输入学号')
	padu = 0
	for i in lie:
		if sc == i['学号']:
			padu = 1
			yn = input('确认删除?y/n:')
			if yn == 'y':
				lie.remove(i)
				print('删除成功')
			elif yn == 'n':
				print('删除失败')
			else:
				print('错误选项')
	if padu == 0:
		print('查无此人')
def li():
	nu = 0
	for i in lie:
		nu += 1
		print('%d、'%nu,end = '')
		for j,v in i.items():
			print('%s:%s  '%(j,v),end='')
		print('')
	if lie == []:
		print('列表为空')

print('学生管理系统'.center(30,' '))
print('1.录入成绩'.center(30,'*'))
print('2.查询成绩'.center(30,'*'))
print('3.修改信息'.center(30,'*'))
print('4.删除信息'.center(30,'*'))
print('5.查看全部'.center(30,'*'))
print('6.退出系统'.center(30,'*'))
lie = []
while True:
	caidan = input('请选择菜单')
	if caidan == '1':
		lu()
	elif caidan == '2':
		cha()
	elif caidan == '3':
		xiu()
	elif caidan == '4':
		de()
	elif caidan == '5':
		li()
	elif caidan == '6':
		yn = input('确认退出?y/n:')
		if yn == 'y':
			print('欢迎下次使用')
			break
		elif yn == 'n':
			print('欢迎回来')
		else:
			print('选择错误')
