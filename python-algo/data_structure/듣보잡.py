# 문제분석

# 일단 이건 set 자료형을 이용하면 금방 찾을거 같은데
# n, m 의 개수만큼 사람의 이름이 주어지니까
# 그 사람의 이름을 각각 모아서
# 아니다 해당 이름들을 그냥 한번에 받아서
# dic에 추가하고
# 기존 dic 에 있다면 += 1
# 기존 dic 에없다면 추가
# 해서 각 명단에 중복되는 이름은 없기 때문에
# 최소 2번이 나온다
# 그럼 2번나온 이름을 찾으면 끝

import sys
n, m = map(int, sys.stdin.readline().strip().split())

dic = {}
for i in range(n+m):
	pl = input()
	if pl not in dic:
		dic[pl] = 0
	else:
		dic[pl] += 1

pl, cnt = [], 0
for i in dic.items():
	if i[1] == 1:
		pl.append(i[0])
		cnt += 1
pl.sort()
print(cnt)
print(*pl, sep = "\n")
