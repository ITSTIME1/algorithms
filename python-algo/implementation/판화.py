import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

# 수직, 수평
# 깊은 복사
board = [[[0, 0] for _ in range(n)] for _ in range(n)]


# 이동경로
path = deque(input().rstrip())

# 방향
direction = {'U': (-1, 0),'R':(0, 1), 'L':(0,-1), 'D':(1, 0)}


startX, startY = 0, 0

while path:
	p = path.popleft()
	nx = startX + direction[p][0]
	ny = startY + direction[p][1]


	if 0<= nx < n and 0<= ny < n:
		# 수직
		if p == 'U' or p == 'D':
			# 0,0, 1, 0
			board[startX][startY][0] = 1
			board[nx][ny][0] = 1
		# 수평이니까
		elif p == 'R' or p == 'L':
			board[startX][startY][1] = 1
			board[nx][ny][1] = 1

		startX, startY = nx, ny
	else:
		continue

for i in range(n):
	for j in range(n):
		# 수직 수평 모두 1이면
		if board[i][j][0] == 1 and board[i][j][1] == 1:
			board[i][j] = "+"

		elif board[i][j][0] == 1 and board[i][j][1] == 0:
			board[i][j] = "|"


		elif board[i][j][0] == 0 and board[i][j][1] == 1:
			board[i][j] = "-"
		else:
			board[i][j] = "."

for i in board:
	print("".join(i), end="\n")