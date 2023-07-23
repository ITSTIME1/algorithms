import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# a = deque([1, 2, 3, 4, 5, 6, 7])

# # 3, 4, 5, 6, 7, 1, 2
# # 무슨 규칙이 존재하지
# k = 3
# b = -2
# a.rotate(b)
# print(a)

# -2 -> k로 바꿔야돼

# 시계방향으로 바뀔때만
# 음?
# 그러면 
# 반시계방향일때는 -(k-1)
# 시계방향일때는 k
n, k, m = map(int, input().split())

reverse = -(k-1)

arr = deque(_ for _ in range(1, n+1))

answer, stand, check_state = [], m, -1

while len(arr) > 1:
	# 인원수가 0이냐 0이 아니냐에 따라
	# 상태가변경이되고 안되고
	if stand == 0:
		if check_state == -1:
			check_state = 1
		else:
			check_state = -1
		stand = m
	else:
		if check_state == 1:
			arr.rotate(k)
		else:
			arr.rotate(reverse)

		a = arr.popleft()
		answer.append(a)
		stand -=1 

answer.append(arr[0])
# 출력방식이 더 오래걸림
# 12ms 차이남.
# print("\n".join([str(i) for i in answer]))
for i in answer:
	print(i, end = "\n")
