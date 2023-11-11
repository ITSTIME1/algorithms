import sys
from collections import defaultdict
from itertools import permutations, combinations
import copy
input = sys.stdin.readline


# 물약의 종류
N = int(input())

# 물약의 가격
potion = list(map(int, input().split()))

# sales
sales_potion = defaultdict(list)


for i in range(N):
	pi = int(input())
	if pi == 0:
		sales_potion[i] = []
		continue
	for j in range(pi):
		ai, dj = map(int, input().split())
		sales_potion[i].append((ai,dj))



all_case = permutations(sales_potion)


minVal = 99999
for i in all_case:
	total = 0
	potion_list = copy.deepcopy(potion)
	for j in i:
		# 0,,1,2,,3
		if len(sales_potion[j]) == 0:
			total += potion_list[j]
			continue
		total += potion_list[j]
		for c in sales_potion[j]:
			# (3, 20)
			# 할인을시킨다.
			if potion_list[c[0]-1] - c[1] <= 0:
				potion_list[c[0]-1] = 1
			else:
				potion_list[c[0]-1] -= c[1]
	
	minVal = min(total, minVal)
print(minVal)