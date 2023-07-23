import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	# 가장 작은 값부터 하나씩 가지고 와서
	# 가장 큰 값이 가운데에 오도록 만들 수 있다.
	arr.sort()
	ch = [0] * len(arr)
	
	l, r = 0, len(ch)-1
	for j in range(len(arr)):
		if j % 2 == 0 and ch[l] == 0:
			ch[l] = arr[j]
			l+=1
		elif j % 2 == 1 and ch[r] == 0:
			ch[r] = arr[j]
			r-=1
	# 난이도는 각 통나무들간의 높이의 차의 최댓값
	# 5-9가 선택된것처럼
	# 그럼 가운데 가장 큰 값을 기준으로
	# 양옆으로 작아지면서
	# 각 통나무들간의 차이를 계산해 가장 큰 값을 리턴하면 그게 답.
	# 독해력 ;;
	a = 0
	for i in range(len(ch)):
		a = max(a, abs(ch[i]-ch[i-1]))
	print(a)

	# 그럼 여기까지 각 통나무들의 높이차를 최소로만들고
	# 높이차이는 차이가 별로 안나게 하면 되는거임
	# 만약 옆의 높이 1 그 옆에 높이가 2 면 최소가 되지만
	# 1 3이면 2로 최소가 되지 않음
	# 따라서 2, 4, 5, 7, 9 라고 하면
	# 2 5 9 7 4
# 아 문제에서 각 인접한 통나무의 높이차가 최소가 되게 한다고 한다
