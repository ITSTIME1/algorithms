import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))



def three():
	index = len(card)-1
	for i in range(len(card)-1, -1, -1):
		if card[i] == 0:
			index = i
			break
	return index


def two():
	index = 1
	for i in range(1, len(card)):
		if card[i] == 0:
			index = i
			break
	return index


def one():
	index = 0
	for i in range(len(card)):
		if card[i] == 0:
			index = i
			break
	return index


# 1, 2, 3

# 아 10^6제곱;;
# 그럼 이걸 거진 n^2으론 풀기 힘들다는건데
# 그럼 이걸 어떻게풀지..
card = deque([0]) * n
number = [i for i in range(1, n+1)]
for i in range(len(arr)):
	n = number.pop()
	# 마지막을 찾아서
	if arr[i] == 3:
		ans = three()
		card[ans] = n
		continue
	elif arr[i] == 2:
		ans = two()
		card[ans] = n
		continue
	else:
		ans = one()
		card[ans] = n


print(*card)
