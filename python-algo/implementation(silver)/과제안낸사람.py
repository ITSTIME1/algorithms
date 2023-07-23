dp = [0] * 31

for i in range(28):
	n = int(input())
	dp[n] = 1

for i in range(1, len(dp)):
	if dp[i] == 0:
		print(i)