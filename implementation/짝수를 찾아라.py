T = int(input())

for _ in range(T):
	arr = list(map(int, input().split()))

	tmp = []
	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			tmp.append(arr[i])

	print(sum(tmp), min(tmp))