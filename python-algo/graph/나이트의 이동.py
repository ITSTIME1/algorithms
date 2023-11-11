import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(sx, sy):
	global board

	# 큐에 시작 위치를 담아주고
	queue = deque([(sx, sy)])

	while queue:
		x, y = queue.popleft()

		for index in range(8):
			nx = dx[index][0] + x
			ny = dx[index][1] + y
			# 범위 안에서 이동해야 하니까	
			if 0<= nx < l and 0 <= ny < l:
				# 거리를 갱신
				if board[nx][ny] == 0:
					board[nx][ny] = board[x][y] + 1
					
					if nx == goalX and ny == goalY:
						return board[nx][ny]


					queue.append((nx, ny))


while T != 0:
	# 한변의 길이
	l = int(input())

	# 나이트가 현재 있는 칸
	startX, startY = map(int, input().split())

	# 나이트가 이동할 칸
	goalX,goalY = map(int, input().split())

	# 체스판
	board = [[0] * l for _ in range(l)]

	if startX == goalX and startY == goalY:
		print(0)
	else:
		print(bfs(startX, startY))

	T -= 1