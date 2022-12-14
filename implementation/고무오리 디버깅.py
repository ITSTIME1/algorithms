

import sys
pr = 0  
while True:
	string = sys.stdin.readline().strip()
	if string == "고무오리 디버깅 끝":
		break

	elif string == "문제":
		pr+=1

	elif string == "고무오리":

		# 문제가 없는데 고무오리를 시도 한다고한다면
		if pr == 0:
			pr+=2
		# 문제가 있다면
		else:
			pr-=1


if pr != 0:
	print("힝구")
else:
	print("고무오리야 사랑해")