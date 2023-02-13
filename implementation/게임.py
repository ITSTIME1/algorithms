# 수학문제?
import sys
import heapq
import math
import fractions
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline


# 같은 숫자가 나온다면 x == y 가 나온다면 아무리 이겨도 절대 변하지 않는다
# 10억의 데이터가 들어올때ㅑ

# 우선 처음 기준으로 승률을 저장해두고
# 처음 승률과 다를때까지 x+1, y+1 해주고 나눠준다
# 이때 처음 승률과 같다면 중단하고 cnt 를 출력
# 그럼 10억의 데이터가 들어오는데 1923만번의 연산을 하게 된다면?
# 2초라 1억 = 1초 2억 = 2초s
# 10억이 들어오면 최선의 경우도 한번에 끝나는건데
# 최악의 경우 10억 만큼의 연산도 해야되기 때문에
# dp 아닐까


# 10억의 데이터면 줄여야하는데
# 10억을 log 로 따지면
# log10억 = 약 29초




x, y = map(int, input().split())

if x == y:
	print(-1)
	exit()