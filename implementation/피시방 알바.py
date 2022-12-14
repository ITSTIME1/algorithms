dp = [0] * 101
N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
	# 아무도 없는 자리라면
	if dp[i] == 0:
		dp[i] += 1
	else:
		count+=1
print(count

# 0 ~ 101
# 0 ~ 100