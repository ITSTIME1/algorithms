import sys
input = sys.stdin.readline

# 방의 크기
r, c = map(int, input().split())

# 장애물의 개수
k = int(input())

board = [[0] * c for _ in range(r)]

if k != 0:
	for _ in range(k):
		x, y = map(int, input().split())
		board[x][y] = 'x'

# 방향을 가지고 있을 딕셔너리
# 1:상, 2:하, 3:왼, 4:오
dic = {1: (-1, 0), 
		2: (1, 0), 
		3: (0, -1), 
		4:(0, 1)}

# 시작위치
startX, startY = map(int, input().split())
# 시작위치를 표시
board[startX][startY] = 1

# 지정한 위치
pos = list(map(int, input().split()))


index = 0
currentPos = dic[pos[index]]

# 시뮬레이션
fail = 0
while True:
	# 그럼 현재 위치를 더해봤을때
	# 갈 수 있으면 이동하고 번호를 지정해주면 되겠다.
	nx = startX  + currentPos[0]
	ny = startY + currentPos[1]

	# 범위 내에 존재하고, 벽이 아니고, 이미 방문하지 않은 구간이라면
	# 지나갈 수 있기 때문에 현재 위치에서 1더해준다.
	# 이동한 위치로 변경해준다.
	if 0<=nx < r and 0 <= ny < c and board[nx][ny] == 0 and board[nx][ny] != 'x':
		fail = 0
		board[nx][ny] = board[startX][startY] + 1
		startX, startY = nx, ny

	else:
		index += 1
		index %= 4

		currentPos = dic[pos[index]]

		fail += 1
		if fail == 4:
			break


print(startX, startY)