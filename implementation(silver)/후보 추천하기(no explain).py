n = int(input())
god = int(input())
reco = list(map(int, input().split()))

dic = {}

time_index = [0] * n
stu_list, time, isActive = [], 1, False


def god_stu(student):
	global time, isActive
	stu_list.append(student)

	if len(stu_list) > n:
		stu_list.pop()
		if student in stu_list:
			dic[student] += 1
			isActive = True

		if isActive != True:
			min_value = min(dic.values())
			min_index = []
		
			for i in dic.items():
				if i[1] == min_value:
					min_index.append(i[0])
	
			if len(min_index) >= 2:
				
				for i in range(len(stu_list)):
					time_index[i] += 1

				pre, pos = 0, 0
				for i in min_index:
					if time_index[stu_list.index(i)] > pre:
						pre = time_index[stu_list.index(i)]
						pos = i
				
				time_index[time_index.index(pre)] = 0
				dic[student] = dic.pop(stu_list[stu_list.index(pos)])
				dic[student] = 0
				stu_list[stu_list.index(pos)] = student
			else:
				c_index = stu_list.index(min_index[0])
				stu_list[c_index] = student
				time_index[c_index] = 0
				dic[student] = dic.pop(min_index[0])
				dic[student] = 0

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
	god_stu(stu)

stu_list.sort()
for i in stu_list:
	print(i, end = " ")
