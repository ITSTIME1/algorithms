# w, h는 적어도 1이상

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 상하좌우(북서, 복동, 남서, 남동)
dx = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(i, j):
	global board
	for index in range(8):
		nx = dx[index][0] + i
		ny = dx[index][1] + j
		# 바다라면
		if 0<= nx < h and 0 <= ny < w:
			if board[nx][ny] == 1:
				board[nx][ny] = 0
				dfs(nx, ny)
		else: continue





while True:

	# 각 테스트 케이스에는 w, h가 주어진다.
	w, h = map(int, input().split())
	if w == 0 and h == 0: break
	# 지도
	board = [list(map(int, input().split())) for _ in range(h)]

	# 0은 바다, 1은 땅
	land = 0
	# 5, 4
	for i in range(h):
		for j in range(w):
			# 육지라면
			if board[i][j] == 1:
				board[i][j] = 0
				dfs(i, j)
				land += 1

	print(land)



