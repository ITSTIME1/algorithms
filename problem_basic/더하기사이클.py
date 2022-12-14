N = int(input())
number = N

# 연산을 조건까지 계속 반복해야 되니까
count = 0
while True:
    # 26
    a = number // 10 # 2 # 6 # 8 # 4 # 2 # 2
    b = number % 10 # 6 # 8 # 4 # 2 # 2 # 4
    # 60 + 8 = 68
    # 80 + 4 = 84
    # 40 + 2 = 42
    # 20 + 6 = 26
    number = (b * 10) + ((a+b) % 10)
    count+=1
    if(number == N):
        break
    
print(count)

# 이거 풀ㄹ어봦

def solution(N):
    number = N
    count = 0
    while True:
        if(len(N) < 10):
            a = "0" + number
            count += 1 
            if(a[0] + a[1] == N):
                break
    print(count)


N = input()
solution(N)