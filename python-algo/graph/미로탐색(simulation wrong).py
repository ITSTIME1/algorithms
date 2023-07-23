# 문제분석

# 생각해보니까 행렬을 보고 시뮬레이션 류로 탐색하면 되겠다 했는데...
# 이러면 최단경로가 나오지 않는다
# N,M 까지 도달할려면 지나갈 수 있는 길 중에 가장 빠른길을 찾아야 하는데
# 시뮬레이션은 동서남북 다 돌고
# 만약 최적의 길의 방향이 아니더라도 그 쪽으로 진행한다
# 그러다 만약 막다른 길이라거나 해당 범위를 넘어간다거나
# 할때 다시 돌아오기 위해 방향을 튼다 그럼 맞는 방향을 통해서
# 움직이게 되고 그렇게 된다면 원래 왔던 길을 중복해서 cnt 하게 되고
# 그럼 최적의 경로가 아닌 더 멀어지는 길이된다
# 행렬의 칸이 100 * 100 으로 주어지는게 가장 최악의 경우라고 한다면
# 100 * 100 칸을 다 검색해야되는데 중첩된 칸이 많아진다
# 중첩된 칸이 많아질수록 불필요한 연산들이많아진다.


import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 먼저 1은 이동가능하고 0은 이동 가능하지 않다
# 이랬을때 처음과, 마지막도 cnt 에 포함한다고 했으니
# 처음시작할때 카운트 마지막 원하는 위치에 도착했을때도 카운트한다.

# 시뮬레이션으로 풀 수 있을거 같은데


# 근데 그러면 원래 왔던 곳은 차감해야되는데
# 원래 왔던 곳을 알고 있어야 하지 않을까


# 뭐지 시뮬레이션으로 하니까 값이 안나오는데.

n, m = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
	a = input().strip()
	board[i] = a



# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
cnt = 1
index = 0 

while True:
	if x == n-1 and y == m-1:
		print(cnt+1)
		break

	# 이동할 좌표를 업데이트하고
	nx = x + dx[index]
	ny = y + dy[index]

	# 그 이동할 좌표를 검사하고
	# 해당 조건들에 맞지 않는다면
	# 방향을 틀어주던지	 아니면
	# 좌표를 업데이트 하지 않는다
	if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "0":
		index += 1
		if index >= len(dx):
			index = 0
		continue
	x, y = nx, ny
	cnt += 1

	












