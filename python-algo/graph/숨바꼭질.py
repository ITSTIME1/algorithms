import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

dot = [0] * 100001
# 0~100000
def bfs(root, cnt):

	queue = deque([(root, cnt)])
	while queue:
		r, c = queue.popleft()
		if r == K :
			return c
		if 0 <= r - 1 < 100001 and dot[r-1] == 0:
			dot[r-1] = 1
			queue.append((r-1, c + 1))
		if 0 <= r * 2  < 100001 and dot[r*2] == 0:
			dot[r*2] = 1
			queue.append((r*2, c + 1))
		if 0 <= r + 1  < 100001 and dot[r+1] == 0:
			dot[r+1] = 1
			queue.append((r+1, c + 1))


# 0 99999
if N == K:
	print(0)
else:
	answer = bfs(N, 0)
	print(answer)