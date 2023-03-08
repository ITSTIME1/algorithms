import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 이 풀이도 zip함수를 사용해서 가능하다.

# a, b라는 배열이 주어졌을때 대신 a,b 둘다 길이가 같아야지만 zip함수를 썼을때 올바른 값으로 유도할 수 있을 것이다.
a = [1,2,3,4]
b = [-3,-1,0,2]

print(sum(x*y for x, y in zip(a, b)))

