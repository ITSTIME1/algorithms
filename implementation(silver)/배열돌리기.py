import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m, r = map(int, input().split())

arr = [list(map(int, input().strip().split())) for _ in range(n)]


# 총 r번을 반복할거고
for i in range(r):

	# 한번 반복시키고
	# 그 다음 내부반복문도 똑같이 반복시키고
	# 오늘 배운것 중 하나는 행렬의 둘 중의 작은 값의 // 2한다면
	# 행렬의 가장 처음값을 선택할 수 있다는 것이다.
	# 그걸 이용해서 문제를 풀어보낟면
	# 첫번째 예시는 4by4행렬이므로 4 // 2 = 2 따랏 0, 1을 선택한다면

	# 외부반복문과 내부반복문 두개를 선택할 수 있다
	# 따라서 한번씩 돌려주면 될거같다
	for j in range(min(n, m) // 2):
		# 초기 값을 생성해주고
		x, y = j, j

		# 왼쪽부터 시작할건데
		# x의 값이 증가하는형태 y는 변하지 않고
		tmp = arr[x][y]
		# 1, 2
		# 1
		for k in range(j+1, n-j):
			x = k
			pre = arr[x][y]
			arr[x][y] = tmp
			tmp = pre


		# x의 값은 변하지 않지만 y의 값은 변하는형태야.
		# 열의 길이 만큼 증가해야하니까
		# 여기서 x값을 고정시켜줘야하는데
		# x는 3이 들어가있을거고 y는 새로시작하면되니까
		for k in range(j+1, m-j):
			y = k
			pre = arr[x][y]
			arr[x][y] = tmp
			tmp = pre

		# x의 값은 감소하고 y의 값은 변하지 않는형태
		# 1, 2
		for k in range(j+1, n-j):
			# 1, 2, 3
			x = n-k-1
			pre = arr[x][y]
			arr[x][y] = tmp
			tmp = pre

		# 마지막은 반대로 도니까
		# x의 값은 그대로지만 y의 값은 감소하는 형태
		for k in range(j+1, m-j):
			# 1, 2, 3
			# 0, 2, 0, 1 0, 0
			y = m-k-1
			pre = arr[x][y]
			arr[x][y] = tmp
			tmp = pre

print(arr)

# 3 14 15 16
# [[3, 4, 8, 12], 
# [2, 11, 10, 16], 
# [1, 7, 6, 15], 
# [5, 9, 13, 14]]

# 인덱스 계산이 쉽지가 않네
# 뭔가 내꺼가 내껀가 아닌느낌 인덱스 계산을 좀 더 많이 해봐야 할 것 같에



