import time
def play():
	for i in range(10):
		print("打代码,美滋滋")
		time.sleep(1)
	print("元哥来了")
	result = kill()
	if result == "说的没脸了":
		print("一天就打代码,去玩游戏")
	else:
		print("没发现,继续打代码,美滋滋")
def kill():
	print("一顿说教")
	return"说的没脸了"




play()
