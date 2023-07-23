N = int(input())
arr = []

# 5 2 3 4 1
for m in range(N):
	arr.append(int(input()))

for i in range(len(arr)):
	min_index = i
	
	# 1, 2, 3, 4
	# 5 | 2 3 4 1
	# 1 | 2 3 4 5
	for j in range(i+1, len(arr)):
		if arr[min_index] > arr[j]:
			min_index = j
	arr[i], arr[min_index] = arr[min_index], arr[i] 

print(*arr, sep="\n")
