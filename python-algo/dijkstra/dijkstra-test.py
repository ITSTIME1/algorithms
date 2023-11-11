from collections import deque


n = int(input())
# 정방행렬로
path = [[0 for i in range(n)]for _ in range(n)]

dx = [(-1, 0), (1, 0), (0,-1), (0, 1)]

visited = [False] * n

def dijkstra(path, start_destination):
	queue = deque([start_destination])
	visited[start] = True

	while queue:
		x, y = queue.popleft()
		for index in range(4):
			nx = dx[index][0] + x
			ny = dx[index][1] + y


		# success
		if 0<= nx < n and 0 <= ny < n:
			queue.append((nx, ny))	



		# fail 





dijkstra(path, 0)