음료수 얼려 먹기.py
# N = 세로, M = 가로
N, M = map(int, input().split())

graph = []
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))


def dfs(i, j):
    # 방문처리
    graph[i][j] = 1
    # 방문처리한 노드 와 인접된 노드를 상하좌우를
    # 통해서 검사를 하고
    # 검사한 그 값이 기준점을 넘어간다면
    # 업데이트한 그 값이 기준값을 넘어 가지 않는다면
    # 그 업데이트한 nx, ny 값이 0 인지 확인하고 0 이라면 계속 dfs 시전
    for k in range(len(dx)):
        nx = i + dx[k]
        ny = j + dy[k]
        if (nx >= 0 and nx < N and ny >= 0 and ny < M):

            # 인접 노드에 음료수를 채울 수 있는지 확인
            if (graph[nx][ny] == 0):

                # 인접 노드 방문
                dfs(nx, ny)


for i in range(N):
    for j in range(M):
        if (graph[i][j] == 0):
            dfs(i, j)
            result += 1

print(result)
