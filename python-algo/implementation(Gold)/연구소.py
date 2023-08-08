import sys
from collections import deque
import copy
input = sys.stdin.readline


# 세로, 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    # 우선 2인 곳을전부 넣어주고 2인곳만 돌면도니까
    global result
    
    dequeue = copy.deepcopy(queue)
    board = copy.deepcopy(arr)

    # visited = [[0] * m for _ in range(n)]
        
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]    

    while dequeue:
        x, y = dequeue.popleft()
        for idx in range(4):
            nx = dx[idx][0] + x
            ny = dx[idx][1] + y
            # 범위 를 벗어나지 않고 방문을 안했다면
            if 0<= nx < n and 0 <= ny < m:
                # 그리고 그게 0이라면 즉 빈칸이라면
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    dequeue.append([nx, ny])
    # 그렇게 bfs가 다 킅났으면
    # 바로 0 ㅡ이개수 찾는 방법이이 있을텐데
    cnt = sum(row.count(0) for row in board)

    result = max(result, cnt)

# 벽을 찾을건데

def find(count):
    # 벽이 다 세워졌으면 이제돌거야
    if count == 3:
        bfs()
        return

    # 3개가 안됬으면 벽을 계속 찾아
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                # 이걸 이렇게 재귀로 할 수 있구나
                # 백트래킹 + bfs
                find(count + 1)
                arr[i][j] = 0


queue = deque([])
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            queue.append([r, c])
result = 0
find(0)
print(result)

# 벽을 일단 세워야 하는데
# 벽이 3개니까 고정 시키는방법은?
# 접근은 맞네
# 벽을 먼저 세우고
# 귿 ㅏ음에 bfs호출
# 접근이 맞긴한데 규현이 아노디네


# 그렇기 떄문에
# 벽을 만들어주면
# 즉 3개의 벽이 다 세워지면 bfs를 통해서 다 퍼트려주는거지

# 1. 벽을만든다.
# 2. 바이러스 퍼트린다.
