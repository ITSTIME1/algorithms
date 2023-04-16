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

# 사각형의 넓이를 구할거면 배열을 이용할 수 있음 해당 칸들만 1을 채워서 그 1들의 개수가 곧 사각형의 넓이가 되니까
# 만약 둘레의 길이를 구해야 한다고 한다면 이런식으로 상하좌우 방향의 값들을 기준으로 구할 수 있음.

# 한개의 사각형이어도 마찬가지


n = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]





# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = 0
for i in range(n):
	x, y = map(int, input().split())	

	for row in range(x-1, (x-1)+10):
		for col in range(y-1, (y-1)+10):
			arr[row][col] = 1

total = 0

for row in range(100):
	for col in range(100):
		if arr[row][col] == 1:
			tmp = 0
			for i in range(4):
				if arr[row+dx[i]][col+dy[i]] == 1:
					tmp += 1

			if tmp == 4:
				continue
			# 모서리길이
			elif tmp == 2:
				total += 2
			# 변의 길이
			elif tmp == 3:
				total += 1

print(total)

	# 아이디어가 이거네
	# 우선 둘레의 길이는 겹치는 부분이 존재
	# 가로와 세로의 각각 모서리에 하나씩 더 있다고 생각해야됨
	# 왜냐하면 가로 10 세로 10은 가로의 길이가 총 10개 있다고 생각해야하고
	# 세로의 길이도 총 10개 즉 마지막 모서리의 길이는 서로 겹친다는 것
	# 따라서 모서리의 길이는 두개씩 더해주어야한다는거
	# 그렇기 떄문에 모서리는 2씩 더해주고
	# 가로와 세로 한번에 계산해준다음에
	# 변의 길이를 구분하면 된다
	# 변의 길이라고 하면 아이디어중 상하좌우를 탐색하는 방법이 존재하는데
	# 만약 상하좌우 총 3개가 1이라면 그건 변의 길이다
	# 만약 4개모두 1이존재한다면 그건 겹쳐진 부분의 길이기 때문에 건너뛴다
	# 만약 두개만 있다면 그건 모서리의 길이기 때문에 2씩 더해주면 된다



	# 둘레니까
	# 겉만 바꾸는 방법이 필요해
	# 전부 1인상태니까
	# 이 상태에서 겉만 다른 값으로 바꾼다면
	# 그 값을 카운트하면
	# 둘레의 길이가 되니까




# 	ox, oy = x-1, y-1
# 	arr[ox][oy] = 1
# 	while True:
# 		nx = ox + dx[start][0]
# 		ny = oy + dx[start][1]

# 		# 원래 자리로 돌아오면
# 		if nx == x-1 and ny == y-1:
# 			break

# 		if nx < x-1 or nx >= (x-1)+10 or ny < y-1 or ny >= (y-1)+10:
# 			start += 1
# 			if start >= len(dx):
# 				start %= len(dx)


# 		ox, oy = nx, ny
# 		if arr[ox][oy] != 1:
# 			arr[ox][oy] = 1
# 		else:
# 			continue

# cnt = 0
# for i in arr:
# 	cnt += i.count(1)

# print(cnt)




