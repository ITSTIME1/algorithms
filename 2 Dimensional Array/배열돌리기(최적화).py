import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 가져오는게문제인데
# arr이 주어지고..
# 그 주어진 값에서 deque를 이용해서 돌릴건데
# 겉의 있는 값만 어떻게 가져올까

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# size 가 틀렸네
# 겉배열만 신경쓰고 겉배열이 돌아가면 같은줄 알았는데 그게 아니었구나
# 다시한번 볼 필요가 있다 이건

size = 2 * n + 2 * m - 4
depth = min(n, m) // 2

def matrix(n, m, r, depth):
	dx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

	for i in range(depth):
		index = 0
		x=y=i
		l = deque([arr[x][y]])
		while True:

			# 0, 1
			nx = x+dx[index][0]
			ny = y+dx[index][1]
			
			if nx == i and ny == i:
				break

			if nx < i or nx > n-i-1 or ny < i or ny > m-i-1:
				index += 1
				if index >= len(dx):
					index = 0
				continue

			x, y = nx, ny
			l.append(arr[x][y])
		# 아니면 이걸 그 범위 구하는것처럼 해야되나
		# i = 0
		# i = len(m)-1
		# i = len(n)-1
		# i = len(m)-1
		x=y=i
		index = 0

		# 이 rotate() 함수를 사용하면 더 잘 돌릴 수 있네
		# 안에 인수를 넘겨주면 -붙이면 반시계
		# rotate() 함수를 잘 사용하면 좋겠네
		l.rotate(-(r % (size-8*i)))	
		# for _ in range():
		# 	a = l.popleft()
		# 	l.append(a)
		arr[x][y] = l[0]
		l.popleft()

		while len(l) != 0:
			nx = x + dx[index][0]
			ny = y + dx[index][1]
			if nx < i or nx > n-i-1 or ny < i or ny > m-i-1:
				index += 1
				if index >= len(dx):
					index = 0
				continue
			x, y = nx, ny
			arr[x][y] = l[0]
			l.popleft()


matrix(n, m, r, depth)
print("\n".join([" ".join([str(item) for item in row]) for row in arr]))
# for row in arr:
# 	for items in row:
# 		print(items, end = " ")
# 	print()

# [[3, 4, 8, 12], 
# [2, 11, 10, 16], 
# [1, 7, 6, 15], 
# [5, 9, 13, 14]]

# [[28, 27, 26, 25], 
# [22, 9, 15, 19], 
# [16, 8, 21, 13], 
# [10, 14, 20, 7], 
# [4, 3, 2, 1]]

# 예제도 맞게 잘나오고


# import sys
# input = sys.stdin.readline

# def rotate(start):

#     #init_tmp
#     top = matrix[start][start]
#     left = matrix[N-start-1][start]
#     bottom = matrix[N-start-1][M-start-1]
#     right = matrix[start][M-start-1]

#     # top
#     for i in range(start+1,M-start):
#         matrix[start][i-1] = matrix[start][i]
#     # left
#     for i in range(N-start-1,start,-1):
#         matrix[i][start] = matrix[i-1][start]
#     # bottom
#     for i in range(M-start-1,start+1,-1):
#         matrix[N-start-1][i] = matrix[N-start-1][i-1]
#     # right
#     for i in range(start+1,N-start):
#         matrix[i-1][M-start-1] = matrix[i][M-start-1]
#     # finish
#     matrix[start+1][start] = top
#     matrix[N-start-1][start+1] = left
#     matrix[N-start-2][M-start-1] = bottom
#     matrix[start][M-start-2] = right

# N, M, R = map(int,input().split())
# size = 2 * N + 2 * M - 4
# matrix = [list(map(int, input().split())) for _ in range(N)]
# short = N if N <= M else M

# for n_th in range(short//2):
#     for _ in range(R%(size-8*n_th)):
#         rotate(n_th)

# for row in matrix:
#     print(*row)


