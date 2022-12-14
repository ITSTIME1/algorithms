import sys
input = sys.stdin.readline()
# # 에라토스테네스의 체 를 이용한 풀이
# def prime_number(num):
#     # 0부터 num 범위의 자연수의 소수 판별 여부를 위한 리스트. 
#     # 0과 1은 소수가 아니므로 False로 선언
#     check_prime = [False, False] + [True] * (num - 1)
#     # 앞서 설명한 약수의 원리를 응용해 소수 판별 범위 축소
#     for i in range(2, int(num**0.5)+1):
#         if check_prime[i]:
#             # i가 소수라면 i 이후 나올 i의 배수들은 전부 소수가 아니므로 False 선언
#             for j in range(i+i, num+1, i):
#                 check_prime[j] = False

#     if check_prime[num]:
#         return True


# M, N = map(int, input.split())

# for i in range(M, N+1):
#     # 만약 해당 수가 소수라면
#     if prime_number(i):
#         print(i)

M, N = map(int, input.split())


# n 까지 소수인지 아닌지 판별하기 위해서 dp 테이블을 만들어둔 다음에
dp = [False] * (N+1)
for i in range(2, N+1):
    if dp[i] == False:
        if i < M:
            pass
        else:
            print(i)
        for j in range(2*i, N+1, i):
            if dp[j] == False:
                dp[j] = True