import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

# 왼쪽이 부모노드, 자식노드
# 대략 다른 사람이 푼걸 보니까 dfs, bfs 를 이용해서 풀어야 되는 방법인거 같다
# 그럼 트리를 탐색하라고 한거 아닌가
tree = {"1": []}

ans_dic = {}
ans = []
for i in range(n-1):
	# 정점이 주어진다 vertex
	f, s = map(int, input().split())
	if str(f) in tree and str(s) not in tree:
		tree[str(f)].append(s)
		ans.append([s, f])

	elif str(f) not in tree and str(s) not in tree:
		tree[str(f)] = [s]
		ans.append([s, f])

	else:
		tree[str(f)] = [s]
		ans.append([f, s])

	# elif str(f) not in tree and str(s) in tree:
		# 4, 1
		# 2, 4
		
		
for i in ans:
	ans_dic[str(i[0])] = i[1]

for i in range(2, n+1):
	print(ans_dic[str(i)])