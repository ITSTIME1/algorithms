from collections import deque
# 미로 탈출 문제


# 간단하게 미로를 탈출 하는 문제
# 우선 첫 시작 값은 1, 1 로 주어지고
# 최소로 이동하는 이동 횟수를 구하는 문제
# 우선 이 문제는 그래프가 2차원 행렬로 주어지고
# dx, dy 를 선언한 다음 하나씩 이동한다음
# 만약 dx, dy 모두가 다 1 이라면
# 값을 갱신시켜주고
# count를 올려주는 방식
# 문제 조건에서 처음 값과 마지막 값도 count 에 포함 시켜야 한다 라는 조건 떄문에[
# 마지막 N, M 에 도달 하여도 count 하여야 하고 
# 처음 1, 1 에서 부터 시작 할 때 도 count 하여야 한다.

# 근데 여기서 고려해야 되는건
# 미로를 벗어 나가는 경우는 없으므로
# 미로를 벗어 나가는 경우를 예외 처리를 해주어 야 한다.


N, M = map(int, input().split())
# 초기 값 설정
graph = []
# graph 에 입력 받은 행렬들 저장
for _ in range(N):
	graph.append(list(map(int, input())))


# 1로 시작하는 이유는 가장 처음 행렬을 놀릴때도
# 카운트를 세기 때문
def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	# dx 가로, dy 세로
	# 상하좌우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while queue:
		# 1,1 
		nx, ny = queue.popleft()
		for k in range(len(dx)):
			# 상도 돌고 하도 돌고 좌, 우 다돌아보자
			sx = nx + dx[k]
			sy = ny + dy[k]

			if (sx < 0 or sx >= N or sy < 0 or sy >= M):
				continue

			if(graph[sx][sy] == 1):
				print(graph[sx][sy])
				graph[sx][sy] = graph[nx][ny] + 1
				print(graph[sx][sy])
				queue.append((sx, sy))
			
			if(graph[sx][sy] == 0):
				continue
	return graph[N-1][M-1]

# 0 = 괴물이 있는 곳
# 1 = 괴물이 없는 곳
print(bfs(1, 1))