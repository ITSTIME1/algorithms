from collections import deque

def bfs(r, c, n, m, board):
    global goalX, goalY
    # 방문이 된 곳에는 숫자를 표시해주기 위해서 배열을 선언해준다.
    visited = [[0] * m for _ in range(n)]
    # 처음 bfs를 돌릴 시작위치는 로봇이 있는 위치이며, 첫시작을 했다는걸 알리기 위해서 1로 바꿔준다.
    visited[r][c] = 1
    queue = deque([[r, c]])
    
    answer = -1
    
    while queue:
        q = queue.popleft()
        x, y = q[0], q[1]
        
        # 목표지점에 도달했다면 목표지점가지의 거리를 리턴하면되는데
        # 만약 그런게 아니라면 그냥 while문만 종료될거니까
        if board[x][y] == "G":
            
            answer = visited[x][y] - 1
            break

        
        
        # 북 서 남 동으로 하면 값이 이상해지는데
        dx = [(-1, 0), (0, -1), (1, 0), (0, 1)] 
        
        for idx in range(4):
            nx, ny = x, y
            while True:
                nx += dx[idx][0]
                ny += dx[idx][1]
                # 만약 더 이상 가지 못하는 곳이라면
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                    nx -= dx[idx][0]
                    ny -= dx[idx][1]
                    break
            
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return answer
    
def solution(board):

    answer = 0
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                answer = bfs(i, j, n, m, board)
    return answer

[[5, 0, 4, 0, 2, 0, 1], 
 [0, 0, 3, 8, 3, 0, 2], 
 [6, 6, 0, 7, 0, 0, 0], 
 [0, 5, 4, 0, 5, 0, 8], 
 [7, 6, 0, 7, 6, 0, 7]]