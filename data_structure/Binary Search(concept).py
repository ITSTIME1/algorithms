# 바이너리 서치는 = 이분탐색

# 우선 이분 탐색은 적은 n 즉 배열의 값이 작은 경우
# 선형 배열 보다 빠르게 동작한다
# 최악의 경우O(log n)의 시간 복잡도를 가진다

# 바이너리 서치를 적용하려면 무조건 처음에
# '정렬이 되어져 있는 상태' 이어야 한다는것이다

# 해쉬 테이블 은 이진 검색보다 더 효율적으로 탐색이 가능하지만
# 이분 탐색또한 넓은 범위에서 문제를 해결할 때 사용될 수 있다

# 그래서 이분탐색을 어떻게 하느냐



## [ Recursive ]

# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")


# 재귀 바이너리 서치를 요약설명 해보자면

# 우선 찾고자 하는 x 의 값이 어디있는지를 확인하는게 우선이다
# 이분 탐색 이기 때문에 정확히 len(arr) // 2 를 한 index 값과 compare 하여
# x 가 배열의 중간값보다 '값으로 따졌을때' 작다면 left half array 만 탐색하면 되기 때문에
# 오른쪽은 재귀를 또 다시 돌리지 않고 왼쪽만 돌리게 된다
# 해서 low 와 high 값을 low 는 배열의 첫값
# high 는 mid-1 값을 기준으로 다시 한번 탐색한다음에 
# 만약 배열의 mid 값이 해당 값이 될 경우에 mid = index 값을 리턴해준다
# 만약 low와 high 값이 high 값이 low 보다 작거나 같다면
# 그 값은 해당 배열에 없는 것이기 때문에 -1 을 리턴한다

# 이렇게 해당 값을 찾아나간다 18값은 1초안에 해결이 가능하다


## [ Iterative ]

# Returns index of x in arr if present, else -1
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")


# 뭔가가 이상한데...
# 인덱스가 마지막까지 남으면 항상 index = 0을 가르키는데
# index = 0 값도 찾는 값이 아닐경우 해당 값을 비교해서
# 오케이 이해됐으
