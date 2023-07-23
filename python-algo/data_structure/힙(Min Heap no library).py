# 최소힙

# 최소힙 문제 기준
import sys
def insert(heap, num):
	heap.append(num)
	last_index = len(heap)-1

	while last_index > 1:
		if heap[last_index] < heap[last_index//2]:
			heap[last_index], heap[last_index//2] = heap[last_index//2], heap[last_index]
			last_index //= 2
		else:
			break


def delete(heap):
	# 가장 작은 값이 heap[1] 째에 있을거니까
	minVal = heap[1]
	tmp = heap.pop()

	parent = 1
	child = 2
	while child <= len(heap)-1:
		if child < len(heap)-1 and heap[child] > heap[child+1]:
			child += 1
		if heap[child] >= tmp:
			break

		heap[parent] = heap[child]
		parent = child
		child *= 2

	if len(heap)!=1:
		heap[parent] = tmp
	return minVal

n = int(sys.stdin.readline().strip())
heap = [0]
for _ in range(n):
	x = int(sys.stdin.readline().strip())
	if x != 0:
		insert(heap, x)
	else:
		if len(heap) == 1:
			print(0)
		else:
			print(delete(heap))