import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 그럼 n이 주어졌을때 1일될떄까지 나누자

# 와 이거 어렵다...
n = int(input())

mat = [list(map(int, input().split())) for i in range(n)]

def matrix(num):
	new_mat = [[0 for _ in range(num//2)] for _ in range(num//2)]
	nx, ny = 0, 0
	# 이렇게 검사할 수도 있네
	n = 0
	for i in range(0, num, 2):
		for j in range(0, num, 2):
			ar = [mat[i][j],  mat[i][j+1], mat[i+1][j], mat[i+1][j+1]]
			ar.sort(reverse=True)
			new_mat[nx][ny] = ar[1]
			ny += 1
		nx+=1
		ny=0
	return new_mat
		# 전부 돌았으면 여기서 나온 값이 바로 두번쨰값 newmat의 첫번째로줌



while n!=1:
	mat = matrix(n)
	n//=2

print(mat[0][0])
