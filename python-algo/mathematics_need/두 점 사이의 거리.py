import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 두 점 사이의 거리를 구하는 방법은 총 세가지가 있다.


# 1. 유클리드 거리 = 우리가 흔히 알고 있는 피타고라스의 정리의 의해서 구하는 방법
# 2. 맨해튼 거리 = 유클리드와 다른 점은 절대값을 바로 합산하는 방식을 쓴다.
# 3. 해밍 거리 