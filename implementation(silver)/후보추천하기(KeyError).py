# 문제분석
# 왜 keyError 가 나지..?
n = int(input())
reco = int(input())

s = list(map(int, input().split()))

s_list = []
dic = {}
def god(student):
	# 사람이 채워지기 전까지 s_list 에 후보를 넣고
	s_list.append(student)
	if s_list.count(student) >= 2:
		dic[student] += 1
		s_list.pop()
	# 다 채워진상태에서
	# 같은숫자가 들어왔을때
	if len(s_list) > n:
		st = s_list.pop()
		min_value = min(dic.values())
		ct = []
		for i in dic.items():
			if i[1] == min_value:
				ct.append(i[0])
		if len(ct) >= 2:
			# 2, 1, 4
			pos = []
			for i in ct:
				pos.append(s_list.index(i))
			# 가장 작은 값
			min_pos = min(pos)
			dic_pos = s_list[min_pos]

			s_list.pop(min_pos)
			s_list.append(st)
			# 딕셔너리 체인지
			dic[st] = dic.pop(dic_pos)
			dic[st] = 0
		# 한명이라면
		elif len(ct) == 1:
			s_index = s_list.index(ct[0])
			s_list.insert(s_index, st)
			dic[st] = dic.pop(ct[0])
			dic[st] = 0

	else:
		# 만약에 후보는 다채워지지 않은 상태에서
		# 같은 후보 추천이 들어왔다면
		if student in s_list and student in dic:
			dic[student] += 1
		else:
			dic[student] = 0

	print(dic)
for i in range(reco):
	stu = s[i]
	god(stu)

s_list.sort()
for i in s_list:
	print(i, end = " ")

# 3
# 3
# 1 1 1
# 1 로 잘나오는데
