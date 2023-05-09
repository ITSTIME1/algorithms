import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 1,1
# 2,2 와 같이
# 이건 무조건 자기자신만 가르키기 때문에
# 하나의 인덱스에 하나를 가르킨다.

# 그러면 우선
# 인접행렬로
# n*n 행렬을 만든다음에
# 크기만큼 받아서
# 해당 행렬위치에 저장해주고
# 1,3이면 3,1 이렇게
# 그렇게 전부다 행렬에 저장한뒤

# 모든 v+e
# dfs로 풀면
# 한 정점으로부터 이어져 있는 정점들을 모두 찾아서
# 해당 정점으로부터 생기는 걸 dic저장
# 해당 방문지점들은 visited에 설정해두고
# 그 지점들은 건너뛰면서
# 다음 지점을 탐색
# 그럼 dic 저장되어 있는 개수가 곧 사이클의 개수


T = int(input())


visit = set()
def dfs(matrix, i, j):
	# 3에서 탐색할게 있다면
	global visit
	non_visit = deque()
	non_visit.append((i, j))

	while non_visit:
		
		x, y = non_visit.popleft()
		visit.add(i)
		visit.add(j)
		matrix[x][y] = 0
		matrix[y][x] = 0

		for k in range(y, y+1):
			for c in range(n):
				if matrix[k][c] == 1:
					non_visit.append((k, c))

	


for i in range(T):
	n = int(input())
	matrix = [[0 for _ in range(n)] for _ in range(n)]

	arr = list(map(int, input().split()))
	for i in range(len(arr)):
		matrix[i][arr[i]-1] = 1
		matrix[arr[i]-1][i] = 1

	ans = 0
	for i in range(n):
		for j in range(n):
			if i not in visit and j not in visit and matrix[i][j] == 1:
					dfs(matrix, i, j)
					ans += 1
					visit = set()
	
	print(ans)
