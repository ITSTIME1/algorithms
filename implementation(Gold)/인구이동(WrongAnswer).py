
# 조건을 검사할대 max() - min()을 통해서 큰거에서 작은 값을 빼게 의도하여 마이너스가 나오지 않게 함
# 
# 결국 1. 현재좌표에서 인접한 곳과 인구차이계산
# 	2. 인구차이 조건에 맞다면 해당 인접좌표 boolean값을 True로 변경(이미 True로 변경되어 있다면 넘어감) 그렇지 않다면 False
# 	3. False로 되어있다면 인구수를 합산 만약 True로 되어 있다면(해당 구간은 이미 연합으로 인정되서 인구수가 더해졌기 때문에 더하지 않음)
# 	4. 현재 좌표에서 인접한 좌표들중 하나 이상 True값을 가지고 있다면 현재 좌표도 True로 변경해주고 인구수 합산
# 	5. 나머지 False인곳탐색

# 	6. 이후 모든 배열을 전부 탐색이 끝나고 나서 인구이동 식을 계산할건데 합산액 / True의 개수 = 값
# 	7. 해당 값으로 True로 되어 있는 조건의 인구수를 변경
# 	8. 이 과정을 True가 존재하지 않을때까지 그렇다는건 전부 False라는거고 전부 False가 된다면 인구이동이 불가능하기 때문에
# 	인구수를 변경까지 완료하면 단계가 1회 완성되었다고 판단하며 그 과정을 total 인구이동 카운트로 간주하고 올림



# 	while문을 해당 과정을 돌면서 전부 True가 배열 전체에 없다면 반복문 종료하고 total 카운트 출력

import sys 
input = sys.stdin.readline
# n = 땅크기
# l = 인구차이 최소조건
# r = 인구차이 최대조건
# 조건은 최소조건 이상 최대조건 이하임
n, l, r = map(int, input().split())


# c는 나라의 인구수를 담고 있는 배열
# check 해당 나라가 연합나라인지 아닌지를 판단.
c = [list(map(int, input().split())) for _ in range(n)]
check = [[False for _ in range(n)] for _ in range(n)]

# 과정을 얼마나 진행했는지를 갱신
total = 0
# 북 동 남 서 기준
# 현재 위치에서방향을 더했을때
# 범위가 넘어가지 않는 것만 인구차이를 구하기 위해서
dx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

human = 0
while True:
	cnt = 0
	for i in range(n):
		for j in range(n):
			# 연합이 아닌 나라라면
			# 인접한 곳을 검사
			if check[i][j] == False:
				# 인접한 곳이 하나라도 True라면 re를 카운트함
				re = 0
				# 현재좌표에서 총 4방향을 볼 수 있기 때문에
				# 범위가 넘어가지 않나 부터 확인을해야됨
				# 범위가 넘어가지 않고 인접한 면만 검사
				for idx in range(4):
					nx = dx[idx][0] + i
					ny = dx[idx][1] + j
	
					# 정사각형이니까
					if nx < 0 or nx >= n or ny < 0 or ny >= n:
						continue
	
					# 범위 내라면
					# 그 범위 내에 있는 것과 현재 좌표와 인구차이를 계산
					# 인구차이가 범위 내에 들어온다면
					# 연합으로 인정해주고 = True
					# 연합 인구수를 합산해준다
	
					# 만약 인접좌표가 이미 True가 되어있다면
					# 이미 그건 연합으로 인정된것이기 때문에
					# 인구수를 합산하지 않고
					# 현재좌표를 열지 말지에 대한 re카운트만 증가시켜준다
					# re카운트를 증가시키는 조건은 인구차이가 인구차이 조건에 맞을때만 증가시켜준다 맞지 않다면 re를 카운트하지 않는다.
					if check[nx][ny] == False:
						dist = max(c[i][j], c[nx][ny]) - min(c[i][j], c[nx][ny])
						if l <= dist <= r:
							re += 1
							check[nx][ny] = True
							human += c[nx][ny]
					else:
						dist = max(c[i][j], c[nx][ny]) - min(c[i][j], c[nx][ny])
						if l <= dist <=r:
							re += 1
						else:
							continue
	
	
				# 인구합산과 True변환이 모두 끝났다면
				# 인접한곳들중 하나 이상 True 인구차이가 성립된다면
				# 현재 좌표도 true로 만들어준다.
				if re >= 1:
					check[i][j] = True
					human += c[i][j]

	# 그렇제 전부다 탐색하고 나서
	# 합산액이 human에 담겨있고
	# true의 개수 즉 연합의 개수를 세준다
	cnt = 0
	for i in range(n):
		for j in range(n):
			if check[i][j] == True:
				cnt += 1
	# 소수점은 버리기 때문에 Int로 보자
	# 각 나라에 대한 인구수가 나왔기 때문에 True인 나라들을 전부 이 인구수로 바꿔준다

	if cnt != 0:
		value = int(human / cnt)
		for i in range(n):
			for j in range(n):
				if check[i][j] == True:
					c[i][j] = value
	else:
		break
	# 해당 과정이 모두 끝났기 때문에 total 카운트를 증가시켜준다.
	total += 1
	
	# true가 없으면 카운트가 0이기 때문에 전부 False라는 얘기이며 반복문을 종료한다
	# 그렇지 않다면 진행할 수 있기 때문에	
	# check를 다시 초기화하고 다시 구해준다.
	check = [[False for _ in range(n)] for _ in range(n)]
	human = 0

print(total)

# 아 음
# 연합이 하나 존재한다고 했으니까 연합의 크기 자체는 4가 맞는데
# 연합이 하나 존재한다는건 이어져 있는 것들을 말하는거 같은데
# 즉 하나에서 시작해서 연합체들은 True로 될거니까
# 그게 True라면 연합이라는거 자체가 하나로 뭉쳐진다는거니까
# 연합이 되어진 것들과 또 연합이 되어진다면 그것도 연합이락 ㅗ볼 수 있으며
# 연합의 덩어리가 생길거아니야
# 그럼 될 수 있는데까지 연합을 찾아나가면 될거 같은데
# 아 그래서 연합은 하나만 존재한다고 했구나
# 최대한 연합이 묶여질 만큼 문어발식으로 확장하는게 중요한거네
# 만약 연합으로 포함되어있는게 끝까지 해당 연합에서

# [[56, 56, 56, 50], 
# [56, 56, 50, 50], 
# [50, 50, 56, 50], 
# [50, 56, 56, 56]]