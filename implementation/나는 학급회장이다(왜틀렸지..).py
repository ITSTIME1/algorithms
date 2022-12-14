N = int(input())

dp = [[0 for _ in range(3)] for _ in range(3)]

for _ in range(N):
	a, b, c = map(int, input().split())
	for k in range(1):
		dp[k][a-1] += a
		dp[k+1][b-1] += b
		dp[k+2][c-1] += c

arr = [sum(c) for c in dp]

max_num = max(arr)
president = 0
for _ in range(len(arr)):
	if arr.count(max_num) > 1:
		index = []
		for j in range(len(arr)):
			if max_num == arr[j]:
				index.append(j)

		th = []
		for k in index:
			th.append(dp[k][2])

		gr = max(th)
		cnt = 0
		for b in th:
			if gr == b:
				cnt+=1
		if cnt > 1:
			se = []
			for c in index:
				se.append(dp[c][1])
			second = max(se)

			scnt = 0
			for k in se:
				if second == k:
					scnt += 1
			if scnt == 1:
				president = se.index(max(se))+1
				break
			else:
				president = 0
				break
		elif cnt == 1:
			president = th.index(max(th)) + 1
			break

print(president, max(arr))

