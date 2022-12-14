# 문제분석

# 한번 분석해볼까

# 아이스크림이 있는데

# N 종류의 아이스크림이 있고 그 중에 3개의 아이스크림을 선택한다고 했을 때
# 아이스크림의 번호는 1 부터 N 까지의 번호로 구성되어져 있다고 한다 = 만약 N = 5라면 1, 2, 3, 4, 5
# 까지의 번호가 있고 저 5 종류의 아이스크림 중에서 3개를 조합해서 아이스크림을 만든다고 했을때
# 섞어 먹으면 안되는 조합이 있다고 한다
# 그 조합은 피해서 몇가지의 종류를 만들 수 있는지 해보자
# 1,2,3 (1, 2) 가 주어졌다고 생각해보면
# 1,2 가 포함이 안되어야 하는데 1, 2 가 포함이 되어있고
# 3, 4 는 같이 포함이 안되어 있기 때문에 이 경우의 수는 가능하지만
# 1, 3 이 경우의 수는 두 수가 포함이 되어 있기 대문에 불가능하다 때문에 1,2,3 은 불가능
# 주어진 경우의 수를 전부다 피하는 아이스크림의 조합을 생각해야 된다.

# 우선 조합을 만들고
# 그 조합된 수랑 같이 조합하면 안되는 수랑 비교해본다
# 비교한다음 해당 수들이 다 통과가 된다면 따로 딕셔너리에 넣어주자
# 

from itertools import combinations
# import time

# start = time.time()

n, m = map(int, input().split())
com = []
for i in range(m):
	f, s = map(int, input().split())
	com.append([f, s])

r_cnt = 0
for j in combinations(range(1, n+1), 3):
	num = list(j)
	ans = 0
	for k in com:
		if len(set(k) & set(num)) != 2:
			ans += 1
	if ans == m:
		r_cnt += 1
print(r_cnt)

# print(time.time() - start)