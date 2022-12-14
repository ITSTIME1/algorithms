arr = list(map(str, input().split()))
N = len(arr)
while "".join(arr) != "12345":
	for i in range(N-1):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
			print(*arr)
