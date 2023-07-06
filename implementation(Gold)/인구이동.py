import sys 
from collections import deque
input = sys.stdin.readline


n, l, r = map(int, input().split())

# 인구수
c = [list(map(int, input().split())) for _ in range(n)]


def bfs(i, j):
	global flag
	queue = deque([[i, j]])
	# 북 서 남 동
	dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	cordi = [[i, j]]
	while queue:
		q = queue.popleft()
		for i in range(4):
			nx = dx[i][0] + q[0]
			ny = dx[i][1] + q[1]

			# 범위만 안넘어가게 설정해주고
			# 그리고 이미 방문했던 지점은 가지마
			if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny] == True:
				continue 

			dist = max(c[nx][ny], c[q[0]][q[1]]) - min(c[nx][ny], c[q[0]][q[1]])

			# l이상이고 r이하일때
			# 인구이동이 가능하다는소리자나
			if l <= dist <= r:
				visit[nx][ny] = True
				queue.append([nx, ny])
				cordi.append([nx, ny])

	if len(cordi) > 1:
		flag = True
		human = int(sum([c[idx[0]][idx[1]] for idx in cordi]) / len(cordi))

		for idx in cordi:
			c[idx[0]][idx[1]] = human



total = 0
while True:
	visit = [[False] * n for _ in range(n)]
	flag = False
	for i in range(n):
		for j in range(n):
			if visit[i][j] == False:
				visit[i][j] = True
				bfs(i, j)
			else: continue
	
	if not flag:
		print(total)	
		break

	total += 1
            
