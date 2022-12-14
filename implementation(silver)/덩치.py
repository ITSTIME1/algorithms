
# O(N^2) dictionart problem
N = int(input())
dict_info = {}
cnt_info = {}
for _ in range(N):
	x, y = map(int, input().split())
	dict_info[_] = (x, y)
	cnt_info[_] = 0
# 몸무게를 기준으로 정렬을 해주고
sorting_dict = sorted(dict_info.items(), key = lambda x : x[1])

# 몸무게를 하나씩 비교해주고
# 0 1 2 3
for i in range(len(sorting_dict)):
	cnt = 0
	for j in range(len(sorting_dict)):
		# 몸무게와 키를 다 검사해봤을 때
		# 자기보다 큰 사람이 있다면 cnt += 1
		if sorting_dict[i][1][0] < sorting_dict[j][1][0] and sorting_dict[i][1][1] < sorting_dict[j][1][1]:
			cnt+=1
	cnt_info[sorting_dict[i][0]]+=cnt+1
# 맵핑시켜둔 다음에
# 일반 for문
# for value in cnt_info.values():
# 	print(value, end = " ")

# pythonic 하게
arr = [value for value in cnt_info.values()]
print(*arr)