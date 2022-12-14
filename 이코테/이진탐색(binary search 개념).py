# 이진 탐색 소스코드 구현 (재귀함수)

def binary_search(array, target, start, end):
	if start > end :
		return None

	mid = (start + end) // 2

	if array[mid] == target:
		return mid

	# 찾고자 하는 값이 중간값 보다 작은 경우
	# 끝 점을 mid 이전 으로 옮긴다
	# 만약 mid 가 4라면 3으로 옮겨준다.
	elif target < array[mid]:
		return binary_search(array, target, start, mid - 1)

	else:
		return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
	print("원소가 존재하지 않습니다")
else:
	print(result+1)