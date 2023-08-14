# 최소 한표 이상은 받기 때문에
# 표가 없는 경우는 없음
# 따라서
# 최다득표자가 1명이냐 또는 1명보다 많냐만 따지면 됨
# 1명보다 많다면 nowinner
# 만약 한명이라면 그 한명이 절반 이상의 득표를 받았는지를 판단하면되고

import sys
input = sys.stdin.readline

t = int(input())

while t > 0:
	n = int(input())
	a = [int(input()) for _ in range(n)]

	if a.count(max(a)) == 1:
		result = sum(a) * 0.5
		if max(a) <= result:
			print(f'minority winner {a.index(max(a)) + 1}')
		else:
			print(f'majority winner {a.index(max(a)) + 1}')
	elif a.count(max(a)) > 1:
		print(f'no winner')

	t-= 1

