N = int(input())

array = []
for i in range(N):
	input_data = input().split()
	array.append((input_data[0], int(input_data[1])))


array = sorted(array, key = lambda x : x[1])
for x in array:
	print(x[0], end = " ")
