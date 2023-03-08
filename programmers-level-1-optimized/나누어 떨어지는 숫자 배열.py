import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# array의 각 요소들중에서 divisor로 나누어 떨어지는 값을
# 오름차순으로 정렬한 배열을 리턴하라고 하는데
# 기본적으로 간단하게 for문으로 구현 하면 되는데 여기서는
# 리스트 컴프리헨션을 사용해서 구현을 해보겠다.

array = [3, 2, 6]
divisor = 10
# 기본적인 문법은 동일하지만 or을 사용해서 배열의 든 값이 없을때 -1을 출력하게되는데
# or연산은 기본적으로 둘 중 하나가 참이면 참을 반환하게 되어있다.
# 그럼 이 문제에서 or의 종류는 두가지.
# 1. 요소들을 divisor로 나누었을 때 = 0 으로 된다면 배열에 추가되는 상태.
# 2. divisor로 나누었을때 배열에 추가되지 않는 상태가 있을것이다.
# 문제에서는 배열의 아무값도 없을때(divisor로 나누어봤지만 아무값도 0이되는 값이 없을때)
# 그때 [-1]을 출력하라 했으므로 둘중의 참인 경우는 [-1]이 참이기 때문에 -1을 출력하게 된다.
answer = sorted([i for i in array if i%divisor == 0]) or [-1]
print(answer)

