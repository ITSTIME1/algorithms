# 문제분석

# 4, 4

# [1,2,3,4]

# 12 = 21 = re 6
# 34 = 43 = re 

# 13 = 31 = re 2 + 7 = 9
# 24 = 42 = re 6 + 4 = 10

# 14 = 41 = re
# 23 = 32 = re

# [1,2,3,4,5,6]

# 이건 단순 완전탐색은 아니고 bfs, dfs 백트래킹이 들어가야 되는문제임.
# 뭔가 아이디어 시도는 좋았던거 같은데
# 일단 아래 방법으론 False 체크가 2개 이상 체크되는 시점에서 일단 안됨

# 백트래킹 과 dfs bfs 를 배우자..

from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

com = list(combinations(range(1, n+1), 2))

dp = [False] * n

result = []
for i in com:
	check = list(i)
	for j in check:
		dp[j-1] = True
	start = 0
	link = 0
	# [1, 2]
	# [0, 1]
	# 0, 1
	for j in range(len(check)-1):
		st1, st2 = arr[check[j]-1][check[j+1]-1], arr[check[j+1]-1][check[j]-1] 
		start += st1+st2

	# 여기서 2개 이상 선택이 안되는구나
	# 이걸 생각을 못했네..
	link_list = []
	for k in range(len(dp)):
		if dp[k] == False:
			link_list.append(k+1)

	for j in range(len(link_list)-1):
		li1, li2 = arr[check[j]-1][check[j+1]-1], arr[check[j+1]-1][check[j]-1] 
		link += st1+st2

	max_num, min_num = max(start, link), min(start, link)
	c = max_num - min_num
	result.append(c)
	# dp 초기화
	for i in dp:
		dp[i] = False

print(min(result))



