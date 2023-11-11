# 문제에서

# 이동하는 도중에 벽을 한개까지 부수고 이동해서 경로가 짧아진다면
# 이라는 가정을 하고 있다.
# 즉 이동 하는 도중에 벽을 한개까지 부수고 이동해서 경로가 짧아진다면 -> 벽을 한개까지 부수고 이동한다.
# 벽을 한개까지 부수고 이동하지 않는다면 -> 이동하는 도중에 벽을 한개까지 부수고 이동해서 경로가 짧아지지 않는다.

# 그렇다면 벽을 부수고 이동해서 경로가 짧아지지 않을수도 있는거네

# 벽을 부수고 이동했을때  더 짧아 질 수 있는거고


# 그럼 몇가지 가정을 할 수 있는것 같은데
# 만약 벽을 뚫고 간다고 했을때
# 벽을 뚫은 다음 도착한 그 경로가, 벽을 뚫지 않았을때보다 빠르게 도착할 수 있다면
# 벽을 뚫고 도착한 경로가 더 빠르므로, 그 경로로 치환한다.

# 만약 벽을 뚫고 가지 않는다고 했을때
# 벽을 뚫지 않은 경로는 어짜피 0만이 지나가게 되므로, 그 구간은 먼저 도착한 구간이 더 빠른 구간임을 보장하므로
# 벽을 뚫지 않을때는 항상 최적의 경로가 나온다.
# 근데 그러면 bfs를 두번수행해야 하는거아닌가?
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(n)]


# v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# print(v)
# 각 경로가 벽을 부수고 이동한 경로인지
# 각 경로가 벽을 부수지 않고 이동한 경로인지
# [[[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]]]
def bfs(x, y, z):
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque([(x, y, z)])
	visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
	while queue:
		a, b, c = queue.popleft()
		# 끝 점에 도달하면 이동 횟수를 출력
		if a == n - 1 and b == m - 1:
			print(visited)
			return visited[a][b][c]
		for index in range(4):
			nx = dx[index][0] + a
			ny = dx[index][1] + b
			if 0<= nx < n and 0<= ny < m:
				# 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
				if board[nx][ny] == 1 and c == 0 :
					visited[nx][ny][1] = visited[a][b][0] + 1
					queue.append((nx, ny, 1))
					# 얘는 그럼 벽을 지나온 루트라고 해도
					# 방문을 하지 않았으면
					# 벽을 지나와서 처음으로 이동하는 루트기 때문에
					# 만약 벽을 지나오지 않은 루트라면
					# 방문을 하지 않았다면 그 경로는 최적의 경로기 때문에
				elif board[nx][ny] == 0 and visited[nx][ny][c] == 0:
					visited[nx][ny][c] = visited[a][b][c] + 1
					queue.append((nx, ny, c))


	print(visited)
	return -1
print(bfs(0, 0, 0))
