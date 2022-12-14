# 이진 탐색은 리스트 내부의 데이터가
# 정렬이 되어 있는 상태에서 사용할 수 있다
# 이미 정렬되어 있다면 빠르게 데이터를 찾을 수 있고
# 이진 탐색은 탐색 범위를 절반씩 줄여가면서 찾는 알고리즘이다
# 이진 탐색은 위치를 나타내는 변수 3개를 받는데
# start 처음값, mid 중간값, end 끝값
# start 는 index[0] 값 이고 end len(arr)-1 값이 끝점이된다
# mid = (start + mid) // 2 나눈 몫 값이 mid 값이 되며
# 이 mid 값이 배열의 길이가 짝수가 아닐 경우 홀 수라면
# // 2 해준 것처럼 나머지 뒤에 있는 소수점은 버리게 된다
# 처음 시작 한 값과 끝 값을 확인하고 mid 값을 설정해 준다음
# 찾으려는 target 숫자가 중간점보다 작다면
# mid 이후의 값에는 target 값이 존재하지 않기 때문에
# end 값을 바꿔준다 mid 의 이전 값으로 바꿔준다면
# 만약 mid = 4 라면 mid 의 내부에서만 찾으면 되기 때문에
# 4 보다 낮은 즉 mid - 1 번째로 바꾸어서 찾아주게 된다
# 만약 4보다 큰 경우라면 end 값은 그대로 두고 start 값dmf
# mid + 1 값을 하게 된다면 mid 다음 인덱스 부터 시작해서 끝 값까지 찾을 수 있게 된다.

# 이런 식으로 찾게되어 array[mid] == target 값이 되었다면
# mid 값을 반환해준다.

# 이진 탐색은 O(logN) 의 시간 복잡도를 가지게 된다.
# 이진 탐색의 탐색 방법을 보면 탐색의 범위가 절반씩 줄어들게 되는 걸 볼 수 있는데
# 이렇게 최적의 시나리오대로 절반씩 줄여나가기에 연산 횟수는 log2N에 비례한다고 할 수 있다
# 이진 탐색을 구현 하는 방법은 재귀적으로 호출하는 방법과
# 반복문을 활용해서 구현하는 방법이 있다.

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
start = 0
end = length - 1

while start <= end:
	mid = (start+end) // 2
	if m_list[mid] == target:
		return mid
		break
	elif m_list[mid] > target:
		end = mid - 1
	else:
		start = mid + 1