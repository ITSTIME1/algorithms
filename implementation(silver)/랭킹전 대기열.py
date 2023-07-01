

# import sys
# input = sys.stdin.readline

# # 플레이어 수, 방의 정원
# p, m = map(int, input().split())

# group = []
# for i in range(int(p)):
# 	l, n = input().split()

# 	# 처음 입장했을때는 방이 없으니까 방을 생성해준다.
# 	if len(group) == 0:
# 		group.append(["Waiting!", [[int(l), n]], int(l)-10, int(l)+10])
# 		continue

# 	# 처음 입장한게 아니고 방에 입장할 수 있는지 보자
# 	# 입장할 수 있다면 그리고 정원이 차지 않았다면
# 	# 들어갈 수 있으니까 들어가 준다.
# 	# 그리고 출력할때도 출력하기 편하게 하기 위해서
# 	# 미리 정렬을 해준다.
# 	flag = False
# 	for j in group:
# 		# 들어갔다면 더 이상 탐색할 필요가 없지
# 		# 그룹을 더 이상 탐색하지 않아 도된다.
# 		if len(j[1]) < int(m) and j[2] <= int(l) <= j[3]:
# 			j[1].append([int(l), n])
# 			flag = True
# 			break
	
# 	# 만약 입장할 수 없다면 방을 만들어준다.
# 	if not flag:
# 		group.append(["Waiting!", [[int(l), n]], int(l)-10, int(l)+10])


# # l이 영향을.. 이것도 sort문제...

# for i in group:
# 	s = i[1]
# 	result = []
# 	ans = sorted(s, key=lambda x: x[1])
# 	if len(s) == int(m):
# 		i[0] = "Started!"
# 	print(i[0])
# 	for level, name in ans:
# 		print(level, name)





import sys
input = sys.stdin.readline

# 플레이어 수, 방의 정원
p, m = map(int, input().split())

group = []
group_number = 1
for i in range(p):
	l, n = input().split()

	# 해당 플레이어가 들어갈 방이 있는지 없는지를 검사해주는데
	# 처음에는 무조건 없으므로 무조건 방을 만들어주어야 한다.
	if len(group) == 0:
		group.append(["Waiting!", [[int(l),n]], int(l)-10, int(l)+10, group_number])
		group_number += 1
		continue


	# 만약 들어 왔는데 방이 없는지부터 계산을 해주어야 하기 때문에
	# 레벨 내가 들어갈 수 있는 방의 레벨 범위부터 검사해주자
	s = []
	for j in group:
		# 레벨 범위에 들어가면서 정원이 다 차지 않는 것의 그룹 넘버를 가지고온다.
		if len(j[1]) < m and j[2] <= int(l) <= j[3]:
			s.append(j[4])
			break

	# 만약 그러한 그룹을 가지고 오지 못했다면
	# 들어갈 수 있는 방이 없는 것이기 때문에 방을 생성해주어야한다.
	# 들어갈 수 있는 방이 없다고 한다면
	if len(s) == 0:
		group.append(["Waiting!", [[int(l), n]], int(l)-10, int(l)+10, group_number])
		group_number += 1
	else:
		# 들어갈 수 있는 방이 여러개인것을 감안한다면
		# 가장 그룹의 번호가 먼저 생긴걸 기준으로 들어와야 되기 때문에
		# 그룹의 번호를 기준으로 가장 작은걸 선택한다.
		# 그러면 이 그룹의 번호가 포함된것에 닉네임을 넣어준다 [10, a]
		# 거기에 넣어주고 난다음에 이후에
		for k in group:
			if s[0] in k:
				k[1].append([int(l), n])

# 출력은 어떻게 할까
for i in group:
	# started는 앞에다가 빼주고
	# 시작 유무와 출바꿈으로 구분된다.
	ans = sorted(i[1], key=lambda x:x[1])
	if len(ans) == m:
		i[0] = "Started!"
	print(i[0])
	for level, name in ans:
		print(level, name)