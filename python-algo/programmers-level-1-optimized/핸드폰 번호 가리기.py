import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이 문제는 핸드폰 번호가 문자열로 주어졌을때 뒤 4자리를 제외한 나머지를 전부*표시 하는것.

# 문자열의 곱셈을 이용한 풀이로 문자열의 길이 - 4자리를 빼면
# 뒤 4자리를 제외한 나머지 부분들이 나온다
# 그 나머지 부분들을 전부 * 만들면 되는 것이기 때문에
# 그 만큼의 문자열을 * 을 만들어주고 그 뒤 네자리 부분은 따로 s문자열에서 슬라이싱을 통해서 가지고 올 수 있다.
# for문을 활용할 필요도 없다.
s = "027778888"
answer = "*" * (len(s)-4) + s[-4:]
print(answer)