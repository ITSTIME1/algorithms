

import sys


def push_swap(last_value):
	heap[last_value], heap[last_value//2] = heap[last_value//2], heap[last_value]

def delete_swap(first, last):
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

# 먼저 루트 노드의 값을 반환한다음에
# 다시 한번 재정렬이 이루어져야 하므로
# 말단 노드가 루트 노드에 와있기 때문에
# 만약 최대힙이라면
# 자식 노드들 중 현재 나보다 큰 값이 있으면 swap 해주어야 한다.
def maxHeapify(heap, i):
	# left value and right value
	heap_n = len(heap)-1
	# 1
	left_value = i*2
	# 2
	right_value = (i*2)+1 
	# 3
	largest = i
	# 1
	if left_value <= heap_n and heap[left_value] > heap[largest]:
		largest = left_value
	else:
		largest = i

	if right_value <= heap_n and heap[right_value] > heap[largest]:
		largest = right_value

	if largest != i:
		delete_swap(largest, i)
		maxHeapify(heap, largest)


def heapremove(heap): 
	# [0, 2, 1]
	# [0, 1]
	last_index = len(heap)-1
	# 루트노드와 바꿔주고
	delete_swap(1, last_index)
	# 그럼 바꾼 가장 말단 노드가
	# 최상단 노드(max or min)
	popped = heap.pop()
	# [0, 1]
	# heapify = 힙의 성질을 맞추기 위해서 트리를 재정렬
	# [0, 1] 에서 바꿔버리기 때문.
	# 여기서 시간초과 난다
	for i in range(len(heap)//2, 0, -1):
		maxHeapify(heap, i)
	return popped


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
			print(heapremove(heap))

