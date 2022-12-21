
# 달팽이 채우기 문제 같다
C, R = map(int, input().split())

arr = [[0 for _ in range(C)] for _ in range(R)]
k = int(input())

# 음 시뮬레이션 유형
# # 북 동 남 서 good
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pos = 0
num = 1

if C*R < k:
	print(0)
	exit()


x, y = R-1, 0
while True:
	if num == k:
		print(y+1, R-x)
		break

	arr[x][y] = num
	nx = x + dx[pos]
	ny = y + dy[pos]

	if nx < 0 or ny < 0 or nx >= R or ny >= C or arr[nx][ny] != 0:
		pos += 1
		if pos == 4:
			pos = 0

		nx = x + dx[pos]
		ny = y + dy[pos]

	x, y = nx, ny
	num += 1
# [[6, 7, 8, 9, 10, 11, 12], 
# [5, 26, 27, 28, 29, 30, 13], 
# [4, 25, 38, 83, 84, 31, 14], 
# [3, 24, 37, 86, 85, 32, 15], 
# [2, 23, 36, 35, 34, 33, 16], 
# [1, 22, 21, 20, 19, 18, 17]]

# 달팽이관을 생각하기 까다로웠던거 같은데