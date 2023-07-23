
# 소수 판별 알고리즘을 알고 있어야됨.
dp = [0] * (123457)

while True:
	N = int(input())
	if N == 0:
		break

	result = []
	for i in range(N+1, (2*N)+1):
		for j in range(1, i+1):
			if i % j == 0:
				dp[i] += 1


		if dp[i] == 2:
			result.append(i)
	print(len(result))




