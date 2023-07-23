import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이건 두 정수 a,b 가 주어졌을때
# a부터 b까지의 수들의 합을 구하는 문제.

# 보통 이런경우 for 문을 돌려주면 되지만
# a > b 큰 경우만 생각해주면 쉽게 풀 수 있는 문제다.
# 왜냐하면 5~3까지는 for문으로는 그냥 543이런식으로 돌려지지 않는다
# 다라서 역순으로 탐색을 해주어야 하는데
# -1씩 줄이는 방법이 있지만
# 어짜피 a와 b 사이의 수들이기때문에
# 3-5나 5-3이나 a,b(포함)사이의 정수들은 정해져있기 때문에
# a, b = b, a로 스왑하여 구해도 되는 것이다.


a, b = 3, 5
a1, b1 = 5, 3

if a1 > b1:
	a1, b1 = b1, a1
print(sum(range(a1,b1+1)))

