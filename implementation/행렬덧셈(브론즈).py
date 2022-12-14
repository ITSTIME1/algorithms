N, M = map(int, input().split())

dp = [[0 for _ in range(M)] for _ in range(N)]

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
	a_ch = A[i]
	b_ch = B[i]
	for j in range(M):
		dp[i][j] = a_ch[j] + b_ch[j]

for i in dp:
	print(*i, end = "\n")