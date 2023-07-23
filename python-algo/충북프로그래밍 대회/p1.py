# a와 b가 가위 바위보를 한다


# 가위 1
# 바위 2
# 보 3

import sys
input = sys.stdin.readline


T = int(input())

for i in range(T):
	a, b = map(int, input().split())

	# 3 > 2
	# 2 < 3
	# 1 < 2

	if a > b:
		if a == 3 and b == 1:
			print("#"+str(i+1)+" B")
		else:
			print("#"+str(i+1)+" A")

	else:
		if b == 3 and a == 1:
			print("#"+str(i+1)+" A")
		else:
			print("#"+str(i+1)+" B")
