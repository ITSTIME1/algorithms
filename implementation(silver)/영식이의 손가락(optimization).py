import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 오케이 정답

# 뭔가 주기 성을 찾고 그 식을 만들면 정답이되는거 같다

# 주기를 찾는게 핵심이면서
# 모듈러 연산을 적절히 활용할 줄 알아야 하는 문제 같았다
# 만약 n == 1 max_val == 0 엄지이면서 시작도 못하기 때문에
# 문제의 내용대로 0을 출력해주고


# 만약 그런게 아니라면 max_val 을 2로 나누었을때 0이 되는지 되지 않는지를 알아야 한다
# 0이 되냐 안되냐가 식이 달라진다


n = int(input())
max_val  = int(input())

# 1과 5가 나올 수 있고
stand = 8
get = stand - n 
get_1 = get+1

if n == 1 and max_val == 0:
	print(0)
	exit()

if n == 1 or n == 5:
	# print(stand*max_val + (stand-((stand-n)+1)))
	print(stand*max_val + (stand-get_1))
else:
	# 8 * (6//2) + 8-((8-n)+1)
	if max_val % 2 != 0:
		print(stand*((max_val//2) + (max_val % 2)) - (stand-get_1))
	else:
		print(stand*(max_val//2) + (stand-get_1))



# 계산을 미리 해둔다음 그 식을 가지고 계산하면 좀 더 빠른 성능을 기대할 수 있다.
# 식을 더 간소화 해보자
# print(stand*max_val + (stand-get_1))


