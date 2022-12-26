import sys
start, end, qtream = sys.stdin.readline().split()

st_time = (int(start[:2]) * 60) + int(start[3:])
et_time = (int(end[:2]) * 60) + int(end[3:])
qt_time = (int(qtream[:2]) * 60) + int(qtream[3:])

# print("입력시간 : " + str(st_time) + ", " + str(et_time) + ", " + str(qt_time))


dic = {}
while True:
	try:
		input_time, name = sys.stdin.readline().split()
		check_time = (int(input_time[:2]) * 60) + int(input_time[3:])
		if check_time <= st_time:
			dic[name] = True
		elif name in dic and et_time <= check_time <= qt_time:
				dic[name] = False
	except:
		break

cnt = 0
for i in dic.items():
	if i[1] == False:
		cnt += 1

print(cnt)