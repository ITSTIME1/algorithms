T = int(input())

for i in range(T):
	arr = list(map(int, input().split()))
	arr.sort()
	del arr[arr.index(max(arr))]
	del arr[arr.index(min(arr))]
	if arr[2] - arr[0] >= 4:
		print("KIN")
	else:
		print(sum(arr))

