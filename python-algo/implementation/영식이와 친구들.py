# 1 - 3 - 5 - 2 - 4 - 1 - 4 - 2 - 5 - 3 - 1
# 0 - 2 - 4 - 1 - 3 - 0 - 3 - 
# = 1번 이제 공을 세번 잡았기 때문에 게임 끝


N, M, L = map(int, input().split())
# [1,2,3,4,5]
# [0,1,2,3,4]
arr = [_ for _ in range(N)]
dp = [0] * N
# 1번부터 공을 잡고 시작하니까 count += 1
dp[0] += 1
# 처음 시작을 arr  = 1 로 잡고
# 첫번째의 카운트가 홀 수인지 짝수인지 확인하고
# 홀수라면 배열의 + L

# 첫 인덱스 설정
idx = 0
count = 0
while True:
	if dp[idx] == M:
		break
	if dp[idx] % 2 !=0 or dp[idx] == 0:
		idx = arr.index(idx)+L
		# 길이를 넘어갈 때
		count+=1
		if idx >= len(arr):
			# 6 - 5 = 1
			idx = idx - len(arr)
		else:
			pass
		dp[idx] += 1
	# 짝수라면
	elif dp[idx] % 2 == 0:
		# 5 - 1
		# 5 - 1 - 1
		idx = arr.index(arr[idx-L])
		count+=1
		dp[idx] += 1

	

print(count)

