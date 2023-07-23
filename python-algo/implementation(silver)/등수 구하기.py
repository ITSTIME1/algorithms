# 문제분석


# 0<=n<=p
# 10<=p<=50
n, new_num, p = map(int, input().split())
ans = 0
if n == 0:
	ans = 1
else:
	ranking = list(map(int, input().split()))
	ranking.sort(reverse=True)
	# 마지막 점수가 가장 작은 점수니까
	# 조건에 따라 새로운 점수는 이전 점수보다 더 커야 그와 교환할 수 있따
	# 즉 가장 작은 점수보다 같거나 혹은 더 작다면 들어오지 못한다는 얘기다

	if n == p:
		if ranking[-1] >= new_num:
			ans = -1
		else:
			for i in range(len(ranking)):
				if ranking[i] <= new_num:
					ans = i + 1
					break
	else:
		ans = n+1
		for i in range(len(ranking)):
			if ranking[i] <= new_num:
				ans = i + 1
				break
		
print(ans)


