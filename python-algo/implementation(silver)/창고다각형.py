# import sys 
# input = sys.stdin.readline

# n = int(input())

# d = [(0, 0) for _ in range(10001)]

# for i in range(n):
#     l, h = map(int, input().split())
#     d[l] = (l, h)

# height = d[0][1]
# idx = 0
# for i in range(len(d)):
#     if d[i][1] > height:
#         idx = i
#         height= d[i][1]

# height = d[0][1]
# total = 0
# for i in range(idx):   
#     if d[i][1] <= height:
#         total += height
#     else:
#         height = d[i][1]
#         total += height
        

# height = d[len(d)-1][1]
# for i in range(len(d)-1, idx, -1):
#     if d[i][1] <= height:
#         total += height
#     else:
#         height = d[i][1]
#         total += height

# print(total + d[idx][1])

# 2 * 4 = 8
# 4 * 6 = 24 = 32


# 2 * 8 = 16 
# 2 * 8 = 16

# 32 + 32 = 64
# 3 * 8 = 24 
# 88 + 10 = 98
import sys 
input = sys.stdin.readline

n = int(input())


arr = []
for i in range(n):
    l, h = map(int, input().split())
    arr.append([l, h])
    
arr = sorted(arr, key=lambda x : (x[0], x[1]))

height = arr[0][1]
idx = 0
for i in range(len(arr)):
    if arr[i][1] > height:
        height = arr[i][1]
        idx = i
    
# 최대 인덱스를 구해주고
# 갱신만해주고 계산이 제대로 안되고 있구나

# 그럼 이 답은 애초에 틀린답이야
# 어렵에
# 깔끔하네
# 이것도 배열풀이
import sys
input = sys.stdin.readline

m = 0
m_idx = 0
pli = [0 for _ in range(1001)] # 기둥
for _ in range(int(input())):
    L,H = map(int,input().split())
    pli[L] = H
    if m < H: # 가장 높은 기둥과 그 기둥의 인덱스를 찾음
        m_idx = L
        m = H
curr = 0
answer = 0
for i in range(m_idx+1): # 왼쪽 그룹
    curr = max(curr,pli[i])
    answer += curr
curr = 0
for i in range(1000,m_idx,-1): # 오른쪽 그룹
    curr = max(curr,pli[i])
    answer += curr
print(answer)