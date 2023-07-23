import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 와 이거 미쳤네..

# 이 문제의 핵심은 가운데 글자를 반환하는 문제다.
# 우선 글자의 개수가 짝수냐 홀수냐에 따라 출력하는 방식이 다르다
# 홀수일 경우 가운데 글자를 그대로 반환하면 되지만 짝수일 경우 앞쪽글자까지 같이 가지고 와야한다.

# 이 예제 같은 경우 2:3까지 출력을 요구하기 때문에 슬라이스의 마지막 3-1 만큼만 출력하게 되므로
# 사실상 짝 홀 나눌 필요는 없게 된다.

# 짝수일경우
# str = "abcde"

# 1부터 출력을 요구하고 있고, 3까지 출력을 요구하고 있기 때문에
# 1-2까지 출력을 하는걸 볼 수 있다.
str = "qwer"
a = str[(len(str)-1)//2 : len(str)//2 + 1]

