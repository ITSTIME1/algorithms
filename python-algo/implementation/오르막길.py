# 오르막길은 항상 숫자가 증가해야 하고
# 적어도 2개 이상이니까
# 3 4 5 이런식으로 이상이어도 오르막길이라고 한다.

import sys
N = int(input())
arr = list(map(int, input().split()))
min_index = 0

tmp = []
result = []
	
for i in range(len(arr)):
	if len(result) == 0:
		result.append(arr[i])
	else:
		# 마지막 가지고 온 값이
		# 지금 가지고 온 값보다 작다면
		# 즉 지금 현재 가지고 온 값이 더 크다면
		if result[-1] < arr[i]:
			result.append(arr[i])
		# 만약 마지막 가지고 온 값이 현재 가지고 온 값보다 크다면
		# 추가 하지 않고 tmp 에 값을 저장해둔 다음
		# 배열을 초기화하고 
		elif result[-1] >= arr[i]:
			tmp.append(max(result) - min(result))
			result.clear()
			result.append(arr[i])

tmp.append(max(result) - min(result))
print(max(tmp))
