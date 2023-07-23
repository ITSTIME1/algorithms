# 이 문제를 풀어보자 이제 코드로 구현해보는거야
# 일단 재귀로 풀어보고 그다음에 리스트로 풀어보자

# 인접행렬 & 재귀
# n, m = map(int, input().split())

# arr = [list(map(int, input())) for _ in range(n)]


# def dfs(x, y):
# 	dt = [-1, 1, -1, 1]
# 	# 상 : 행 감소
# 	# 하 : 행 증가
# 	# 좌 : 열 감소
# 	# 우 : 열 증가
# 	if x <= -1 or x >= n or y <= -1 or y >=m:
# 		return False
# 	# 일단 상하좌우를 검사해야되는데
# 	# 해당 정점에서 부터 시작해서
# 	# 그 값이 0이니까 그 값을 보내주고
# 	# 해당 정점에서 부터 상 하 좌 우 하려면
# 	# 방향백터가 있으면 좋겠는데
# 	if arr[x][y] == 0:
# 		arr[x][y] = 1
# 		# 상
# 		dfs(x+dt[0], y)
# 		# 하
# 		dfs(x+dt[1], y)
# 		# 좌
# 		dfs(x, y+dt[2])
# 		# 우
# 		dfs(x, y+dt[3])
# 		return True
# 	else:
# 		return False

# cnt = 0
# for i in range(n):
# 	for j in range(m):
# 		# dfs 를 돌리는거야
# 		if arr[i][j] == 0:
# 			if dfs(i, j) == True:
# 				cnt += 1

# print(cnt)

# 조금더 명쾌하게 설명했으면 좋겠는데 내가 아는 부분과 헷갈리는 부분을

# dfs 기본 형태를 외우는것도 하나의 방법이겠지만 모든 문제가 dfs 기본형태처럼 나오는건 아니기 때문에
# 외워서 풀기엔 한계가 있따

# 인접행렬 & 스택
from collections import deque
# 디큐를 이용해서 인접행렬 & 리스트를 stack을 이용해서 할 수 있나?
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

# 시뮬레이션 + dfs
# dequeue 사용법을 좀 제대로 알아야 될것 같고
# 재귀와 스택의 활용성을 좀 더 공부해 봐야 dfs 를 풀 수 있을 것 같다
def dfs(i, j):
	stack = deque([(i, j)])
	arr[i][j] = 1
	# 상 하 좌 우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	# 더이 상 방문할게 없을때까지
	while stack:
		x, y = stack.popleft()
		# 이렇게 상하 좌우를 탐색한다면
		# 4*5 니까
		# 왜 이게 이렇게 되는거야ㅅㅂ ㅅㅂ ㅅㅂ ㅅㅄㅄ
		for i in range(len(dx)):
			nx = x+dx[i]
			ny = y+dy[i]
			# 만약 해당 범위가 넘어간다면 그냥 넘기면 되고
			# 0이 아닌 부분은 구할 필요가 없으니까 그냥 패스하면 되고
			if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
				continue
			# 만약 그래프에서 탐색하는 부분이 0 이라면
			# 탐색해야 되는 부분이므로
			if arr[nx][ny] == 0:
				arr[nx][ny] = 1
				stack.append((nx, ny))

	# 만약 더 이상 탐색할 부분이 없다면
	return arr




cnt = 0
for i in range(n):
	for j in range(m):
		# 한번 정점을 돌때 graph 를 최신화 시켜주어야 다음 그래프에서 착오가 없다
		# 한 정점에대 해서 먼저 탐색을 진행하는거니까
		# 그 정점에서 시작해서 모든 탐색해야 되는 부분을 스택에 넣을거고
		# 그 스택에서 더 이상 탐색해야 되는 부분이 없게 된다면
		# graph 를 최신화 시켜주고
		# 해당 dfs 값의 arr 변화된 값을 최신화 시켜주고
		# 얼음면적의 개수를 세면..?
		if arr[i][j] == 0:
			dfs(i, j)
			cnt += 1

print(cnt)