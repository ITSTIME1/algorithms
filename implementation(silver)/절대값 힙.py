# 문제 분석

import sys
import heapq
from collections import deque
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
# 배열에 정수를 넣는데 x = 0 이면 안된다는데 그럼 양의정수 와 음의정수가 들어간다는거고

# 배열에서 절대값이 가장작은값 그 값을 찾고 제거한다
# 아이디어가 뭘까


# heap을 튜플로 구성했을시
# 앞에 있는 첫 숫자를 가지고 정렬하므로
# 힙을 구성했을때 앞의 있는 첫 숫자를 가지고 정렬을 한다라는걸 기억하면 좋을거 같다.
n = int(input())


stack = []
for i in range(n):
	# 빼는 연산
	num = int(input())
	if num == 0:
		if len(stack) == 0:
			print(0)
		else:
			a = heapq.heappop(stack)
			print(a[1])
	else:
		heapq.heappush(stack, (abs(num), num))