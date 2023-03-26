import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# 반시계
def matrix(n, m, r):
	for _ in range(r):
		# 사각형을 선택하기 위한 for문인거지
		for j in range((min(n,m)//2)-1, -1, -1):
			x=y=j
			tmp = arr[x][y]
			for k in range(j+1, n-j):
				pre = arr[k][y]
				arr[k][y], tmp = tmp, pre
				x = k

			for k in range(j+1, m-j):
				pre = arr[x][k]
				arr[x][k], tmp = tmp, pre
				y = k

			for k in range(j+1, n-j):
				pre = arr[n-k-1][y]
				arr[n-k-1][y], tmp = tmp, pre
				x = n-k-1

			for k in range(j+1, m-j):
				pre = arr[x][m-k-1]
				arr[x][m-k-1], tmp = tmp, pre
				y = m-k-1

	for row in arr:
		for item in row:
			print(item, end = " ")
		print()

	# 와 지리네;;
matrix(n, m, r)
# print("\n".join([" ".join([str(item) for item in row]) for row in arr]))
# for i in a:
# 	print(*i)

# [[3, 4, 8, 12], 
# [2, 11, 10, 16], 
# [1, 7, 6, 15], 
# [5, 9, 13, 14]]

# 위에건 반시계방향으로 그럼 시계방향으로 돌려볼까

# 시계방향
# def matrix_o(n, m, r, arr):
# 	# 두번 돌리는건 여전한데
# 	for _ in range(r):
# 		# 사각형을 선택하는것도 가장 작은 변의 mod를 한 변을선택해서
# 		for j in range(min(n,m)//2):
# 			# 상 -> 우 -> 하 -> 좌 순서대로 가보면 될거 같은
# 			x=y=j
# 			tmp = arr[x][y]
# 			for k in range(j+1, (m-1-j)+1):
# 				pre = arr[x][k]
# 				arr[x][k], tmp = tmp, pre
# 				y = k
# 			# 0, 3
# 			for k in range(j+1, (n-1-j)+1):
# 				pre = arr[k][y]
# 				arr[k][y], tmp = tmp, pre
# 				x = k

# 			# 3, 3
# 			# 1, 2, 3
# 			for k in range(j+1, (m-1-j)+1):
# 				pre = arr[x][n-k-1]
# 				arr[x][n-k-1], tmp = tmp, pre
# 				y = n-k-1

# 			# 3, 0
# 			for k in range(j+1, (n-1-j)+1):
# 				pre = arr[n-k-1][y]
# 				arr[n-k-1][y], tmp = tmp, pre
# 				x = n-k-1


# 	return arr

# a = matrix_o(n, m, r, arr)
# print(a)



# [[9, 5, 1, 2], 
# [13, 11, 10, 3], 
# [14, 7, 6, 4], [
# 15, 16, 12, 8]]









