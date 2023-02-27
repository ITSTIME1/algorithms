import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


a = 3
b = 1
n = 20

ar = []

보유중인 n병
빈병a개
콜라1개
20-18+6
xa xa= 8 <= total

# 보유중인 병이 바꿀 빈병의 개수보다 작게 된다면
# 바꿀 수 없지
# 때문에 a까지만 바꿀 수 있으니 a까지만 반복을하고
while n >= a:
	re = n % a
	# 이게 바꿀 수 있는 콜라의 개수 식
	n = (n//a) * b
	answer += n
	n += re
