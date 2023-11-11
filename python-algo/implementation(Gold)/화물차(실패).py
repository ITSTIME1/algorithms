
import sys
from collections import deque
input = sys.stdin.readline


def inter_check():
	global inter_infor_dic
	# 모든 교차로는 한번에 바뀌어야하니까
	for i in inter_list:
		# 해당 교차로의 4번값을 즉 열려있는값을 기준으로 감소
			# 동서가 열려있는 상태라면
		if inter_infor_dic[i][4] == 0:
			inter_infor_dic[i][1] -=1 
			if inter_infor_dic[i][1] == 0:
				inter_infor_dic[i][4] == 1
			continue
		else:
			# 남북이 열려있는상태라면
			inter_infor_dic[i][2] -=1 
			if inter_infor_dic[i][2] == 0:
				inter_infor_dic[i][4] == 0
			continue


		# 만약 둘다 0이면
		# 초기값 셋팅
		if inter_infor_dic[i][1] == 0 and inter_infor_dic[i][2] == 0:
			inter_infor_dic[i][1] = inter_infor_dic[i][3][0]
			inter_infor_dic[i][2] = inter_infor_dic[i][3][1]
			inter_infor_dic[i][4] = inter_infor_dic[i][3][2]


def bfs():
	global inter_infor_dic
	queue = deque([(startX, startY)])
	# 동서남북
	dx = [(0, 1), (0,-1), (1, 0), (-1,0)]

	# 방문지점 체크
	visited = [[0] * n for _ in range(m)]
		
	while queue:
		x, y = queue.popleft()
		for index in range(4):
			nx = dx[index][0] + x
			ny = dx[index][1] + y

			if 0<= nx < m and 0<= ny < n:
				# 방문하지 않았으면서, 도로라면
				if visited[nx][ny] == 0 and board[nx][ny] == "#":
					queue.append((nx, ny))
					visited[nx][ny] = visited[x][y] + 1
					inter_check()
				# 방문하지 않았으면서, 교차로라면
				elif visited[nx][ny] == 0 and "0"<=board[nx][ny] <="9":
					# 우선 지나가면서도 계속 방향을 바꿔야하니까
					
					if (index == 0 or index == 1) and inter_infor_dic[board[nx][ny]][4] == 0:
						inter_check()
						queue.append((nx, ny))
						visited[nx][ny] = visited[x][y] + 1
					elif (index == 2 or index == 3) and inter_infor_dic[board[nx][ny]][4] == 1:
						inter_check()
						queue.append((nx, ny))
						visited[nx][ny] = visited[x][y] + 1
					else:
						queue.append((x, y))
						visited[x][y] += 1	
						continue

				
				elif visited[nx][ny] == 0 and nx == endX and ny == endY:
					visited[nx][ny] = visited[x][y] + 1
					print(visited)
					return visited[nx][ny]

	return "impossible"


while True:
	m, n = map(int, input().split())
	if n==0 and m==0: break
	board = []
	# m행만큼 데이터를 받아주고
	inter = 0
	startX, startY = -1, -1
	endX, endY = -1, -1
	# 교차로 정보를 담아주자.
	inter_list = []
	for j in range(m):
		tmp = list(input().rstrip())
		for k in range(n):	
			if "0" <= tmp[k] <= "9":
				inter += 1
				inter_list.append(tmp[k])

			elif tmp[k] == "A":
				startX = j
				startY = k

			elif tmp[k] == "B":
				endX = j
				endY = k
		board.append(tmp)

	# 교차로정보
	inter_infor_dic = {}
	for j in range(inter):
		inter_infor = list(input().split())

		if inter_infor[1] == "-":
			inter_infor_dic[inter_infor[0]] = [inter_infor[1], int(inter_infor[2]), int(inter_infor[3]), [int(inter_infor[2]), int(inter_infor[3]), 0], 0]
		else:
			inter_infor_dic[inter_infor[0]] = [inter_infor[1], int(inter_infor[2]), int(inter_infor[3]), [int(inter_infor[2]), int(inter_infor[3]), 1], 1]

		
	space = input()
	# 교차로 리스트가 비어있다는건 교차로가 없다는것.
	# 이제 이 정보들을 가지고 bfs를 돌릴건데
	answer = bfs()
	print(answer)

