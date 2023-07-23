# O(2n)

# def fiboDP(N):
# 	dp = [0] * (N+1)
# 	dp[1] = 1
# 	dp[2] = 1

# 	for i in range(3, N+1):
# 		dp[i] = dp[i-1] + dp[i-2]
# 	return dp[i]

# # 피보나치 수열
# N = int(input())
# print(fiboDP(N))

# N = int(input())

# def fib(n):
#     _curr, _next = 0, 1
#     for _ in range(n):
#         _curr, _next = _next, _curr + _next

#     return _curr

# print(fib(N))


# 피보나치의 수열을 n 번씩 받을 경우
# n 번을 걸쳐서 출력을 해야 되는경우
# generator 를 구현해서 사용할 수 있다

# def fib(n):
#     _curr, _next = 0, 1
#     # 5
#     # 0 ~ 5
#     for _ in range(n + 1):
#         yield _curr
#         _curr, _next = _next, _curr + _next

# print(fib(int(input())))


N = int(input())
a, b = 0, 1
for i in range(N):
	a, b = b, a+b
print(a)