from collections import deque

def bfs(s, e, gx, gy, n, m, maps):
    visited = [[0] * m for _ in range(n)]
    visited[s][e] = 1
    queue = deque([[s, e]])
    
    result = 0
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while queue:
        q = queue.popleft()
        x, y = q[0], q[1]

        isActive = True
        for idx in range(4):
            nx = dx[idx][0] + x
            ny = dx[idx][1] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] != 0 or maps[nx][ny] == "X":
                continue
            
            if nx == gx and ny == gy:
                visited[nx][ny] = visited[x][y] + 1
                result = visited[nx][ny]
                isActive = False
                break
            
            else:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
        if not isActive:
            break

    return result

def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    
    startX, startY = 0, 0
    leverX, leverY = 0, 0
    goalX, goalY = 0, 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                startX, startY = i, j
            elif maps[i][j] == "L":
                leverX, leverY = i, j
                
            elif maps[i][j] == "E":
                goalX, goalY = i, j
    
    one = bfs(startX, startY, leverX, leverY, n, m, maps)
    two =  bfs(leverX, leverY, goalX, goalY, n, m, maps)

    if one > 0 and two > 0:
        answer =  (one + two) - 2
        
    
    return answer