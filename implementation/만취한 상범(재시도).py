T = int(input())

for _ in range(T):
	room = int(input())

	arr = [0] * room
	
	for i in range(1, room+1):
		check = i
		while check <= room:
			if arr[check-1] == 0:
				arr[check-1] = 1
			else:
				arr[check-1] = 0

			check+=i
	print(sum(arr))