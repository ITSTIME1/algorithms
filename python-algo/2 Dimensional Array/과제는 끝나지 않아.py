import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

# 이전과제용
pre = []
# 총 점수
score = 0
# 과제 시간재기
hash_table = {}
# 과제 번호부여
index = 1

for _ in range(n):
	sub = list(map(int, input().split()))
	# 과제가 1인지 0인지
	# sub[0]
	# 과제 점수
	# sub[1]
	# 과제의 시간
	# sub[2]
	check_sub=grade=sub_time=0
	# 0이 아니라면 변수에 저장해두고
	if len(sub) != 1:
		check_sub = sub[0]
		grade = sub[1]
		sub_time = sub[2]
		# 여기는 이제 과제가 있는거 처리를하면되지
		sub_time -= 1
		if sub_time == 0:
			score += grade
		else:
			hash_table[str(index)] = [grade, sub_time]
			pre.append(index)
			index += 1

	else:
		# 이전과제 에대한 처리
		if len(pre) == 0:
			continue
		else:
			# 이전과제를 확인하기 위한 변수를 남기고
			a = pre[-1]
			check_grade = hash_table[str(a)][1] - 1
			if check_grade == 0:
				score += hash_table[str(a)][0]
				del hash_table[str(a)]
				pre.pop()
			else:
				hash_table[str(a)][1]-=1

print(score)






