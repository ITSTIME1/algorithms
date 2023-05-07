import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(input().strip()) for _ in range((5*m)+1)]


grid = ["................", "****............", "********........", "************....", "****************"]

one, two, three, four, five = 0, 0, 0, 0, 0



def go(i, j):
	#5, 5
	global one, two, three, four, five
	answer = ""
	for idx in range(i, i+4):
		for jdx in range(j, j+4):
			answer += board[idx][jdx]
			board[idx][jdx] = "x"

	for i in range(len(grid)):
		if answer == grid[i]:
			if i == 0:
				one += 1
			elif i == 1:
				two += 1
			elif i == 2:
				three += 1
			elif i == 3:
				four += 1
			else:
				five += 1






for i in range((5*m)+1):
	for j in range((5*n)+1):
		if board[i][j] == "." or board[i][j] == "*":
			# 1, 1
			go(i, j)
		else:
			continue


print(one, two, three, four, five)
