# 문제 분석

import sys
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

stack = deque([])
print(sys.getsizeof(stack))
for i in range(n):
	num = list(map(int, input().split()))
	num.sort(reverse = True)

	for j in num:
		stack.appendleft(j)

stack_list = list(stack)
stack_list.sort(reverse=True)
print(stack_list[n-1])