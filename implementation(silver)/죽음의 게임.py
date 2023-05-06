import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, bo = map(int, input().split())

cnt = 1
dic = {}
h = 0
for i in range(n):
	dic[str(i)] = int(input())

# dic은 몇번 사람이 몇번을 지목하는 테이블이 되는거고

# 새로운 딕을 만들때는
# 0번 사람이 만약에 cnt번을 외치고
# 그 외친 사람인 0번이 지목한 사람을 다음 사람으로 지목해

# '0' : 1
new_dic = {}
ans = 0
for _ in range(n):

	new_dic[str(h)] = [dic[str(h)], cnt]
	if new_dic[str(h)][0] == bo:
		ans = new_dic[str(h)][1]
		break
	h = str(dic[str(h)])
	# {'0': [1, 1], '1': [3, 2]}
	cnt += 1
if ans == 0:
	print(-1)
else:
	print(ans)