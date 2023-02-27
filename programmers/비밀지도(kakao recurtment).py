import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


decimal = 9


# 20 미만의 숫자들은 0을하나씩붙이나
# 그럼 18도 0을 붙여야하는데 그것도 아니고

# n의 크기에 못미친다면
# 앞에 0을 붙여주어야하네
# 개수가 부족한만큼
# 1 같은경우
# 4개가 부족하니 4개의 0을 붙여야 하는거고

# 9같은 경우 1개가 부족하니 1개를 붙여야하는거고

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

# str 으로 오니까
# print(type(format(decimal, 'b')))
for i in range(len(arr1)):
	c = format(arr1[i], 'b')
	if len(c) < n:
		r = n - len(c)
		c = '0'*r + c
		arr1[i] = c
	else:
		arr1[i] = c

for i in range(len(arr2)):
	c = format(arr2[i], 'b')
	if len(c) < n:
		r = n - len(c)
		c = '0'*r + c
		arr2[i] = c
	else:
		arr2[i] = c


# 이렇게 이진수로 각각 변환을 시켜준다음

# 0 0 일때는 공백
# 1 0 둘중 하나가 1일때는 무조건 #

board = [["#" for _ in range(n)] for _ in range(n)]

for i in range(len(arr1)):
	for j in range(len(arr2)):
		if arr1[i][j] == "0" and arr2[i][j] == "1":
			board[i][j] = "#"
		elif arr1[i][j] == "1" and arr2[i][j] == "0":
			board[i][j] = "#"
		elif arr1[i][j] == "0" and arr2[i][j] == "0":
			board[i][j] = " "

answer = []
for i in board:
	answer.append("".join(i))
print(answer)