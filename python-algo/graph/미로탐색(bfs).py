import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# bfs 너비우선 탐색으로 풀어보자면
# 먼저 1은 이동가능한 경로
# 0은 이동이 불가능한 경로이다

# 앞서 dfs 로 풀었을 경우 모든 구간을 다 탐색하기 때문에
# 최단경로를 찾기가 매우 어려웠다 (다익스트라 알고리즘 개념을 사용해야 풀린다.)
# 하지만 곰곰히 생각해보면 dfs 는 한도 끝도 없이 내려갈 수 있다 즉 하나의 정점의 대해서 연결된 정점까지
# 계속해서 내려간다는 것이다. 연결된 정점이라면 모든 연결된 정점을 다 지나가게 되고
# 이렇게 된다면 최적의 경로를 찾을 확률이 매우 적어진다.

# 반면에 bfs 같은 경우 한 정점의 대해서 연결된 정점들을 우선적으로 전부 탐색하게 된다.
# 즉 그 정점의 인접정점들을 탐색하다보면 한정점의 연결된 정점들만 탐색하는게 아니기 때문에
# 최적의 경로를 찾는게 더 빠를 수도 있다는 것이다.
n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

x, y = 0, 0

# print(matrix)

# 북 서 남 동 
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, graph):
	visited = deque([])
	visited.append((x, y))

	while visited:
		x, y = visited.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			# 이동이 가능한 상태를 정의
			if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				if nx == n-1 and ny == m-1:
					return
				visited.append((nx, ny))


bfs(x, y, graph)

print(graph[n-1][m-1])