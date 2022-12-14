import sys


# 떡볶이 개수, 원하는 떡볶이 길이
N, M = map(int, sys.stdin.readline().rstrip().split())


# 각 떡볶이 길이 = 높이
array = list(map(int, sys.stdin.readline().rstrip().split()))


start = 0
end = max(array)



return_mid = 0
while start <= end:
	mid = ( start + end ) // 2
	result = 0	
	for i in array:
	# 그 높이를 설정한 값보다 크다면
	# 떡이 잘릴 수 있으므로
		if i > mid:
			result += i - mid

	if result < M:
		end = mid - 1

	else:
		return_mid = mid
		start = mid + 1


print(return_mid)
