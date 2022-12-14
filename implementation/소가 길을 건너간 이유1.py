N = int(input())

# 소의 번호는 1~10이하
# 길의 왼쪽 0 오른쪽 1

dp = [0] * 11
dp1 = [1] * 11

cnt = 0
for _ in range(N):
	n, p = map(int, input().split())

	prev = dp[n]
	# 0 1
	# 수가 다르다면
	# 처음 변경하는 지 체크
	# 0 0
	if prev != p:
		# dp1[n] == 1이라면
		# 처음 바뀌는 값
		if dp1[n] == 1:
			dp1[n] += 1
			dp[n] = p
		else:
			dp[n] = p
			cnt+=1
	else:
		# 만약 값이 같다면
		if dp1[n] == 1:
			dp1[n] += 1
			dp[n] = p
		else:
			dp[n] = p
print(cnt)

