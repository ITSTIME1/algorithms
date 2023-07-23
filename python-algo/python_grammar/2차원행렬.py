from collections import deque
# 1은 이동 가능 
# 0은 이동 불가능
# 1, 1 에서 출발
# 지나야 하는 최소한의 칸수 
# 시작 위치와 도착 위치도 계산에 포함한다
# ex) (5, 6) 가로x세로에 도착하면
# 최소 개수
# 붙어서 입력 된다는건 split()구분 지어서 입력 받지 말라는 것이죠

N, M = map(int, input().split())
x, y = 1, 1
graph = []
for _ in range(N):
	graph.append(list(map(int, input())))





def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	
	# 가로 세로
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while queue:
		nx, ny = queue.popleft()


		
		for i in range(len(dx)):
			cx = nx + dx[i]
			cy = ny + dy[i]
			# 범위를 벗어나는 경우는 예외처리 해주어야 하고
			# 이때 N, M에 도달 했을 때 더이상 돌지 않도록 빠져 나와야 함
			if(cx < 0 or cx >= N or cy > 0 or cy >= M):
				continue

			if(graph[cx][cy] == 1):
				graph[cx][cy] = graph[nx][ny] + 1
				queue.append((cx, cy))

			if graph[cx][cy] == 0:
				continue

	return graph[N-1][M-1]

print(bfs(0, 0))

