# 문제분석

# 위성사진을 바탕으로 실시간 순위를 계산하려고 한다.


# 모든 글자의 처음은 s 로 시작하고
# s = 출발선을 의미한다
# f = 결승선을 의미한다.

# . = 물
# 대회에참가한 팀은 총 9개의팀 각팀은 1~9번호로 매겨져있다.


# 결승선으로부터 가까울 수록 순위가 높다
# 만약 두팀이 결승선과 떨어진 거리가 같다면 같은 등수로 매긴다


# f + "." 물의 개수로 따지면 거리겠네
# 거리를 계산 하는 방법은 많은데
# 그럼..
# dic 으로 해야겟따

# 카약은 항상 9개

# 그럼 그냥 하나씩 뚫어보면 되겠네

r, c = map(int, input().split())

map_v = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
	arr = input()
	map_v[i] = arr



def isDigit(arr):
	isDigit = False
	for i in arr:
		if i.isdigit():
			isDigit = True
	return isDigit

final = c-1
arr = []
for i in range(r):
	for j in range(c):
		

# 아 ㅇㅋ 문제를 잘못 이해했네.



S..........222F 1 두번째팀
S.....111.....F 5 첫번째팀
S...333.......F 7
S...555.......F 7
S.......444...F 3
S.............F 0
S......777....F 4
S..888........F 8
S........999..F 2
S...666.......F 7