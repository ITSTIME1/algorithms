T = int(input())

for _ in range(T):

	# 3
	# 0
	# 1 
	# 2
	N, M = map(int, input().split())
	arr = [int(x) for x in input().split()]
	want_number = arr[M]
	# 4 1 2 3
	count = 0
	while True:
		max_number = 0
		first = arr[0]
		# 1, 2, 3, 4
		if max(arr) != first:
			c = arr.pop(0)
			arr.append(c)
			# 2 3 4 1
			# 3 4 1 2
			# 4 1 2 3
			# 2 3 1
			# 3 2 1
		else:
			max_number = first
			arr.pop(0)
			count+=1
			# 1 2 3
		# 같은 숫자가 존재한다면
		# 1 1 1 1 1
		# 
		if(arr.count(max_number) > 0):
			count+=len(arr)-1

		if(max_number == want_number):
			break
	
	print(count)







