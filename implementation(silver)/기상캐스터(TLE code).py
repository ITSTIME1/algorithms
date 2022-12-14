N, M = map(int, input().split())
# 그래프와 비교할 dp
arr = [list(input()) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(len(arr)):
	for j in range(M):
		if arr[i][j] == "c":
			dp[i][j] = 0
		else:
			dp[i][j] = -1

for i in range(N):
	cnt = 0
	index = []
	for j in range(M):
		if dp[i][j] == 0:
			cnt+=1
			index.append(j)
	# 0이 있는지 없는지 카운트를 세주고
	# 만약 0이 한개라면
	# 그리고 0 1개 이상이라면
	if cnt == 1:
		for k in range(M):
			if dp[i][k] == 0:
				count = 0
				for c in range(k+1, len(dp[i])):
					if dp[i][c] == -1:
						count += 1
						dp[i][c] = count
					elif dp[i][c] == 0:
						continue
	elif cnt > 1:
		# 0이 많다면
		count_m = 0
		min_index = min(index)
		max_index = max(index)
		for n in range(min_index, max_index):
			if dp[i][n] == -1:
				count_m += 1
				dp[i][n] = count_m
			elif dp[i][n] == 0:
				continue

		# 마지막 인덱스 loop
		count_m = 0
		for m in range(max_index+1, len(arr[i])):
			if dp[i][m] == -1:
				count_m+=1
				dp[i][m] = count_m




for i in dp:
	print(*i, end = "\n")