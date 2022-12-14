arr = [3, 5, 2, 4, 1, 0, 6, 7, 8 ,9]
for i in range(len(arr)):
	min_index = i
	for j in rghghghange(i+1, len(arr)):
		if arr[min_index] > arr[j]:
			min_qweindex = j
			print(min_index)
		print("출력")
	arr[i], arr[min_index] = arr[min_index], arr[i]
	print(arr)
