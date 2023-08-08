import sys 
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
s = int(input())


# c * r
# 5 * 10
# 세로 * 가로
arr = [[0] * r for _ in range(c)]



def bfs(start, end, arr, shop, dic):
	oriX, oriY = start, end
	shoped = [0] * len(shop)
	visited = [[0] * r for _ in range(c)]
	# 상하좌우
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	first, second = 0, 0
	# 북 남 일 경우는 first, second 는 서, 동
	if dic == 1 or dic == 2:
		first, second = 2, 3

	# 서와 동쪽에 위치해 있다면 북 과 남으로 이동할거니까
	elif dic == 3 or dic == 4:
		first, second = 0, 1

	# 처음과 second에 대해서 두번의 연산을 진행하면 되지 않을까
	f, s = [0] * len(shop), [0] * len(shop)
	time, check = 1, 0
	while True:
		# 모든 상점을 다 찾았다면 그만
		if 0 not in shoped:
			break

		nx = dx[first][0] + start
		ny = dx[first][1] + end
		# 범위 안에 있다면
		if 0<= nx < c and 0 <= ny < r and visited[nx][ny] == 0:
			if [nx, ny] in shop:
				shoped[check] = 1
				visited[nx][ny] = 1
				start, end = nx, ny
				check += 1
				f[shop.index([nx, ny])] = time
				
			else:
				visited[nx][ny] = 1
				start, end = nx, ny
			time += 1
		else:
			time += 1
			# 방향을 찾는 방법이 필요한데.
			# 현재 범위가 넘어갔다면 그곳으로 가지 못한다는거고
			# 그럼 다른 방향을 찾아야하는거니까
			# 갈 수 있는 방향을 찾아야하는데 상하좌우로 찾으면 될거 같은데
			for idx in range(4):
				newX = dx[idx][0] + start
				newY = dx[idx][1] + end

				# 갈수 있는 범위 내라면 그 방향을 선택한다.
				if 0<= newX < c and 0<= newY < r and visited[newX][newY] == 0:
					first = idx
					break
	shoped = [0] * len(shop)
	visited = [[0] * r for _ in range(c)]
	time, check = 1, 0
	start, end = oriX, oriY
	while True:

		# 모든 상점을 다 찾았다면 그만
		if 0 not in shoped:
			break

		nx = dx[second][0] + start
		ny = dx[second][1] + end
		# 범위 안에 있다면
		if 0<= nx < c and 0 <= ny < r and visited[nx][ny] == 0:
			if [nx, ny] in shop:
				shoped[check] = 1
				visited[nx][ny] = 1
				start, end = nx, ny
				check += 1
				s[shop.index([nx, ny])] = time
			else:
				visited[nx][ny] = 1
				start, end = nx, ny
			time += 1
		else:
			time += 1
			# 방향을 찾는 방법이 필요한데.
			# 현재 범위가 넘어갔다면 그곳으로 가지 못한다는거고
			# 그럼 다른 방향을 찾아야하는거니까
			# 갈 수 있는 방향을 찾아야하는데 상하좌우로 찾으면 될거 같은데
			for idx in range(4):
				newX = dx[idx][0] + start
				newY = dx[idx][1] + end

				# 갈수 있는 범위 내라면 그 방향을 선택한다.
				if 0<= newX < c and 0<= newY < r and visited[newX][newY] == 0:
					second = idx
					break
	total = 0
	for i in range(len(shop)):
		if f[i] > s[i]:
			total += s[i]
		else:
			total += f[i]
	print(total)

shop = [] 
sX, sY = 0, 0
for i in range(s+1):
	dic, val = map(int, input().split())

	if i == s:
		# 북 or 남
		if dic == 1 or dic == 2:
			if dic == 1:
				arr[0][val-1] = 1
				sX, sY = 0, val-1
			else:
				arr[c-1][val-1] = 1
				sX, sY = c-1, val-1
	
		# 서 or 동
		elif dic == 3 or dic == 4:
			if dic == 3:
				arr[val-1][0] = 1
				sX, sY = val-1, 0
	
			else:
				arr[r-1][val-1] = 1
				sX, sY = r-1, val-1

		# 어짜피 주인공은 마지막에 주어지니까
		# 마지막에 bfs돌리고 끝내면 되는거지
		bfs(sX, sY, arr, shop, dic)
		continue
	else:
		# 북 or 남
		if dic == 1 or dic == 2:
			if dic == 1:
				shop.append([0, val-1])
			else:
				arr[c-1][val-1] = 1
				shop.append([c-1, val-1])
			
		# 서 or 동
		elif dic == 3 or dic == 4:
			if dic == 3:
				shop.append([val-1, 0])
	
			else:
				shop.append([r-1, val-1])



# 시간복자도 상 터진다..



