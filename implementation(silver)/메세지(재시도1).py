

def makelist(stu):
	p_list = []
	for key in stu.items():
		p_list.append(key[0])
	return p_list


group = 1
while True:

	n = int(input())
	if n == 0:
		break	
	
	stu = {}
	for i in range(n):
		p = list(map(str, input().split()))
		if p[0] not in stu:
			stu[p[0]] = p[1:]
	# 사람을 리스트로 만들어서
	stu_list = makelist(stu)

	# ['Ann', 'Bob', 'Clive', 'Debby', 'Eunice']
	ans = []
	for key, value in stu.items():
		name = key
		check = value
		if check.count("N") >= 1:
			nlist = []
			for j in range(len(check)):
				if check[j] == "N":
					nlist.append(j+1)

			if len(nlist) != 0:
				for k in nlist:
					a = stu_list.index(name)
					# 0 + 2
					# 3 - 2
					# 0 - 2
					# 범인이다!
					no = stu_list[a - k]
					complete = str(no) + " was nasty about " + str(name)
					ans.append(complete)
			else:	
				continue
	if len(ans) == 0:
		print("Group " + str(group))
		print("Nobody was nasty")
		print(" ")
		group += 1
	else:
		print("Group " + str(group))
		for i in ans:
			print(i, end = "\n")
		print(" ")
		group += 1


