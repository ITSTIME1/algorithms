import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



string = list(input().strip())

ans = []

for i in string:
	if i == "_" or i == ".":
		ans.append(i)
	else:
		if i.islower():
			ans.append(i.upper())
		else:
			ans.append(i)

print("".join(ans))