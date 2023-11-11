import sys
import heapq
import math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


def not_bfs(sx, sy):
	global board
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque([sx, sy])

	while queue:
		x, y= queue.popleft()

		for index in range(4):
			nx = dx[index][0] + x
			ny = dx[index][1] + y
			# 벽을 부수고 이동하거나
			# 벽을 부수고 이동하지 않거나

			# 그럼
			if 0<= nx < n and 0<= ny < m:


	pass



board = [list(map(int, input().rstrip())) for _ in range(n)]


not_bfs(0, 0)