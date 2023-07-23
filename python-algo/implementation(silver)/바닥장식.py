import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 세로가 n 가로가 m
n, m = map(int, input().split())


board = [input().strip() for i in range(n)]


board_check = [[False for _ in range(m)] for _ in range(n)]


total = 0

def mak(start, end):
	for i in range(end+1, m):
		if board[start][i] == "-":
			if board_check[start][i] != False:
				break
			else:
				board_check[start][i] = True

		else:
			break



def mak1(start, end):
	for i in range(start+1, n):
		if board[i][end] == "|":
			if board_check[i][end] != False:
				break
			else:
				board_check[i][end] = True
		else:
			break



for i in range(n):
	for j in range(m):
		# - 인것
		# |인것
		if board_check[i][j] == False and board[i][j] == "-":
			board_check[i][j] = True
			mak(i, j)
			total += 1
			continue

		elif board_check[i][j] == False and board[i][j] == "|":
			mak1(i, j)
			total += 1
print(total)

