import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

board = [list(input().strip()) for _ in range(n)]


def bfs(board, i, j):
	queue = deque()
	queue.append((i, j))
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]
	cnt = 1
	board[i][j] = "0"

	while queue:
		x, y = queue.popleft()

		for c in range(4):
			nx = x + dx[c]
			ny = y + dy[c]

			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue

			if board[nx][ny] == "1":
				board[nx][ny] = "0"
				cnt += 1
				# 해당 1의 위치에서 방향을 탐색먼저하고
				# 그럼 이렇게 되면 한 단지에서 더 이상
				# 탐색할게 없으니까
				# 종료되고
				queue.append((nx, ny))
	return cnt


danzi = 0
cnt = 1
ans = []
for i in range(n):
	for j in range(n):
		if board[i][j] == "1":
			f = bfs(board, i, j)
			ans.append(f)
			danzi += 1


print(danzi)
ans.sort()
print(*ans, sep="\n")