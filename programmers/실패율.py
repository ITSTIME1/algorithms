import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = 4
stages = [4,4,4,4,4]

# stage에 머물고 있는 사람부터 구해보자면
# stage에 머물고 있는 사람이 없는 경우는 그냥 0 이니까
# 이때의 실패율은 그냥 0
# 음....


dic = {str(i): 0 for i in range(1, n+1)}

st = {str(i): 0 for i in range(1, n+1)}

# 스테이지의 머물고 있는 사람들
for i in stages:
	if str(i) not in dic:
		dic[str(i)] = 1
	else:
		dic[str(i)] += 1

# 스테이지를 거쳐간 사람들
for i in range(1, n+1):
	c = i
	for j in stages:
		if j >= c:
			st[str(c)] += 1



ans = {}
for k, v in dic.items():
	if v == 0:
		if int(k) <= n:
			ans[str(k)] = 0
	else:
		if str(k) in st:
			ans[str(k)] = v / st[str(k)]


# 내림차순정렬
ans_list = sorted(ans.items(), key=lambda x: -x[1])


answer = []
for i in ans_list:
	answer.append(int(i[0]))

print(answer)
