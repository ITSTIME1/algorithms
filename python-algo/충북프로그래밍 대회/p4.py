import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



n = int(input())


matrix = [[0 for i in range(n)] for _ in range(n)]


# 처음을 제외하고
# 짝수는 왼쪽 -> 오른쪽
# 홀수는 오른쪽 -> 왼쪽
# 분수 찾기 문제랑 비슷한데..

for i in range(n):
	for j in range(n):
		if i % 2 == 0:

		else:
			a = i // 2 
			