import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

board = [list(map(str, input().strip())) for _ in range(N)]
# 상하좌우
board_copy = copy.deepcopy(board)
dx = [(-1, 0), (1, 0), (0,-1),(0,1)]
def dfs(i, j, what, board, stand):
	# 색약인 사람 
	board[i][j] = 'X'
	if what == "yes":
		# i, j부터 검사할거고 
		# 색약인 사람들은 R이라면 G도 같은 색상으로 취급해야 되기 때문에
		for index in range(4):
			nx = dx[index][0] + i
			ny = dx[index][1] + j
			# 범위 안에 들고 기준 색상이라면	
			if 0<= nx < N and 0 <= ny < N:
				# R을 검사하고 있다면
				if stand == "R" and (board[nx][ny] == stand or board[nx][ny] == 'G'): 
					board[nx][ny] = 'X'
					dfs(nx, ny, what, board, stand)
				elif stand == "G" and (board[nx][ny] == stand or board[nx][ny] == 'R'):
					board[nx][ny] = 'X'
					dfs(nx, ny, what, board, stand)
				elif stand == "B" and board[nx][ny] == stand:
					board[nx][ny] = 'X'
					dfs(nx, ny, what, board, stand)
			else:
				continue

	# 색약이 아닌 사람
	else:
		# i, j부터 검사할거고 
		for index in range(4):
			nx = dx[index][0] + i
			ny = dx[index][1] + j
			# 범위 안에 들고 기준 색상이라면	
			if 0<= nx < N and 0 <= ny < N:
				if board[nx][ny] == stand:
					board[nx][ny] = 'X'
					dfs(nx, ny, what, board, stand)

			else:
				continue
	return board
# 0은 색약, 1은 색약x
count = {"R":[0, 0], "B":[0, 0], "G":[0,0]}

# 색약 아닌사람
for i in range(N):
	for j in range(N):
		# R,G,B중하나라면
		if board[i][j] != "X":
			stand = board[i][j]
			board = dfs(i, j, 'no', board, stand)
			count[stand][1] += 1

# 색약인 사람
for i in range(N):
	for j in range(N):
		# R,G,B중하나라면
		if board_copy[i][j] != "X":
			stand = board_copy[i][j]
			board_copy = dfs(i, j, 'yes', board_copy, stand)
			count[stand][0] += 1 

a = 0
b = 0
for v in count.values():
	a  += v[1]
	b  += v[0]

print(a, b)
