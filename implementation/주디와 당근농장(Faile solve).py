N, R, C = map(int, input().split())
dp = [[0 for _ in range(N)] for _ in range(N+1)]

for i in range(1, len(dp)):
	for j in range(N):
		if i % 2 == 0:
			if dp[i].index(dp[i][j]) % 2 == 0:
				dp[i][j] = "v"
			else:
				dp[i][j] = "." 
		
		else:
			if dp[i].index(dp[i][j]) % 2 == 1:
				dp[i][j] = "v"
			else:
				dp[i][j] = "." 


for i in range(1, len(dp)):
	print("".join(dp[i]))
# . v . v
# v . v .
# . v . v
# v . v .

# .v.v
# v.v.
# .v.v
# v.v.