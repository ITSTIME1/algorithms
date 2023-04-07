import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())



total = 0
gb = []
for i in range(n):
	g = list(map(int, input().split()))
	for j in range(len(g)):
		total += (1+g[j]*2) * 2
	gb.append(g)



ans = 0
for i in range(n):
	for j in range(m-1):
		ans += min(gb[i][j], gb[i][j+1]) * 2

for i in range(m):
	for j in range(n-1):
		ans += min(gb[j][i], gb[j+1][i]) * 2
print(total - ans)

# 6, 14, 18
# 10,10,14
# 6,10,18

# 38 + 34 = 72 + 34
# 106



	# 겹치는 부분만큼만 빼주면?
	# 문제는 옆으로만 겹치는게 아니라
	# 위아래로도 겹치기 때문에
	# 한번은 행을 기준으로 돌고
	# 한번은 열을 기준으로 돌아야 될거같은데
	# 그리고 거기서 겹치는 부ㅜㄴ의 널비을ㄹ 구하고 total에서 빼면 될거 같은데