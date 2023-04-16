import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [[0 for _ in range(10)] for _ in range(10)]



# 동 남 서 북
dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]


x, y = 0, 0
start = 0
arr[x][y] = 1
cnt = 1
while True:
	nx = x + dx[start][0]
	ny = y + dx[start][1]

	if nx == 0 and ny == 0:
		cnt += 1
		# 마지막 모서리에서 한번더 더해주면 둘레의 길이 완성
		break

	if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
		start += 1

		# 모서리 부분을 한번더 더해줌으로써
		# 중복된걸 해결할 수 있고
		cnt += 1
		if start >= 4:
			start %= 4
		continue

	x, y = nx, ny
	arr[x][y] = 1
	cnt += 1

# ddx = [-1, 1, 0, 0]
# ddy = [0, 0, -1, 1]
# for i in range(10):
# 	for j in range(10):
# 		if arr[i][j] == 1:
# 			for k in range(4):
# 				if arr[i+ddx[k]][j+ddy[k]] == 1

print(cnt)

