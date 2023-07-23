N, M = map(int, input().split())
# 그래프와 비교할 dp
arr = [list(input()) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(len(arr)):
	goorm = 0
	count = 0
	for j in range(M):
		if arr[i][j] == "c":
			dp[i][j] = 0
			goorm += 1
			count = 0
		elif arr[i][j] == ".":
			# 전에 구름이 있었는지 없었는지 판단을 하고
			# 구름이 없었다면 앞으로도 쭉 없을테니까
			# -1을 출력해주고
			if goorm == 0:
				dp[i][j] = -1
			else:
				count+=1
				dp[i][j] = count

for i in dp:
	print(*i, end = "\n")