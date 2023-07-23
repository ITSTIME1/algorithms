doo = input()
N = int(input())

arr = []
team_name = []
for _ in range(N):
	team = input()
	team_name.append(team)
	for _ in team:
		L = doo.count("L") + team.count("L")
		O = doo.count("O") + team.count("O")
		V = doo.count("V") + team.count("V")
		E = doo.count("E") + team.count("E")
	result = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
	arr.append((result, team))
	# [(), (), ()]
	# 리스트에 튜플이 들어가 있는 형태.
	# 이런 식일 경우 리스트 내 튜플을 람다를 이용해서
	# 정렬이 가능하다

# 기본 값은 오름차순이다.
# 현재 여기서 x[0] 은 숫자가 들어있는데
# 기본적으로 오름차순으로 정렬이 된다.

# 두번째 파라미터는 문자열인데 문자열은
# 알파벳, 가나다순 으로 정렬이 된다.
# -부호를 이용해서 숫자는 역순으로 출력이 가능하다.
arr.sort(key = lambda x : (-x[0], x[1]))
print(arr)
print(arr[0][1])

# 정렬된 결과를 반환. 원형을 변형시키지 않는다.
# 괄호( ) 안에 반복 가능한 iterable 자료형을 입력하여
#  사용한다. 
#  정렬 기준은 문자열은 알파벳, 
#  가나다순이고 
#  숫자는 오름차순이 기본값이다.
#  # '-'부호를 이용해서 역순으로 가능



# 다른 사람 풀이
# ms = input()
# n = int(input())
# li = sorted([input() for i in range(n)])
# print(li)
# max_p = max_i = 0
# for i in range(n):
#     L = ms.count("L") + li[i].count("L")
#     O = ms.count("O") + li[i].count("O")
#     V = ms.count("V") + li[i].count("V")
#     E = ms.count("E") + li[i].count("E")
#     p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
#     print(p)
#     if max_p < p:
#     	max_p = p
#     	max_i = i

# print(li[max_i])