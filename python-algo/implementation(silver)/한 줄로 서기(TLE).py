# 문제분석
# N 명의 사람들은 한줄로 선다 = 선형

# 자리는 바꾸지 못한다

# 대조 한다
# 처음위치와 바뀐 위치를
# 사람들은 자기보다 큰 사람이 왼쪽에 몇명 있었는지만 기억한다

# N명의 키는 각각 다르다
# 각 사람이 기억하는 정보가 주어질대 줄을 어떻게 서야 하는지

# 음
# 먼저 첫번쨰와 마지막 사람을 정한다
# 첫번재 사람은 가장 크기 때문에 가장 큰 사람들이고
# 마지막 사람은 가장 많이 보이는 사람들인데...

# 이걸 순열로 이용한다면?
# 나열을 해서
# 각각의 수의 가장 큰 사람이 몇명인지 dic 체크해두고
# hashtable 을 이용해서 
# 각각의 옆의 가장큰 수가 몇개 있는지 알아본다면 가능할지도?


# 순열 쓰면 TLE..
import itertools


n = int(input())
key = list(map(int, input().split()))



dic = {}
for i in range(n):
	dic[i+1] = key[i]

for i in itertools.permutations(range(1, n+1), n):
	check = list(i)
	# [4, 2, 1, 3]
	total = []
	for j in range(len(check)):
		# 사람을 가지고 와서
		# 해당 사람이 가지고 있는 키 값을 가지고 온뒤\
		# [4, ]
		key = dic[check[j]]
		cnt = 0
		for k in total:
			if len(total) == 0:
				total.append(check[j])
			else:
				if k > check[j]:
					cnt += 1

		if cnt == key:
			if check[j] not in total:
				total.append(check[j])
			else:
				pass
	if len(total) == n:
		print(*total, end = " ")
		break

