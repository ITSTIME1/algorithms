import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 시뮬레이션으로 돌리면 될거 같은데
# 먼저 3행 7열을 입력받는다면
# 3행부터 시작해서 3+10 까지 x윗부분을 채우고
# 거기 까지 도달했으면 밑으로 방향을 바꿔서 y만큼채워주고
# 또 전부 도달했으면 방향을 바꿔주고

# 아 이렇게 하면
# 두번재 사각형이 안쪽에 1이 생기니까
# 사실상 겹치는 값이 되네 ;;
# 이걸 예상했던건가

n = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]

# 동 남 서 북
dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = 0
for i in range(n):
	x, y = map(int, input().split())	

	ox, oy = x-1, y-1
	arr[ox][oy] = 1
	while True:
		nx = ox + dx[start][0]
		ny = oy + dx[start][1]

		# 원래 자리로 돌아오면
		if nx == x-1 and ny == y-1:
			break

		if nx < x-1 or nx >= (x-1)+10 or ny < y-1 or ny >= (y-1)+10:
			start += 1
			if start >= len(dx):
				start %= len(dx)


		ox, oy = nx, ny
		if arr[ox][oy] != 1:
			arr[ox][oy] = 1
		else:
			continue

cnt = 0
for i in arr:
	cnt += i.count(1)

print(cnt)




