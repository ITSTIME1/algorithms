import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# s라는 문자열이 주어졌을때
# 그 s라는 문자열이 숫자로만 이루어져 있는지 확인하는 코드를 작성해라

# a234 는 숫자로만 구성되어져 있지 않다.
# a때문에
# 하지만 1234 라는 문자열은 숫자로만 구성되어져 있기 때문에 True를 리턴한다.

# 이걸 확인하는 방법은 isdigit()함수를 활용해서 숫자인지 아닌지를 확인하는 방법이다.
# 그럼 문자열 자체가 숫자로만 구성되어져 있다면 True를 그렇지 않다면 False 를 리턴할것이다.

s = "a234"


# 숫자로 구성되어져 있으면서 길이가 4,6또는 6에 해당된다면 해당 숫자로만 구성 되어져 있다고 판단한다.
if s.isdigit() and len(s) in [4, 6]:
	return True
else:
	return False

