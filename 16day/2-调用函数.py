import time
def register(phone,pwd):
	add = diaoyong(phone)
	if add:
		print("注册成功")
	else:
		print("注册失败")

def land(phone,pwd):
	add = diaoyong(phone)
	if add:
		print("登录成功")
	else:
		print("登录失败")
def diaoyong(phone):
	if phone.startswith("1") and len(phone)==11:
		return True
	else:
		return False

register("18888888888","123456")
land("18888888888","123456")
