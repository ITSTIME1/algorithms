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

if n == 1 and max_val == 0:
	print(0)
	exit()

if n == 1 or n == 5:
	print(stand*max_val + (stand-((stand-n)+1)))
else:
	# 8 * (6//2) + 8-((8-n)+1)
	if max_val % 2 != 0:
		print(stand*((max_val//2) + (max_val % 2)) - (stand-((stand-n)+1)))
	else:
		print(stand*(max_val//2) + (stand-((stand-n)+1)))


# 16 + 1 = 17
 
# 2 5

# 5 // 2 2 1 = 3

# 아직까지는 모듈러 연산이 어떤건지 정확히는 잘 모르겠지만
# 식을 도출하는데 있어서 연관성이 있는거 같다.


# 24 - 1
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 -1



# 나눗셈 연산을 진행했을때
# 1 과 5는 몫이 1이 나오는걸 알 수 있고



# 2 3 4 는 1이 아닌 다른 수가 나오는걸 확인할 수 있네

# 그랬을때 그럼 주기를 // 핑거로 나눈 몫이 1이라면 1주기에서 1씩 차감 된다는 걸 알 수 있고
# 만약 주기를 // 핑거로 나눴을때 1이 아닌 다른 수라면 1주기에서 2씩 차감 된다는 걸 알 수 있으니


# 이걸 일반화 할 수 있나







