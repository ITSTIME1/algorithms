from collections import deque
n = int(input())
q = deque(enumerate(map(int,input().split())))

ans=[]

print(q)

while q:
    idx,num = q.popleft()
    ans.append(idx+1)
    print(q)
    if num>0:
        q.rotate(-(num-1))
        print(q)
    elif num<0:
        q.rotate(-num)
print(' '.join(map(str,ans)))


# rotate(-1) = 반시계방향으로
# rotate(1) = 시계방향으로 회전 시킨다

