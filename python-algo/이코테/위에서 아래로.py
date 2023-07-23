N = int(input())

array = []
for i in range(N):
	array.append(int(input()))


# 선택정렬


for j in range(len(array)):
	min_index = j
	for k in range(1, len(array)):
		if array[min_index] < array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]

array.sort(reverse=True)
print(*array, end = " ")