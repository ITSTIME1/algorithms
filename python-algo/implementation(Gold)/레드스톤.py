

# 맞았땅
import sys
from collections import deque
input = sys.stdin.readline


w, h = map(int, input().split())
n = int(input())

board = [[[0, 0] for _ in range(w)] for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]
# block = 1
# dust = 2
# lamp = 3


lamp = []
for i in range(n):
    name, x, y = input().split()
    x, y = int(y), int(x)
    a = name.split("_")
    if a[1] == "block":
        board[x][y] = [1, 15]
    
    elif a[1] == "dust":
        board[x][y] = [2, 0]
    
    elif a[1] == "lamp":
        board[x][y] = [3, 0]
        lamp.append([x,y])


def bfs(i, j):
    queue = deque([[i, j]])
    
    visited[i][j] = True
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    # j, i니까
    # j = y (세로)
    # i = x (가로)
    while queue:
        q = queue.popleft()
        # 먼지라면
        # 해당 큐에서 꺼낸게 이제 먼지라면 돌리는게 다르지
        if board[q[0]][q[1]][0] == 2:
            for i in range(4):
                nx = dx[i][0] + q[0]
                ny = dx[i][1] + q[1]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                
                # 이제 그게 램프인지 더스트인지
                # 램프인데 만약 전기신호가
                # 더 크다면 큐에 넣지 않음
                if board[nx][ny][0] == 3:
                   # 켜지지 않은 램프니까 켜줘야지
                   visited[nx][ny] = True
                   board[nx][ny][1] = board[q[0]][q[1]][1]-1

                # 만약 그게 dust라면 
                # 레드스톤 블럭에게 전기신호를 전달한다
                elif board[nx][ny][0] == 2:
                    # 전기신호가 크면 무시하고
                    if board[nx][ny][1] > board[q[0]][q[1]][1] or board[q[0]][q[1]][1] - 1 <= 1:
                        continue
                        
                    
                    # 전기신호가 작다면 현재 전기신호에서 -1해서 전달함]
                    board[nx][ny][1] = board[q[0]][q[1]][1] - 1
                    
                    queue.append([nx, ny])
                    

                # 레드스톤 블럭이라면
                elif board[nx][ny][0] == 1: continue

                # 0인구간 맨땅인구간에도 전기신호는 저장해주어야 하니까
                else:
                  board[nx][ny][1] = board[q[0]][q[1]][1] - 1
            
        
        # 레드스톤 블럭이라면
        elif board[q[0]][q[1]][0] == 1:
            # (1, 15)
            x, y = q[0], q[1]
            for i in range(4):
                nx = dx[i][0] + x
                ny = dx[i][1] + y

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                # 이제 그게 램프인지 더스트인지
                # 만약 램프라면 불을 켜버리면 되는거지
                if board[nx][ny][0] == 3:
                    visited[nx][ny] = True
                    board[nx][ny][1] = 15

                # 만약 그게 dust라면 
                # 레드스톤 블럭에게 전기신호를 전달한다
                elif board[nx][ny][0] == 2:
                    queue.append([nx, ny])
                    board[nx][ny][1] = 15

                # 레드스톤 블럭이라면
                elif board[nx][ny][0] == 1: 
                    continue

                # 0인구간 맨땅인구간에도 전기신호는 저장해주어야 하니까
                else:
                    board[nx][ny][1] = 15
                

for i in range(h):
    for j in range(w):
        # 레드스톤 블럭이라면
        if board[i][j][0] == 1:
            bfs(i, j)
            
            
cnt = 0
for i in lamp: 
    if visited[i[0]][i[1]] == True:
        cnt += 1


if cnt == len(lamp):
    print("success")
else:
    print("failed")
    


