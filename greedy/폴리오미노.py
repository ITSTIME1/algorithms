import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



n = input().strip()

# "" = .


n = n.replace("XXXX", "AAAA")
n = n.replace("XX", "BB")

ans = ""
if "X" in n:
	ans = -1
else:
	ans = n
print(ans)

