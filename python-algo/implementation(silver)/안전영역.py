import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]


# def dfs(r, c, arr, height, visited):
#     # 시작 지점부터 받게 되니까
#     # 그 시작지점부터 봐야하는데
#     # 상하좌우를 살펴봐야 될거 같은데
#     dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
#     for idx in range(4):
#         nx = dx[idx][0] + r
#         ny = dx[idx][1] + c
        
#         if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or arr[nx][ny] <= height:
#             continue
#         visited[nx][ny] = 1
#         dfs(nx, ny, arr, height, visited)
    
#     return

def bfs(r, c, arr, height, visited):
    queue = deque([[r, c]])
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    while queue:
        q = queue.popleft()
        x, y = q[0], q[1]

        for idx in range(4):
            nx = dx[idx][0] + x
            ny = dx[idx][1] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or arr[nx][ny] <= height:
                continue

            visited[nx][ny] = 1
            queue.append([nx, ny])
    
    return visited


# 아무 지역도 물에 안잠길 수 있다라는건
# 우선 물의 높이가 1이상으로 주어지기 때문에
# 만약 1이 주어졌다고 했을때도
# 아무지역도 물에 암잠기는 방법은
# 0이하일때지
# 즉 이때는 비가 내리지 않은 상황이고 그럴때는
# 어떠한 지역도 0보다 큰 상황이기 때문에
# 모두가 안전지역인거지
# 따라서 아무지역도 물에잠기지 않는다는건 전체가 안전지대라는 의미가 되고

# 만약 100이상이라고 했으니까
# 배열에서 가장 큰 값이 100까지 주어졌다고 했을때
# 100이 주어지면 모두 잠기게 된다. 왜냐하면 물의 높이가 가장 클때는 100이 주어졌을떄고
# 100이하의 값들을 전부 잠기기 때문에 100이라도 전부 잠기게 된다.
# 따라서 모든 지역이 잠긴다.
total = []
# 가장 작은 숫자를 기준으로 해보자
for height in range(max(map(max, arr))+1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] > height and not visited[r][c]:
                # dfs(r, c, arr, height, visited)
                visited[r][c] = 1
                visited = bfs(r, c, arr, height, visited)
                cnt += 1
    total.append(cnt)
print(max(total))


