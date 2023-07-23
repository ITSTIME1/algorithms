import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = 11

# n이 각 자리수의 합으로 나눠서 == 0이 된다면 그건 하샤드수.
# 이런 방법도 생각할 수 있네
n%sum(int(x) for x in str(n)) == 0
answer = n%sum(int(x) for x in str(n)) == 0
print(answer)