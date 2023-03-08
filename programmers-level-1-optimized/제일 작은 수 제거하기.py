import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [10]

# 이 문제는 제일 작은 수를 제거하고 그 배열을 리턴하면 되기 때문에
# 해당 배열에서 가장 작은 수를 찾을 min함수를 사용해볼것이고
# 그 수의 index 를 찾아 del 함수를 사용해 제거한 뒤 그 배열이 0이라면 -1을 채워서 리턴할것이고
# 만약 그렇지 않다면 수를 제거한 배열 그대로를 리턴할것이다.
del arr[arr.index(min(arr))]

if arr:
	print(arr)
else:
	arr.append(-1)
	print(arr)