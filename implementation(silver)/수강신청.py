# 뭘 해도 시간초과가 나는데
# hash 로 다시 접근해볼까


import sys

dic = {}
k, l = map(int, sys.stdin.readline().strip().split())

for i in range(l):
	number = sys.stdin.readline().strip()
	dic[number] = i

print(dic)
sorted_dic = sorted(dic.items(), key = lambda item : item[1])

# 왜 sorteㅇ 를 사용하냐
# 우선 대기열에 저장해둔 값중에서 수강신청을 두번 누른 학생은 학번이 두번 뜨게된다
# 먼저 수강신청을 누른 사람이 먼저 대기열에 들어가기 때문에
# 만약 수강신청을 한번더 클릭했다면 2 < 3 이런식으로 수강신청 횟수의 우선순위를 정해볼 수 있다
# 가령 예제에서2013221, 2013221 이라면 들어온 순서대로 번호를 매겨본다면
# 앞에게 2 뒤에게 3으로 된다 그렇게 된다면 두번 누른 건 대기열의 맨 뒤로 가야 되기 때문에
# dic의 성질을 이용한다면 같은 값이 들어온다면 i값을 바꾸니까 마지막으로 들어온 값으로 바꾼다는 것
# 그리고 나서 다음 값이 들어오고 쭉 들어오다가
# 어떤 사람이 이미 대기열에 넣었는데 또 한번 수강신청을 누른다면
# 맨 뒤의 번호가 우선순위가 되어야 하기 때문에
# 앞에 있는 번호를 덮어 씌울 수 있다
# 그렇게 되면 문제에서 대기열의 맨 뒤로 간다는게 성립이 된다

# 이렇게 되면 정렬이 되지 않은 상태로 되어 있다
# 순서가 뒤죽박죽이 될 수 있기 때문에

# 가장 앞에 있는 사람부터 수강신청이 완료된다면
# 어짜피 실시간으로 이루어지기 때문에
# 해당 번호가 맨 뒤의 열의 순서로 덮여졌지만
# 그 순서는 정렬된 상태가 아니므로
# 정렬이 필요하다
# 때문에 정렬을 하게 된다면 대기열의 맨 뒤로 가게 된다는 의미가 충족됨과 동시에 가장 앞에서부터
# 정상적으로 들어온 사람의 순서대로 수강신청이 되는 것이다.

print(sorted_dic)
index = 0
for i in sorted_dic:
	if index == k:
		break
	print(i[0])
	index+=1
	



# import copy
# import sys

# O(2n)
# k, l = map(int, sys.stdin.readline().strip().split())
# arr = []
# for i in range(l):
# 	number = sys.stdin.readline().strip()
# 	arr.append(number)

# # 대기목록에 일단 다 넣어주고

# cpy_arr = arr.copy()
# for i in arr:
# 	if cpy_arr.count(i) >= 2:
# 		c = cpy_arr.index(i)
# 		del cpy_arr[c]

# print(*cpy_arr[:k], sep ="\n")