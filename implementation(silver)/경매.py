# 문제분석

u, n = map(int, input().split())

tra = {}
mani = {}
for _ in range(n):
	s, p = input().split()
	if s not in tra:
		tra[s] = int(p)# 문제 분석
	else:
		mani[s] = int(p)

# 정렬하고
sorted_tra_dic = sorted(tra.items(), key = lambda x : x[1])
min_num = sorted_tra_dic[0][1]

min = 0
peo = []
if min_num <= u:
	for i in sorted_tra_dic:
		if i[1] == min_num:
			min += 1
			peo.append(i[0])
	# min 
	if min >= 2:
		ans = ""
		for i in mani.items():
			if i[1] <= u:
				ans = i[0]
				break
		print(ans+" "+str(i[1]))		