# 점화식 떠올리자


dp = [0] * 30001

# x // 5
# x // 3
# x // 2
# x - 1


# x = 25

# 가장  큰 문제는 25고
# 이걸 x // 5 로 나눴을 때의 최소값
# x // 3 으로나눈 것 중 최솟값
# x // 2로 나눈 것 중 최솟값

# ai == 1 로 만드는 점화식
# min(ai-1, ai/2, ai/3, ai/5) + 1

N = int(input())

for i in range(2, N+1):
	dp[i] = dp[i-1] + 1

	if i // 5 == 0:
		dp[i] = min(dp[i], dp[i // 5] + 1)

	elif i // 3 == 0:
		dp[i] = min(dp[i], dp[i // 3] + 1)

	elif i // 2 == 0:
		dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])
