# 문제분석 

# 힙 자료구조를 이용해서 푸는 문제이다
# 완전 이진 트리를 기반으로 한 데이터 자료구조 이다
# 힙은 트리 기반의 데이터 자료 구조이고
# 힙에는 최대힙과 최소힙을 구하는 방법이 있고

# 힙은 우선순위 큐라고도 불리는데 종종 힙이라고 지칭된다

# 보통 우선순위 큐를 구한다고 한다.
# 거기에서 최대값을 구할지 최소값을 구할지가 다르다

import heapq
import sys

# MaxHeap
# mac test?
# 1. heap insert
def insert(heap, num):
	# heap list 에 마지막 값을 넣어주고
	heap.append(num)
	# 마지막 값의 index 값을 변수에 담아주고
	i = len(heap)-1
	while i > 1:
		# 마지막 인덱스 값이 더 크다면 부모노드를 찾아 올라갔을때
		if heap[i] > heap[i//2]:
			# 부모노드 가 더 작은 값이라면 바꿔주고
			# 계속 찾아 올라갈 i의 값은 인덱스의 값이기 때문에 계속 올라간다
			heap[i], heap[i//2] = heap[i//2], heap[i]
			i //= 2
		else:
			# 만약 부모 노드가 더 크다면 swap 하는걸 멈추고
			break

# 2. heap delete
# step by step
# 1). Replace root node with last-value
# 2). After change root node and last-value, Delete previous root node.
# 3). need to know left child and right child and then what is the larger than root node. 
# 4). if left child larger than root node, have to change position(index) each other.
# 5). if right child larger than root node, have to change position(index) each other.

def delete(heap):
	# root node
	maxVal = heap[1]
	tmp = heap.pop()

	parent = 1
	child = 2

	# 자식 노드들의 개수 까지 반복하고
	while child <= len(heap)-1:
		
		if child < len(heap)-1 and heap[child] < heap[child+1]:
			child += 1
		if heap[child] <= tmp:
			break

		heap[parent] = heap[child]

		parent = child
		child *= 2
	if len(heap) != 1:
		heap[parent] = tmp
	return maxVal

# x 가 자연수라면
# 추가하는 연산
# 0 이라는 값을 준다면 출력
# 음의 정수는 나오지 않는다
n = int(sys.stdin.readline().strip())
heap = [0]
for _ in range(n):
	x = int(sys.stdin.readline().strip())
	if x != 0:
		insert(heap, x)
	else:
		# // 왜 0 이 아니고 1이지 
		if len(heap) == 1:
			print(0)
		else:
			print(delete(heap))