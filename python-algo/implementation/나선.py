import sys
input = sys.stdin.readline


n, m = map(int, input().split())
visited = [[0] * n for _ in range(m)]
def simul():
	global visited
	startX, startY = m-1, 0
	visited[m-1][0] = 1
	# 동쪽으로간다.
	dx = [(0, 1), (-1,0), (0, -1), (1,0)]
	index = 0
	cnt = 0
	while cnt != 4:
		# 갈 수 있는 방향이라면
		x = startX + dx[index][0]
		y = startY + dx[index][1]
		if 0<= x < m and 0<= y < n and visited[x][y] == 0:
			cnt = 0
			if visited[x][y] == 0:
				visited[x][y] = visited[startX][startY] + 1
				startX, startY = x, y
				continuen
		else:
			index += 1
			index %= 4
			cnt += 1
		
	print(startY, m - startX - 1)

simul()
