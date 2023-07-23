from collections import deque

def bfs(s, e, maps, visited, n, m):
    visited[s][e] = 1
    
    queue = deque([s, e])
    
    total = 0
    
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while queue:
        q = queue.popleft()
        x, y = q[0], q[1]
    
        for idx in range(4):
            nx = dx[idx][0] + x
            ny = dx[idx][1] + y
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1 or maps[nx][ny] == "X": continue
            
            visited[nx][ny] = 1
            queue.append([nx, ny])
            total += int(maps[nx][ny])
    
    
    return total
            
            
    


def solution(maps):
    answer = []
    # 그러면 bfs로 방문한 지점의 식량을 세어서
    # bfs가 한번 끝날때마다 갈 수 있는 지점의 섬들의 최대 머물 수 있는 수는 가져온거니까
    # bfs끝나면 answer에 저장하자
    
    # x : 바다
    # digit : 식량
    
    maps = [list(i) for i in maps]
    
    
    n = len(maps)
    m = len(maps[0])
    

    visited = [[0] * m for _ in range(n)]
    total = []
    for i in range(n):
        for j in range(m):
            # 바다가 아니고 방문을 안했다면
            if maps[i][j] != "X" and visited[i][j] == 0:
                a = bfs(i, j, maps, visited, n, m)
                total.append(a)
    
    print(total)
    
solution(["X591X","X1X5X","X231X", "1XXX1"]	)