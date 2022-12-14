T = 10
arr = [i for i in range(1, 21)] 

for _ in range(T):
	x, y = map(int, input().split())
	c = arr[x-1:y]
	del arr[x-1:y]
	# del 해서 구간을 없애고
	# 새로 reverse 한 구간을 다시 삽입해준다.
	c.reverse()
	# 4, 5, 6, 7, 8, 9
	
	z = 0
	for i in range(x-1, y):
		arr.insert(i, c[z])
		z += 1
	
print(*arr, end = " ")

