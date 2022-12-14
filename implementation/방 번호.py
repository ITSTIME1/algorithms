N = list(map(int, input()))

num = [_ for _ in range(10)]
# 9 또는 6이 리스트에 있다면
cnt = 0
if 9 in N or 6 in N:
	for k in range(len(N)):
		# 9를 찾고
		if N[k] == 9 or N[k] == 6:
			if 9 in num:
				cnt+=1
				num.remove(9)
			else:
				if 6 in num:
					cnt+=1
					num.remove(6)
				else:
					break
		else:
			pass
	print(cnt)

# 없다면
# 한타스를 돌면서 보면 되네


# 111222333444555
# 1+1+1 = 3
# 12345
# cnt 1 + 1 + 1


# [0,1,2,3,4,5,6,7,8,9]
else:
	# 해당 값이 있으면 num 에서 지우고
	# 해당 값이 없으면 num 에서 지우지 않는다
	# 그렇게 한번씩 다 돌았다면 cnt += 1
	# 한번씩 돌때마다 arr 초기화
	# 그렇게 홰서 len(arr) == 0 이면 break print(cnt)
	cnt = 0
	c = N[:]
	while len(c) != 0:
		for i in range(len(N)):
			if N[i] in num:
				num.remove(N[i])
				c.remove(N[i])
			else:
				pass
		cnt+=1
		num = [_ for _ in range(10)] 
	print(cnt)
