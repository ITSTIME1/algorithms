import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 일수
n = int(input())

sang = []

for i in range(n):
	t, p = map(int, input().split())
	sang.append((t, p))


# 뭔가 이상한데

total = []
for i in range(len(sang)):
	s = sang[i]
	index = i

	cp = s[1]
	if index + sang[index][0] > n:
		continue

	# 0 + 5 = 5 
	# 5 + 1 = 6
	# 6 + 2 = 8
	result = index + sang[index][0]
	while result < n:
		if result + sang[result][0] > n:
			break
		cp += sang[result][1]
		result += sang[result][0]

	total.append(cp)
print(total)
print(max(total))
	