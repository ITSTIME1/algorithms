# 후보 수
n = int(input())
# 추천 수
god = int(input())
# 추천 받은 회원의 목록
reco = list(map(int, input().split()))
# 추천 수를 기록할 딕셔너리 하나 만들어주고
dic = {}
# 시간을 기록할 리스트를 만들어주고
time_index = [0] * n
stu_list, time, isActive = [], 1, False

# 뭔가 방법이 있긴한데
def god_stu(student):
	global time, isActive
	# 아 다시 뭔가 있는데 이거 
	stu_list.append(student)
	# 만약 n보다 커진다면 사진틀이 없다는것이고
	# 만약 사진틀이 부족해진다면 현재 student 는 다음값인 상태이고
	# 그 값이 이미 들어가져 있으니 그 값을 우선 빼준다음에
	# [2, 1, 4] -> 3이 들어와야 한다면
	# 우선 추천수가 가장 작은 값부터 검사를하고
	if len(stu_list) > n:
		stu_list.pop()
		# 여기서 들어온 값이 같은 값일 수도 있기 때문에
		# 추천수만 올리고 시간은 올리지 않는다
		if student in stu_list:
			dic[student] += 1
			isActive = True

		if isActive != True:
			min_value = min(dic.values())
			min_index = []
			#[2, 1, 4]
			# 를 가지고 있을것이며
			for i in dic.items():
				if i[1] == min_value:
					min_index.append(i[0])
			# min_index 에 가지고 있는 값들 중 가장 오래된 값을 구하고
			# 만약 추천수가 같은값이 2명이상 이니까
			# 우선 들어있는 값들의 시간들을 다 증가시켜주고
			# student 값을 바꿔준다
			if len(min_index) >= 2:
				for i in range(len(stu_list)):
					time_index[i] += 1
				pre, pos = 0, 0
				for i in min_index:
					if time_index[stu_list.index(i)] > pre:
						pre = time_index[stu_list.index(i)]
						pos = i
				# 가장 시간이 오래걸린 값을 찾았으며
				# [4, 3, 2]
				# time_index[4] = time_index[0]
				# [0, 3, 2]
				# [3, 1, 4]
				time_index[time_index.index(pre)] = 0
				dic[student] = dic.pop(stu_list[stu_list.index(pos)])
				dic[student] = 0
				stu_list[stu_list.index(pos)] = student
			else:
				# 만약 값이 하나라면
				# 그 값만 cnt 에 있을거니까
				# [2, 4, 3]
				# [2] = 3이라면
				# print(stu_list) = [2, 7, 100]
				# print(min_index) = [7]
				c_index = stu_list.index(min_index[0])
				stu_list[c_index] = student
				time_index[c_index] = 0
				dic[student] = dic.pop(min_index[0])
				dic[student] = 0
		# 같은 값이 들어왔을때
		# dic 증가말고 아무것도 할 필요가 없기 때문에
		if isActive == True:
			isActive = False
		else:
			pass
	else:
		if student in stu_list and student in dic:
			stu_list.pop()
			dic[student] += 1
		else:
			dic[student] = 0
			for i in range(len(stu_list)):
				time_index[i] += 1
			time+=1

for i in range(god):
	stu = reco[i]
	# 구현할 함수
	god_stu(stu)

stu_list.sort()
for i in stu_list:
	print(i, end = " ")

# 3
# 3
# 1 1 1