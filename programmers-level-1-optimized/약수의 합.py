import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 정수 n을 받아 n의 약수를 모두 더한 값을 리턴하는 예제

# 최적화 아이디어는 약수의 개념을 이용한 아이디어 중 하나로



# 1. list comprehension을 이용한 방법.
# n 까지의 값들을 n으로 나눠 나머지가 0 이 된다면 약수이므로 리스트의 담은 다음 sum()함수를 이용해서
# 합을 구한 것 까지는 동일함.
answer = sum([i for i in range(1, n+1) if n % i == 0])

# 2. n의 절반까지만 구한뒤 마지막 n의 값만 더해주면 n의 약수를 모두 더한 값이 된다.
# n의절반이 넘어가게 되면 나머지가 0 이되는 i가 존재하지 않기 때문.
# 만약 30 이라면 15까지만
# 1, 2, 3, 5, 10, 15

# 만약 12 라면 6까지만 진행한다면
# 1, 2, 3, 4, 6(7,8,9,10,11) 까지는 약수가 존재 하지 않는다
# 따라서 마지막 n값만 더해준다면 약수의 합이 되는 것.
# 만약 문제에 따라서 n의 약수를 모두 구하라 라고 한다면.
# n//2 까지 구한 뒤 n만 추가시켜주어 개수를 세면 된다.
answer = n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
