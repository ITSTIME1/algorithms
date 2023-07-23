import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 1. 주어진 값을 각각의 자릿수의 10^n승 만큼에서 a, b를 빼서 새로운 a,b 에 갱신
# 2. c와 d를 구하는데 c는 더한값을 10^n승에서 빼주고 d는 a, b를 곱한 값으로 정의한다 
# 3. 만약 d의 두자리 초과라면 3자리부터는 계산을 더한다.
# 4. 세자리라면 d값을 100으로 나누고 몫과 나머지가 나오면 몫을 c와 더하고 이걸 c로 갱신
# 5. 나머지를 r이라고 했을때 그걸 뒷자리로 갱신한다.



n1, n2 = map(int, input().split())

# 범위가 10 이상 100미만이기 때문에
# 10~99까지 결국 두자리는 고정이다.
a, b = 100-n1, 100-n2

c, d = 100-(a+b), a * b

q, r = 0, 0
if len(str(d)) >= 3:
	q1 = d // 100
	r1 = d  % 100

	print(a, b, c, d, q1, r1)
	print(c + q1, r1)

else:
	q = d // 100
	r = d % 100

	print(a, b, c, d, q, r)
	print(c, d)