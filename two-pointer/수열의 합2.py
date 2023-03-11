import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m = map(int, input().split())

arr = list(map(int, input().strip().split(" ")))

end = 0
total = 0
ans = 0
for i in range(len(arr)):

	while total < m and end < n:
		total += arr[end]
		end += 1

	# 만약 그 구간 배열의 합이 원하는 값보다 크거나 같아졌을때
	# start 값을 앞으로 떙겨야하니까
	# 일단 여기서는 카운트를 체크하라고 했으니
	if total == m:
		ans += 1 

	# 그럼 i 는 for문에 의해서 증가될거고
	# 부분합의 값은 첫번째를 제외한 값으로 줄어들것이다.
	# 왜 i 값은 증가했기 때문에
	total -= arr[i]


# 이게 포인터의 기초
print(ans)