import sys
input = sys.stdin.readline()
# 약수의 성질을 이용한 풀이
# 문제에서 1도 포함하기 때문에 1이 들어오면 False를 리턴해줄 것이다.
def check_prime(num):
    if num == 1: 
        return False # 1은 소수가 아니므로 제외
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


M, N = map(int, input.split())

for i in range(M, N+1):
    # 만약 해당 수가 약수라면
    if check_prime(i):
        print(i)
