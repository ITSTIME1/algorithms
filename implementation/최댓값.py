N = 9
# N * N
board = [list(map(int, input().split())) for _ in range(N)]

max_num = board[0][0]
h = 0
y = 0
for i in range(len(board)):
	for j in range(N):
		if board[i][j] > max_num:
			h = i
			y = j
			max_num = board[i][j]

print(max_num)
print(h+1, y+1)	