
# 첫번째 방법
M, N = map(int, input().split())
arr=[]

for i in range(M,N+1):
    if i==1:
        pass
    elif i==2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                print(i)
                arr.append(i)

for i in arr:
    print(i)

# 두번째 방법
M, N = map(int, input().split())

for i in range(M, N+1):
    check = True
    if i == 1:
        check = False
    else:
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            print(i)

# 세번째 방법 ( 에라토스 테네스의 체 )