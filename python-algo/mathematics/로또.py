import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


while True:
	n = list(map(int, input().split()))
	k = n[0]
	arr = n[1:]

	if k == 0:
		break

	for i in combinations(arr, 6):
		print(*i)
	print(" ")