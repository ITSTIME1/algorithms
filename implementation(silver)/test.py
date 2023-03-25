import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = [1, 2, 3, 4]

print(n[1:])
print(n[:1])
print(n[1:] + n[:1])
# 슬라이싱 자체가 리스트로써 하나의 객체를 만들고
# 슬라이싱 끼리의 연산을 통해서 리스트가 하나로 합쳐지는걸 볼 수 있다.


# 따라서 "".join(map(str, n[1:] + n[:1]))

# 리스트를 하나로 합친다음 그걸 str타입으로 바꾼 뒤 join해서 하나의 숫자로 만들 수 있다는것.

# 음 ㅇㅋ
