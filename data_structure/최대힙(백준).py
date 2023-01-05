

import sys


def push_swap(last_value):
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
			push_swap(last_value)
			# 부모 노드의 인덱스로 바꿔준다
			last_value //= 2
		else:
			break

def maxHeapify(prioirity, parent, last_value):
	while prioirity < last_value:
		if prioirity < last_value and heap[prioirity] > heap[parent]:
			basic_swap(parent, prioirity)
			parent = prioirity
			# index error shit
			# ==> 여기서부터 고쳐야됨...
		if prioirity < last_value and heap[prioirity+1] > heap[parent]:
			basic_swap(parent, prioirity+1)
			parent = prioirity + 1
			
		prioirity *= 2


def heapdelete(heap):
	# [0, 3, 2, 1]
	last_value = len(heap)-1
	prioirity, parent = 2, 1
	basic_swap(1, last_value)
	# [0, 1, 2, 3]
	popped = heap.pop()
	# [0, 1, 2]
	maxHeapify(prioirity, parent, last_value)

	return popped


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

