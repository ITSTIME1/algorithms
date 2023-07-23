N, P = map(int, input().split())

ans = N
arr = []
arr.append(N)
last = 0
while True:
	ans = (ans * N) % P
	# 수가 포함되어 있지 않다면
	# [67, 25, 1, 5, 25]
	if ans not in arr:
		arr.append(ans)
	else:
		last = ans
		break
if last in arr:
	print(len(arr[arr.index(last):]))