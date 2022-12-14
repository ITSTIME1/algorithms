import copy

n = int(input())
arr = [input() for _ in range(n)]

first = list(arr[0])

dic = {}
for i in first:
	if i in dic:
		dic[i] += 1
	else:
		dic[i] = 1

ans = 0
for i in range(1, len(arr)):
	check = arr[i]
	# 안되는 조건들
	if len(first)+1 < len(check) or len(first)-1 > len(check):
		continue
	word = []

	cpy_dic = copy.deepcopy(dic)
	for j in check:
		if j in cpy_dic and cpy_dic[j] != 0:
			cpy_dic[j] -= 1
			continue
		elif j in cpy_dic and cpy_dic[j] == 0:
			word.append(j)
		else:
			word.append(j)
	# 그럼 이제 여기 1개가 남았을때를 알아야 하는데
	# 이부분이 계속 틀리네
	
	if len(word) == 1:
		cnt = 0
		# DOG
		# 00x0
		# GOOD
		for i in cpy_dic:
			if cpy_dic[i] == 0:
				cnt += 1
		if cnt == len(first):
			ans += 1
	if len(word) == 0:
		ans += 1
print(ans)

# 내 논리대로라면 a가1이니까 이걸 개수를 하나 줄여주고
# 잠깐 결국

# 2
# ABB
# AAA



# 5
# AB = first
# A = o []
# BB = o B
# CB = [c] o
# P = [x] x

# 5
# AB
# A
# CB
# BB
# P

# AB
# P

# [C]
# [P]