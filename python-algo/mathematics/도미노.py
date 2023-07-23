import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

# 중복이 되지 않는다는 것은 세트의 나온 수가 똑같이 구성이 되어진것 들은 경우로 보지 않는다 는 것.
# 결국 0, 0 2,2 같은 중복은 허락하지만 순서는 고려하지 않는 중복순열문제가 되는데


# 하지만 최대 n이 1000으로 잡혀있기 때문에
# 중복순열로 풀게 된다면 시간초과가 날 수 있다.

cnt = 0

# for i in range(0, n+1):
# 	for j in range(i, n+1):
# 		print(i ,j)

for i in combinations_with_replacement(range(n+1), 2):
	cnt += sum(list(i))
print(cnt)