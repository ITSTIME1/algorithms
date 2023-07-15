
import sys
from collections import deque
input = sys.stdin.readline

# m이 가로고 n이 세로니까
m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

def bfs(first_queue):
    # 그럼 무한루프가 돌텐데
    # 계속 추가해서
    # 아 뭔지 알겠따
    # bfs에 들어가는 큐가 관련된게 먼저 들어가서 그러네
    # 그렇게 익은 사과들만 우선적으로 넣어져야 하니까 아..
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while first_queue:
        q = first_queue.popleft()
        x, y = q[0], q[1]
        
        for idx in range(4):
            nx = dx[idx][0] + x
            ny = dx[idx][1] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or box[nx][ny] == -1:
                continue
        
            # 익지 않은 상태라면
            # 익지 않은 상태이면서 그쪽을 방문을 안한곳
            if box[nx][ny] == 0:
                first_queue.append([nx, ny])
                box[nx][ny] = box[x][y] + 1

first_queue = deque([])


for i in range(n):  
    for j in range(m):
        # 익은 토마토일때
        # 익은 토마토인데 또 방문되면 이상하자나
        if box[i][j] == 1:
            first_queue.append([i, j])


bfs(first_queue)


cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            cnt += 1

# 다 돌았는데도 익지 않은 사과가 있다면    
if cnt != 0:
    print(-1)
else:
    print(max(map(max, box))-1)


# [[1, -1, 7, 8, 9, 10], 
#  [2, -1, 6, 7, 8, 9], 
#  [3, 4, 5, 6, -1, 10], 
#  [4, 5, 6, 7, -1, 1]]

# [[1, -1, 7, 6, 5, 4], 
#  [2, -1, 6, 5, 4, 3], 
#  [3, 4, 5, 6, -1, 2], 
#  [4, 5, 6, 7, -1, 1]]

