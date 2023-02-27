import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

s = "abcde"
s_l = list(s)
l = len(s_l)

answer = ""
if l % 2 == 1:
	answer = s_l[l//2]

else:
	answer = "".join(s_l[l//2-1:l//2+1])

print(answer)