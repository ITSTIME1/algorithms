import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, k = map(int, input().split())


if n < k:
	print(-1)
	exit()

arr = deque([1] * n)

# 물을 합칠 수 있으면 끝까지 합쳐
# 만약 정말 합칠수 없다면
# 끝까지 왔는ㄷ ㅔ합칡 ㅔ없으면 하나가져와
[8,4,1,1] cnt += 1
[8,4,2,1] cnt += 2
[8,8] cnt += 3


[1,1,1,1,1,1,1,1,1,1,1,1,1]

# 합칠 수 있는건 전부 합치고
# 합칠 수 없을때 하나를 가져와
# 합치는건
# 앞에서부터 자기랑 같은 번호가 있으면 그거랑 합쳐

index = 0
while len(arr) != k:

	if index == len(arr)-1:


	total = 0
	if arr[index] == arr[index+1]:
		total += arr[index] + arr[index+1]
		for i in range(2):
			arr.popleft()
		arr.insert(index, total)
	else:
		index += 1






# print(cnt)