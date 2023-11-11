

import sys
input = sys.stdin.readline


T = int(input())


for _ in range(T):
	# 용량, 지점
	w, n = map(int, input().split())

	d = 0
	capa = w
	for i in range(n):
		# 거리, 쓰레기양
		x_i, w_i = map(int, input().split())

		if w - w_i < 0:
			d += (x_i * 2)
			w = capa - w_i

		elif w - w_i == 0:
			d += (x_i * 2)
			w = capa

		else:
			w -= w_i

	# 마지막 용량이 남은경우도
	# 집으로 가야하니까
	# 즉 맨마지막까지 돌았는데도 물건을 담은 상태라면
	# 돌아갔다 와야하므로
	if w != capa:
		d += x_i * 2

		
	print(d)

