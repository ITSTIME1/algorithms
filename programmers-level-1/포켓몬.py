import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# combinations 쓰면 시간초과인데

nums = [3,3,3,2,2,2]


# 그럼이제 이 포켓몬들 조합중에서 최대로 포켓몬을 다르게 가질 수 있는 경우를 생각해야된다는건데
# 조합이 시간초과될때 쓸 수 있는게 뭐지
c = [i for i in combinations(nums, len(nums)//2)]

a = set()
p = 0 
for i in c:
	s = i
	for j in s:
		a.add(j)
	if len(a) > p:
		p = len(a)
print(p)
