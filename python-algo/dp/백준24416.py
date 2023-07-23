# 피보 나치 재귀함수
def fibo(n):
	if(n == 1 or n == 2):
		return 1

	else:
		return fibo(n-1) + fibo(n-2)


# 피보 나치 동적 계획법

def dp(n):
	dp = [0] * (n+1)
	dp[1] = 1
	dp[2] = 1
	count = 0
	for i in range(3, n+1):
		count+=1
		dp[i] = dp[i-1] + dp[i-2]
	return count


n = int(input())
print(fibo(n), dp(n))
