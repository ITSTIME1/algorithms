import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [[0 for _ in range(10)] for _ in range(10)]

xx, yy = 0, 0

x, y = 0, 0
dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = 0


arr[x][y] = 1
while True:

	nx = x+dx[start][0]
	ny = y+dx[start][1]		

	if nx == xx and ny == yy:
		break

	if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
		start += 1
		start %= len(dx)
		continue


	x, y = nx, ny
	arr[x][y] = 1


# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print(arr)