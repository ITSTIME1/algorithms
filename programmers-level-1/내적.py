import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 그전 값이 소문자고 이번에 들어온 값이 대문자라면
# 소문자가 더 큰것으로 간주하기 떄문에
# 소문자가 앞으로오면 될거 같은데

s = "Zbcdefg"

s_l = list(s)
s_l.sort(reverse=True)
print("".join(s_l))