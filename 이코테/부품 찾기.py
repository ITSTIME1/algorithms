import sys

# 부품의 N 개가 있고
N = int(sys.stdin.readline())
# 각각의 부품의 번호는 이렇다
array = list(map(int, sys.stdin.readline().split()))
array.sort()
M = int(sys.stdin.readline())
find_array = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(array) - 1


def binary_search(array, target, start, end):

	result_min = 0
	while start <= end:
		mid = (start+end) // 2

		if array[mid] == target:
			return mid
		elif target < array[mid]:
			end = mid - 1
		elif target > array[mid]:
			start = mid + 1

	if array[mid] != target:
		return result_min


for i in find_array:
	result = binary_search(array, i, start, end)

	if result == 0:
		print("no", end = " ")
	else:
		print("yes", end = " ")

