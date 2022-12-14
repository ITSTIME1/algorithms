T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = sum(arr)
    cnt = 1
    # 21 : 21, 22
    while N >= result:
        cnt+=1
        result*=4   
    print(cnt)
