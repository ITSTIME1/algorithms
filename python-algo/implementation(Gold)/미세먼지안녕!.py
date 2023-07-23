# 음
# 확산의 정의가 정확힘 ㅝ지

# 결국 칸이 없다라는건 범위가 넘어간다는 얘기가 되고
# 확산이 그러면 겹쳐서 일어나게 된다는거 같은데
# 

# 

# 아 그래서 미세먼지 확산은 동시에 일어난다고 했구나
# 내가 생각한 방법은 한 방향에서만 확산한다음에
# 확산한 다음에 그 다음 확산을 생각했기 때문인거네
# 사실 동시에 확산된다면
# 동시에 먼지가 쌓여야 하는게 맞으니까
#아 ㅇㅋ

# 그러면 문제이해가 쉬워지지 와 이거 확산을 이해하지 못하면 못푸는 문제구만
import sys 
import copy
from collections import deque
input= sys.stdin.readline


r, c, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(r)]

ori = copy.deepcopy(board)
# 일단 확산부터 진행해야겠네
# 1초에 진행된게 확산, 청정기 둘다 진행되는거니까
# 초가 -1 씩 감소될때마다 진행해주어야 하는 부분이




def simul(i, j):    
    # 북 서 남 동
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cnt = 0
    for idx in range(4):
        nx = dx[idx][0] + i
        ny = dx[idx][1] + j
        
        if nx < 0 or nx >= r or ny < 0 or ny >= c or ori[nx][ny] == -1:
            continue
        
        # 그렇지 않은 부분들
        dust = ori[i][j] // 5
        board[nx][ny] += dust
        cnt += 1
    
    # 다끝나고나면
    # 이제 dust더한만큼 빼줘야되니까
    board[i][j] = board[i][j] - ((ori[i][j] // 5 ) * cnt)


for i in range(r):
    for j in range(c):
        # 공기청정기는 피하면서 and 미세먼지가 있는 곳
        if ori[i][j] != 0 and ori[i][j] != -1:
            # 확산  
            simul(i, j)    

print(board)

