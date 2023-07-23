# 문제분석


def find(num, people):
	for key, value in people.items():
		if value[0] == num:
			return key

group = 1
while True:
	n = int(input())	
	if n == 0:
		break

	people = {}

	for i in range(n):
		paper = list(map(str, input().split()))
		if paper[0] not in people:
			people[paper[0]] = [i, paper[1:]]

	ans = []
	# for 문을 이용해서 key, value 를 받아오고
	# 받아온다음에 n 값을 검사한다음에

	for key, value in people.items():
		check = value[1]
		n_list = []
		if check.count("N") >= 1:
			for j in range(len(check)):
				if check[j] == "N":
					n_list.append(j+1)
			# n_list = [2]
			# Ann P N N P
			# people
			if len(n_list) != 0:
				for k in n_list:
					num = value[0] + k+1
					if num >= len(check):
						num //= len(check)
					# 해당 사람을 찾았으니까
					name = find(num, people)
					comple_string = str(name)+" was nasty about "+str(key) 
					ans.append(comple_string)
		else:
			continue
	

	if len(ans) == 0:
		print("Group"+" "+str(group))
		print("Nobody was nasty")
		print(" ")

	else:
		print("Group"+" "+str(group))
		for i in ans:
			print(i, end="\n")
		print(" ")
		group += 1


# Ann P N P P = Debby
# Bob P P P P 4
# Clive P P P P 3
# Debby P N P P 2
# Eunice P P P P 1

# 왼쪽으로 전달해준다고 했으니까
# ann papaer 기준으로
# 왼쪽의 첫번재는 eun eun 은 ann 한테 p
# 왼쪽의 두번쨰는 debby debby 는 ann 한테 n
# 왼쪽의 세번째는 clive 클리브는 ann 한테 p
# 마지막

# 우선 아이들의 페이퍼를 하나씩 가지고오고


