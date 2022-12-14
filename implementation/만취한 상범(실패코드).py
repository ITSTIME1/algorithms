T = int(input())

for _ in range(T):
	room = int(input())

	arr = [0] * room
	count = 0
	#       1 2 3 4 5
	# r = 5 0 1 2 3 4
	for i in range(1, room+1):
		if i == 1:
			pass
		else:
			check = i
			if arr[check-1] == 0:
				arr[check-1] = 1
			elif arr[check-1] == 1:
				arr[check-1] = 0
			# i = 2 check *= i 4
			# i = 2 check *= 4 * i = 8
			while i*check < room:

				if i*check > room:
					break
				else:
					if arr[(i*check)-1] == 0:
						arr[(i*check)-1] = 1
					elif arr[(i*check)-1] == 1:
						arr[(i*check)-1] = 0

				check += i
				
	print(arr.count(0))
	