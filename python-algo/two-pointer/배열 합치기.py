import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split(" "))

# 정렬되어 있는 두 배열을 합친다..
# 두 배열을 합치는거면 그냥 두 배열을 합쳐주고 정렬시키면되지 않을까?

a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))



l, r = 0, 0
result = []
# while l < n and r < m:
#     if a[l] < b[r]:
#         result.append(a[l])
#         l += 1
#     else:
#         result.append(b[r])
#         r += 1

# # 2,1
# # 위 과정까지는 [2, 3, 5] 까지 리스트의 추가가 되어지고
# # 마지막에 l의 지점을 올려놨기 때문에
# # r의 지점을 하나더 올려주기 위해 그 지점의 있는 수를 더해준다면 된다


# # 음 투포인터라는걸 좀 생각을 해야되는 문제구나.
# while l < n:
#     result.append(a[l])
#     l += 1

# while r < m:
#     result.append(b[r])
# 	r += 1
while l < n and r < m:
	if a[l] < b[r]:
		result.append(a[l])
		l+=1
	else:
		result.append(b[r])
		r+=1






