# 문제분석
# 시계 방향으로 푸는건데
# 시뮬레이션이네

n = int(input())
find = int(input())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [[0 for _ in range(n)] for _ in range(n)]

x, y = 0, 0
board[x][y] = n*n

# 남
direction = 2
number = (n*n)-1
ansX, ansY = 0, 0
while True:
	# nx, ny 
	# 우선 direction 방향으로 x, y를 업데이트 해주고
	nx = x + dx[direction]
	ny = y + dy[direction]
	# 그럼 이 nx가 갈 수 잇는지 없는지 확인해야됨
	if nx > n-1 or nx < 0 or ny > n-1 or board[nx][ny] != 0:
		# 만약 이런 경우라면 방향을 바꿔야함
		direction -= 1
		if direction < 0:
			direction = 3
		# 방향을 바꾸고 
		# nx, ny 값을 업데이트하고
		# 그럼 새로운 좌표로 설정되었으니까
		nx = x + dx[direction]
		ny = y + dy[direction]
	# x, y 업데이트
	# 만약 업데이트 한 값의 number 값이 우리가 찾던 find 값이라면
	# ansX, ansY 에 좌표를 업데이트 해준다
	x, y = nx, ny
	board[x][y] = number
	if board[x][y] == find:
		ansX, ansY = x, y
	number -= 1
	if number <= 0:
		for i in board:
			print(*i, end = "\n")
		print(ansX+1, ansY+1)
		break
	# 수를 저장해주고

# [[49, 0, 0, 0, 0, 0, 0], 
# [48, 0, 0, 0, 0, 0, 0], 
# [47, 0, 0, 0, 0, 0, 0], 
# [46, 0, 0, 0, 0, 0, 0], 
# [45, 0, 0, 0, 0, 0, 0], 
# [44, 0, 0, 0, 0, 0, 36], 
# [43, 42, 41, 40, 39, 38, 37]]



# [[49, 26, 27, 28, 29, 30, 31], 
# [48, 25, 10, 11, 12, 13, 32], 
# [47, 24, 9, 2, 3, 14, 33], 
# [46, 23, 8, 1, 4, 15, 34], 
# [45, 22, 7, 6, 5, 16, 35], 
# [44, 21, 20, 19, 18, 17, 36], 
# [43, 42, 41, 40, 39, 38, 37]]