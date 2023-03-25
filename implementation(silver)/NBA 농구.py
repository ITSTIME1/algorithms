import sys
import heapq
import math
import datetime
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 오케이 해보자


# 득점 개수
n = int(input())


# 스코어변수
team_1, team_2 = 0, 0

# 업데이트할 시간.
hash_table = {1: 0, 2: 0}

stand = 48*60

win = 0
winner_time = 0

for i in range(n):
	team, time = map(str, input().split())
	# 분과 초로 바꾸고
	min, sec = map(int, time.split(":"))
	# 얻은 시간
	get_time = min*60+sec
	if i == 0:
		if int(team) == 1:
			team_1 += 1
			win = 1
			
		else:
			team_2 += 1
			win = 2

		winner_time = get_time

	else:	
		if int(team) == 1:
			team_1 += 1
		else:
			team_2 += 1


		if team_1 == team_2:
			a = get_time - winner_time
			hash_table[win] += a
			win = 0
		# 여기서만 수정해보자
		if win == 0 and team_2 > team_1:
			winner_time = get_time
			win = 2
		elif win == 0 and team_1 > team_2:
			winner_time = get_time
			win = 1

if win != 0:
	get = stand - winner_time
	hash_table[win] += get


print('{:0>2}:{:0>2}'.format((hash_table[1])//60, (hash_table[1])%60))
print('{:0>2}:{:0>2}'.format((hash_table[2])//60, (hash_table[2])%60))




# 그치 이렇게 푸는게 맞는거지
# 시간 계산 문제에 좀 더 익숙해질 필요가 있다
# 아래 프린트문 문법도 어떤건지 정확히모르니까 
# 시간 변환 공부 + 출력공부 다시 해볼 필요가있다.
# 아이디어는 맞았으니 다른 코드도 좀 봐야겠다

# 1. 시간변환
# 2. 출력형태공부
# 3. 이 문제 다른 사람 코드 공부




