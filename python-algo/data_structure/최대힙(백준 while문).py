

import sys


def parent_swap(last_value):
	# 부모 노드와 자식 노드 간의 swap 을 이루어야 가장 큰 노드가 가장 위로 올라 갈 수 있음.
	heap[last_value], heap[last_value//2] = heap[last_value//2], heap[last_value]

def basic_swap(first, last):
	heap[first], heap[last] = heap[last], heap[first]

def heappush(heap, value):
	heap.append(value)
	# heap 에 추가 했던 마지막 value 값의 index를 가지고 온다.
	last_value = len(heap)-1
	# 부모노드를 다 탐색할때 까지 while문을 반복한다
	while last_value > 1:
		# 자식노드가 부모노드보다 더 크다면 swapping 한다
		# swap()
		if heap[last_value] > heap[last_value//2]:
			parent_swap(last_value)
			# 부모 노드의 인덱스로 바꿔준다
			last_value //= 2
		else:
			break


def check_priority(priority):
	if priority < len(heap)-1 and heap[priority] < heap[priority + 1]:
		return priority + 1
	else:
		return priority


# maxheapify 를 구현한건데 뭔가 내가 원하는 코드는 아님.
# 내일 한번 차이점을 찾아보자
# 분명 예제가 잘 못 나오는데에는 이유가 있다.

# 힙을 만족하지 않았기 때문이겠지
# 1. 리프노드의 문제라고 생각이 들긴하는데
# 2. 만약 리프노드의 문제가 아니라면
# 3 .무엇이 문제일까

def maxHeapify(index):
	child = 2
	parent = index

	while child <= len(heap)-1:
		get_priority = check_priority(child)
		if heap[get_priority] > heap[parent]:
			basic_swap(parent, get_priority)
			parent = get_priority
			child = get_priority * 2
		else:
			break


def heapdelete(heap):
	if len(heap) == 1:
		return 0
	#[0, 2, 1]
	basic_swap(1, len(heap)-1)
	# maxVal을 뽑아주고
	maxVal = heap.pop()
	maxHeapify(1)
	return maxVal

# 1. 0이면 출력
# 2. 0이 아니면 배열의 추가하는 건데
# 3. 배열의 추가할 때 중요한건 최대힙을 구한다고 한다면
# 4. 부모노드의 값을 계속 찾아 올라가면서
# 5. parent < child 상태라면 지속적으로 바꾸어 주어야 한다는 것이다.
# 6. 그렇게 된다면 가장 최상위 부모 노드엔 가장 큰 값이 올라가져 있을것이므로 index // 2 = parent


n = int(sys.stdin.readline().strip())
heap=[0]
for _ in range(n):
	value = int(sys.stdin.readline().strip())
	if value != 0:
		heappush(heap, value)
	else:
		if len(heap) == 1:
			print(0)
		else:
			print(heapdelete(heap))

