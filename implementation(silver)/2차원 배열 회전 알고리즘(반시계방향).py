arr = [[1,2,3], [4,5,6], [7,8,9]]

def left_90(arr):
	N = len(arr)
	ret = [[0 for _ in range(N)] for _ in range(N)]
	for r in range(N):
		for c in range(N):
			ret[N-1-c][r] = arr[r][c]
	return ret
print(left_90(arr))

# [[3, 6, 9], 
# [2, 5, 8], 
# [1, 4, 7]]

def left_180(arr):
	N = len(arr)
	ret = [[0 for _ in range(N)] for _ in range(N)]
	for r in range(N):
		for c in range(N):
			ret[N-1-r][N-1-c] = arr[r][c]

	return ret

print(left_180(arr))
# [[9, 8, 7], 
# [6, 5, 4],
#  [3, 2, 1]]

def left_270(arr):
	N = len(arr)
	ret = [[0 for _ in range(N)] for _ in range(N)]
	for r in range(N):
		for c in range(N):
			ret[c][N-1-r] = arr[r][c]

	return ret

print(left_270(arr))

# [[7, 4, 1], 
# [8, 5, 2], 
# [9, 6, 3]]