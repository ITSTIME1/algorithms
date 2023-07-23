import sys
N = int(sys.stdin.readline().rstrip())
dp = [input().split() for _ in range(N)]
dp2 = [[0 for _ in range(N)] for _ in range(N)]
arr = []	
for k in range(len(dp)):
	for m in range(5):
		c = dp[k][m]
		for u in range(N):
			if c == dp[u][m]:
				dp2[k][m] += 1

	arr.append(sum(dp2[k]))
print(arr.index(max(arr)) + 1)
# O(N2)
# O(n3 + 2n)
# 1초 1억
# 2초 2억 

