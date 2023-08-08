import sys
input = sys.stdin.readline


r, c, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]


# 상하좌우
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 초기 폭탄 위치
boomb = [[i, j] for i in range(r) for j in range(c) if arr[i][j] == "O"]
# for i in range(r):
# 	for j in range(c):
# 		if arr[i][j] == "O":
# 			boomb.append([i, j])

time = 0
while time <= n:

	# 0초와 1초는 가만 있으니까
	if time == 0 or time == 1: 
		time += 1
		continue

	# 2때 채우고, 3때터트리고, 4때 채우고
	# 짝수일때와 홀수 일때 역할이 다르네
	# 터트리는건 이전 폭탄 위치를 터트린다.
	if time % 2 == 0:
		# 여기서는 채워야 하니까
		# 채운지점을 boomb에 넣어준다.
		# 빈칸인 곳을 채워야하니까
		# 채워야 된다는건 .이걸 다 채우면되니까
		arr = [['O' if arr[i][j] == '.' else arr[i][j] for j in range(c)] for i in range(r)]

		# for i in range(r):
		# 	for j in range(c):
		# 		if arr[i][j] == ".":
		# 			arr[i][j] = "O"
		# print(arr)

	elif time % 2 == 1:
		# 폭탄을 터트려준다.
		# 터트려 주기만 하면되겠네.
		while boomb:
			x, y = boomb.pop()
			arr[x][y] = "."

			for idx in range(4):
				nx = dx[idx][0] + x
				ny = dx[idx][1] + y
				# 범위가 넘어가지 않는 선에서 
				# 인접한 공간은 터트리는데
				# 폭탄이 있는 구역도 터트리게 되고
				if 0<= nx < r and 0 <= ny < c:
					if arr[nx][ny] == "O":
						arr[nx][ny] = "."

		boomb = [[i, j] for i in range(r) for j in range(c) if arr[i][j] == "O"]
		# for i in range(r):
		# 	for j in range(c):
		# 		if arr[i][j] == "O":
		# 			boomb.append([i, j])


	time += 1


for i in arr:
	print("".join(i), end="\n")

# [['O', 'O', 'O', '.', 'O', 'O', 'O'], 
# ['O', 'O', '.', '.', '.', 'O', 'O'], 
# ['O', 'O', 'O', '.', '.', '.', 'O'], 
# ['.', '.', 'O', 'O', '.', 'O', 'O'], 
# ['.', '.', '.', 'O', 'O', 'O', 'O'], 
# ['.', '.', '.', 'O', 'O', 'O', 'O']]

