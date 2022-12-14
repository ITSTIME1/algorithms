# A 행렬의 크기 N, M을 받고
# B 행렬의 크기 M, K을 받고
# A 행렬 * B행렬이 성립되려면
# A 행렬의 M(열) 과 B행렬의 M(행이) 같아야 행렬의 곱이
# 성립이됨
import sys
# A행렬
N, M = map(int, sys.stdin.readline().strip().split())
a_matrix = [sys.stdin.readline().strip().split() for _ in range(N)]

# B행렬
M, K = map(int, sys.stdin.readline().strip().split())
b_matrix = [sys.stdin.readline().strip().split() for _ in range(M)]

# # AB 행렬곱의 조건
C = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += int(a_matrix[n][m]) * int(b_matrix[m][k])


for i in C:
	print(*i, end="\n")