import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 수학으로 푸는 방법이 있는데 0~9까지의 수기 때문에
# 0~9의 수들의 합은
# 0+1+2+3+4+5+6+7+8+9
# 9가 총 5개 9*5= 45
# 만약 이 총 합에서 - 현재 주어진 수들의 합을 빼면 없는 숫자들의 합을 알 수 있다.
# 천재네..

numbers = [1,2,3,4,5,6,7,8,0]
print(45-sum(numbers))