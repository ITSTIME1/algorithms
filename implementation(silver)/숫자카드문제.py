import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


number = deque(list(map(str, input().split())))


def min_Val(num):
	a = deque(list(map(str, num)))
	ar = [int("".join(a))]
	for i in range(3):
		b = a.popleft()
		a.append(b)
		ar.append(int("".join(a)))
	return int(min(ar))

# minVal을 구하는 또 다른 방법
# python의 슬라이싱 기능을 이용한 방법
# [i:] i 부터 시작해서 end를 지정하지 않았으므로 끝까지 가지고온다
# [:i] 거꾸로 i까지의 모든 수를 가지고 온다.
# min 의 값을 계속해서 갱신해서 가지고 온다.
# 디큐를 썼지만 더 괜찮은 방법인것 같기도 하네 메모리 측면에서 당연히 우수할거 같다.
def get_clock_num(n):
    min = int(''.join(map(str, n)))
    for i in range(1,4):
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    return min
# 그럼 가장 작은 시계수를 구한거고
# 이제 모든 시계수들을 검사해야하는데

# 정렬했을때같다면?
# 1122
minVal = min_Val(number)
# minVal 이랑 다른지만 체크하면 되자나
# 이 문장을 이해하는게 핵심이네
# 모든 가능한 십자카드가 주어질 때 각각의 카드는 다음과 같은 시계수 라는 번호를가진다.

# 즉 위에 주어진것만 시계수로 주어지는것이 아니라
# 1111~minVal 시계수또한 시계수라는걸 각각 갖는다는 의미다.
# 문해력보단 이걸 캐치하는 사람이 얼마나 있을까..
cnt = 0
for i in range(1111, minVal):
	if "0" not in list(str(i)) and i == min_Val(list(str(i))):
		cnt += 1

# +1 해주는 이유는 minVal의 위치는 결국 모든 수들의 +1번째이기 때문이다.
print(cnt+1)



# 문제를 잘 이해해야된다 문제를;;

