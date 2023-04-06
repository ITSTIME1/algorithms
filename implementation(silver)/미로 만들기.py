import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())
zido = input()

# 100 * 100사이즈를 만들어주고
board = [["#" for _ in range(100)] for _ in range(100)]


# 초기 위치
firstX, firstY, firstD = 49, 49, 0
board[firstX][firstY] = "."

# 남 서 북 동
dx = [[1, 0], [0, -1], [-1, 0], [0, 1]]


index = 0

# 방향일 경우야
x = [firstX]
y = [firstY]
while True:
	# 문자열의 값을 하나씩 가지고오고
	# 지도의 값을 인덱스를 올리면서 하나씩 가지고오고
	s = zido[index]
	index += 1
	
	if index > n:
		break

	# 방향을 업데이트해주고
	if s == "R":
		firstD = (firstD + 1) % len(dx)
	elif s == "L":
		firstD = (firstD - 1) % len(dx)

	elif s == "F":
		# 좌표를 업데이트해주고
		firstX += dx[firstD][0] 
		firstY += dx[firstD][1]

		x.append(firstX)
		y.append(firstY)

		board[firstX][firstY] = "."


maxX = max(x)
minX = min(x)
maxY = max(y)
minY = min(y)


total = []
for i in range(minX, maxX+1):
	answer = []
	for j in range(minY, maxY+1):
		answer.append(board[i][j])
	total.append(answer)


for i in total:
	print(*i, sep = "", end="\n")






