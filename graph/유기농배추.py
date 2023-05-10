import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**7)



T = int(input())



# def dfs(matrix, c, k):

# 	if c < 0 or c >= n or k < 0 or k >= m:
# 		return 


# 	dx = [-1, 0, 1, 0]
# 	dy = [0, 1, 0, -1]		

# 	if matrix[c][k] == 1:
# 		matrix[c][k] = 0
# 		for i in range(4):
# 			nx = c + dx[i]
# 			ny = k + dy[i]
# 			dfs(matrix, nx, ny)
# 		return True
# 	return False

def bfs(matrix, c, k):
	queue = deque()
	queue.append((c, k))

	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]	

	while queue:
		x, y = queue.popleft()
		matrix[x][y] = 0
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue

			if matrix[nx][ny] == 1:
				queue.append((nx, ny))



for _ in range(T):
	n, m, k = map(int, input().split())

	matrix = [[0 for _ in range(m)] for _ in range(n)]
	
	# 0<x< n-1, 0<y<m-1

	# 배추를 만들어주고
	for _ in range(k):
		x, y = map(int, input().split())
		matrix[x][y] = 1

	ans = 0
	for c in range(n):
		for k in range(m):
			if matrix[c][k] == 1:
				bfs(matrix, c, k)
				ans += 1
				


	print(ans)







