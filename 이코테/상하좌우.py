import time 
start = time.time()
N = int(input())
input_data = list(input().split())
# x = 열 (세로)
# y = 행 (가로)
x, y = 1, 1

# ex 5
data_type = ["L", "R", "U", "D"]

for i in range(len(input_data)):

    # 오른쪽
    if input_data[i] == data_type[1]:
        y += 1
        print(y)
    # 왼쪽    
    elif input_data[i] == data_type[0]:
        y -= 1
        print(y)
    # 위    
    elif input_data[i] == data_type[2]:
        up_x = x - 1
        if up_x < 1:
          continue
    # 아래
    elif input_data[i] == data_type[3]:
        x += 1
        print(x)

        # 예외처리
    if (x < 1 or x > N or y < 1 or y > N):
        continue

print(x, y)
print("time : {:.2f}".format(time.time() - start))

# 다른 사람 풀이
import time 
start = time.time()
n = int(input())
roots = list(input().split())
x,y = 1,1

#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

for root in roots: #이동 계획 하나씩 확인
    for i in range(len(move)): #이동 후 좌표 구하기
        if root == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx<1 or ny<1 or nx>n+1 or ny>n+1:
        continue #무시
    
    x,y = nx,ny #이동  
        
                
# print()
print(x,y)
print("time : {:.2f}".format(time.time() - start))