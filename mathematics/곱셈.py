import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = list(map(int, input().split()))

a, b, c = n[0], n[1], n[2]

# 제곱은 상대적으로 커질 수 있으니까
# O(log2N)의 시간복잡도를 가지고 있고
# 그 이유는 분할 정복을 이용하기 때문
# 2^4 = 2^2 * 2^2
# 2^5 = 2^2 * 2*2 * 2


# 저 공식을 베이스롤 수가 커지는걸 방지하기 위해 매번의 계산마다 c로 나눈걸 리턴

def power(x, p, s):
    if p == 0:
        return 1
    
    re = power(x, p//2, s)

    if p % 2 == 0:
        return (re*re) % s
    
    else:
        return (re * re * x) % s

print(power(a, b, c))
