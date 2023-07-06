import sys
from collections import deque
input = sys.stdin.readline


# 톱니바퀴 개수
t = int(input())
# T개의 톱니바퀴 받기
top = [deque(list(map(int, input().strip()))) for _ in range(t)]

# 회전수 
k = int(input())
# 회전할때마다 돌릴 번호와 & 방향
src = deque(tuple(map(int, input().strip().split())) for _ in range(k))


def dfs(number, direction, check):
    # 여기서 가장 우선시 되어야 하는건 return조건
    # number 값은 = 돌린 바퀴
    # number - 1 or number + 1이 다음 검사할 바퀴
    if check == "l":
        # 왼쪽이라면 number는 right[index]를 참조하고 6
        # number-1 은 left[index]를 참조 2
        if right[number] == left[number-1]:
            return
        
        # 방향에 따라반대방향으로
        if direction == -1:
            top[number-1].rotate(1)
            direction = 1
        else:
            top[number-1].rotate(-1)
            direction = -1
            
        # 왼쪽으로가면 0이나오니가 
        
        if number-1 == 0:
            return    
            
        dfs(number-1, direction, "l") 
        
        
           
    elif check == "r":
        # 왼쪽이라면 number는 right[index]를 참조하고 6
        # number-1 은 left[index]를 참조 2
        if left[number] == right[number+1]:
            return
        
        # 방향에 따라반대방향으로
        if direction == -1:
            top[number+1].rotate(1)
            direction = 1
        else:
            top[number+1].rotate(-1)
            direction = -1
            
        # 왼쪽으로가면 0이나오니가 
        
        if number+1 == t-1:
            return
        dfs(number+1, direction, "r")
        
        
        
    elif check == "first":
        if left[number] == right[number+1]:
            return
        # 방향에 따라반대방향으로
        if direction == -1:
            top[number+1].rotate(1)
            direction = 1
        else:
            top[number+1].rotate(-1)
            direction = -1
            
        if number+1 == t-1:
            return
        
        dfs(number+1, direction, "first")
        
        
        
    elif check == "last":
        if right[number] == left[number-1]:
            return
        
        # 방향에 따라반대방향으로
        if direction == -1:
            top[number-1].rotate(1)
            direction = 1
        else:
            top[number-1].rotate(-1)
            direction = -1


        if number-1 == 0:
            return 
    
        dfs(number-1, direction, "last")
        
        
        

while k > 0:
    left = [i[2] for i in top]
    right = [i[6] for i in top]
    
    d = src.popleft()
    # 회전해야되는 바퀴와, 그때의 방향
    num, dir = d[0], d[1]
    
    # 처음이든 중간이든 마지막이든
    # 회전시킬 바퀴가 처음 회전한다.
    if dir == -1:
        top[num-1].rotate(-1)
    else:
        top[num-1].rotate(1)
    
    
    # 처음 or 마지막
    if num-1 == 0 or num-1 == t-1:
        if num - 1 == 0:
            # 구현
            dfs(num-1, dir, "first")

        elif num -1 == t-1:
            # 구현
            dfs(num-1, dir, "last")

    else:
        # 구현
        # 왼, 오른쪽을 판단해야됨
        dfs(num-1, dir, "l")
        dfs(num-1, dir, "r")

    k-= 1
    
print(len([i[0] for i in top if i[0] == 1]))