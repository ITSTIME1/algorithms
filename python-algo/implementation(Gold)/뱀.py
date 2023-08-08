
import sys
from collections import deque
sys = sys.stdin.readline


n = int(input())
k = int(input())

board=[[0] * n for _ in range(n)]


for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2


check = {}
l = int(input())

for _ in range(l):
    t, dir = map(str, input().split())
    check[int(t)] = dir

def simul(s, e):

    dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 초기 방향
    dir = 0
    # 시간체크
    time = 0

    # time_list = [*check.keys()]
    body = deque([[s, e]])
    
    
    while True:
        nx = dx[dir][0] + s
        ny = dx[dir][1] + e
    
        if 0 <= nx < n and 0 <= ny < n and [nx, ny] not in body:

            if board[nx][ny] == 2:
                board[nx][ny] = 0
                body.append([nx, ny])
            # 사과가 아니라면
            elif board[nx][ny] == 0:

                if body:
                    body.append([nx, ny])
                    # 꼬리는 제거해주자
                    body.popleft()                    
                 
            # 좌표 갱신   
            s, e = nx, ny
            # 옮긴 다음에 시간 올리고
            time += 1
            
            if check.get(time) != None:
                d = check[time]

                if d == "L":
                    dir -= 1
                    if dir <= -5:
                        dir = -1
                else:
                    dir += 1
                    if dir >= 4:
                        dir %= 4
        else:
            time +=1
            # 벽밖으로 나간거니까 바로 종료
            break
    
    return time

a = simul(0, 0)

print(a)

            
            
        
    
[1,1,1,0]
[0,0,0,1]