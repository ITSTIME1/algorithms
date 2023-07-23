import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

s = "Zbcdefg"

# sorted() 함수는 파이썬의 내장함수인데
# 새로운 정렬된 리스트로 만들어서 반환해주는 역할을 한다.

# 그럼 sort()와 sorted()차이를 알아야하는데

# list.sort() 같은 경우는 본체의 리스트를 정렬해서 반환하는것 즉 본체를 직접적으로 정렬을 시키는 함수고
# sorted(list, reverse=True|False) 값은 본 list 값은 두고 그 리스트를 새로 정렬한 리스트를 반환한다는것.

# 다시말해 직접적으로 본체리스트를 건드냐 안건드냐의 차이다.
# sorted()의 reverse 값을 따로 정해주지 않는다면
# 디폴트값으로 오름차순이 진행이된다. 즉 reverse=False
answer = "".join(sorted(s, reverse=True))


# 그럼 sorted() 딕셔너리의 key를 정렬한다면?
d = dict()
# d라는 dic테이블이 존재할때 값이 있다고 가정하고

f = sorted(d.items()) d딕셔너리 기준 오름차순으로 정렬이 진행이된다.
f1 = sorted(d.items(), reverse=True) d딕셔너리 기준 내림차순으로 정렬이 된다.
f2 = sorted(d.keys()) 키만 정렬하게 된다.