dp = [_ for _ in range(1, 101)]
first = [1,1,1,2,2,3,4,5,7,9]
for _ in range(len(dp)):
	if _ <= 2:
		dp[0] = first[0]
		dp[1] = first[1]
		dp[2] = first[2]
	else:
		dp[_] = dp[_-2] + dp[_-3]

for i in range(int(input())): print(dp[int(input())-1])