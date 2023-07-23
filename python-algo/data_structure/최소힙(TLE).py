# 문제분석

# 최소힙이라는 문제인데
# 자연수 x를 배열에 넣고
# 자연수를 넣고 난 후의 배열에서 가장 작은 값을 출력하고
# 그 값을 배열에서 제거한다고 한다
# deque?

import sys
from collections import deque


n = int(sys.stdin.readline().strip())

# x 가자 양의 정수라면 배열에 넣어주고 음의정수는 입력으로 주어지지 않는다고 했기 때문이다
# x = 0 이라면 배열에서 가장 작은 값을 출력한다
# TLE
arr = []

for _ in range(n):
	x = int(sys.stdin.readline().strip())
	if x != 0:
		arr.append(x)
	else:
		# 가장 작은 값을 출력할려면 정렬된 배열을 deque 로 바꾸는게 편할거 같은데?
		arr.sort()
		deque_list = deque(arr)
		if len(deque_list) == 0:
			print(0)
		else:
			# 가장 작은 값을 c 변수에 담아주고
			# 해당 deque 값을 리스트에 다시 업데이트 해주기 위해서
			# 리스트로 다시 변환 후 arr에 업데이트 해준다
			# 이렇게 되면 항상 작은 값을 뺄 수 있게 된다
			c = deque_list.popleft()
			arr = list(deque_list)
			print(c)
