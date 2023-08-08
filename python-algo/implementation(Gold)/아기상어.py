import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# bfs를 통해서
# 거리가 최소가 되는 물고기를 찾는다.
# 거리가 최소가 되는 물고기를 찾기 위해서 최단경로 알고리즘을 사용
# 비용이 없으니 bfs의 최단경로를 이럴때 활용하는게 좋겠다.
def bfs(s, e, arr, shark):
	# 방문을 했는지 안했는지를 설정해서
	# 먹을 수 있는 곳을 다시 재방문하지 않는다. 처리를 해주어야 다시 재방문하지 않으니까
	distance = [[0] * n for _ in range(n)]
	visited = [[0] * n for _ in range(n)]

	visited[s][e] = 1
	queue = deque([[s, e]])
	# 상하좌우 이동 방향 정의
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
	# 그럼 이제 최적의 경로룰 찾아야하니까
	fish = []
	while queue:

		x, y = queue.popleft()

		for idx in range(4):
			nx = dx[idx][0] + x
			ny = dx[idx][1] + y

			# 범위는 벗어나지 않으면서 방문하지 않은곳
			if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
				
				# 그러면서 현재 방문하는게 샤크 크기보다 작거나 같다면
				# 작거나 같은 구간만 갈 수 있으니까
				if arr[nx][ny] <= shark:
					queue.append([nx, ny])
					visited[nx][ny] = 1
					distance[nx][ny] = distance[x][y] + 1

					# 그곳이 빈칸이 아니면서 상어가 먹을 수 있는 구간이라면
					# 좌표, 거리 값을 fish에 넣어준다.
					# 먹을 수 있다고해서 바로 먹어버리면 
					# 모든 먹을 수 있는 곳들을 다 먹어 버리니까 그렇게 하면안됨.
					if 0 < arr[nx][ny] < shark:
						fish.append([nx, ny, distance[nx][ny]])

	# 이제 최소값을 기준으로 정렬할건데
	# 우선 거리가 가장 작은 값을 볼거고 거리가 작은 값들이 여러개라면 x가 가장 작은걸 볼거고
	# 그러한 아이들도 많다면 y가 가장 작은걸 리턴할것이다.
	result = sorted(fish, key=lambda x : (-x[2], -x[0], -x[1]))

	return result



# 여러번 돌려야 하니까
shark = 2
cnt = 0
startX, startY = 0, 0

result = 0
for i in range(n):
	for j in range(n):
		if arr[i][j] == 9:
			startX, startY = i, j
			break

while True:
	# bfs를 돌려서 최적의 하나를 찾고
	# [x, y, distance]
	fish = bfs(startX, startY, arr, shark)

	# 만약 더 이상 먹을 물고기가 없다면 종료
	
	if not fish: break

	fx, fy, dist = fish.pop()

	cnt += 1
	if shark == cnt:
		shark += 1
		# 상어와 같다면 그 상어의 크기를 올려주고
		# 이후에 다시 그 만큼 먹는걸 체크해야 하니까 0으로 변경해준다.
		cnt = 0

	# 엄마의 도움없이 온전히 먹은 횟수만
	result += dist
	# 먹은 상어의 위치는 변경해주어야지.
	# 먹은 위치를 변경해주고 원래 시작했던 위치도 변경해준다.
	# 상어 위치니까 더 이상 거기는 상어 위치가 아니자나.
	# 물고기가 있는 위치도 아니니까
	arr[startX][startY], arr[fx][fy] = 0, 0

	# 그리고 먹은 위치로 이동을 해주어야 하기때문에
	# 이후에 bfs를 할때는 이동한 위치에서부터 시작해서 거리를 계산한다.
	startX, startY = fx, fy

print(result)


