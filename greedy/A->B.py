import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

a, b = map(int, input().split())



# 2로 나누어 떨어진다면 2로 나누고
# 만약 2로 나누어 떨어지지 않는 홀수들이 있는데
# 그런 홀수들은 마지막이 1이냐 아니냐에 따라 다름
# 만약 마지막이 1이면 1을 빼고 cnt += 1

# 만약 마지막이 1이 아니라면 중지 어떻게 선택지가 없자나

cnt = 0
while b > a:
	if b % 2 == 0:
		b//=2
		cnt += 1
	else:
		if str(b)[-1] == "1":
			b = int(str(b)[:-1])
			cnt += 1
		else:
			break

# 2 23
# 23은 더이상 해볼 수 있는 방법이 없으니까
# 결국 a!=b가 다르게 되어 -1을 출력하게됨
if b != a:
	print(-1)
else:
	print(cnt+1)

# 됐다..