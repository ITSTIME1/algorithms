


import sys
from itertools import combinations
input = sys.stdin.readline


# n은 도시크기 n*n
# m은 최대치킨집M개선택
n, m = map(int, input().split())


# 1: [2,3]
# 2: [3,3]..
c_c = {}
# 그럼 이후에 value[0]은 치킨집 좌표를 나타내고 있으니까
# 이후 치킨집에서 M개를 추려낼때 저 값을 가진 key값들을 뽑아내면 [1,2]
# 이런식으로 되니까 value[0]이 = 저 키값들을 가지고 있는 것들의 거리들만 합산하면된다.
# 만약에 저 두거리는 모든 집에 다 있으니까
# 그 중에서 가장 작은 값을 가진 것들 중에 저 둘중에 하나라도 포함되면 가장 작은 값을 합산에 포함시킨다.
# 그래서 정렬을이용해서 봤을때 가장 작은 값이 저 좌표들 중 하나라면 합산.
# "13" : [[1,2], [2, 3]]
h_d ={}

city = [input().split() for _ in range(n)]
	
# 치킨집을 찾아서 h_d에 치킨집 좌표를 저장해주자
index = 1
for i in range(n):
	for j in range(n):
		# 치킨집이라면 치킨집은 중복이 없으니까
		if city[i][j] == "2":
			c_c[index] = [i, j]
			index += 1

# 모든 집들과 거리를 구해주고 저장
for i in range(n):
	for j in range(n): 
		if city[i][j] == "1":
			for k, v in c_c.items():
				dist = abs(i-v[0]) + abs(j-v[1])
				if str(i)+str(j) not in h_d:
					h_d[str(i)+str(j)] = [[k, dist]]
				else:
					h_d[str(i)+str(j)].append([k, dist])

num = set()
for v in h_d.values():
	a = sorted(v, key=lambda x : x[1])
	num.add(a[0][0])




