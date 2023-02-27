import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


s = "a234"

s_l = list(s)
ans = [True] * len(s)


for i in range(len(s_l)):
	if s_l[i].isdigit() != True:
		ans[i] = False
	else:
		ans[i] = True

if False in ans:
	answer = False
else:
	answer = True