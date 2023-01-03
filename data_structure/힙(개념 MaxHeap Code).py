# 힙 정렬 문제라고 한다


# 힙은 무엇일까?

# 힙(heap) = 힙은 트리 구조를 기반으로 한 데이터 자료구조이다.
# 완전 이진 트리를 기본으로하는 자료 구조.

# 일단 힙을 좀 알아보자면
# 어떤 노드 c가 주어졌을 때 c의 부모노드가 p라고 한다면
# 부모의 키 값(value)이 자식 노드인 c보다 크거나 같다면 = max heap 이라고 부른다
# 부모의 키 값(value)이 자식 노드인 c보다 작거나 같다면 = min heap 이라고 부른다

# 여기서 부모 노드는 (top node) 라고 해서 root node 라고 불린다

# 이 힙 자료구조는 priority queue 라는 우선순위 알고리즘에서 필수적으로 최대 효율을 낸다
# 힙 에서 가장 큰 값 또는 가장 작은 값은 항상 root 에 저장되어 진다
# 배열로 따지자면 가장 앞?

# 그래서 이 힙 자료구조는 가장 큰 값또는 가장 작은 값을 우선적으로 지워야 할 때 유용한 자료구조가 된다

# 원소 값의 대소 관계는 오로지 부모 노드와 자식 노드 간에만 성립하며 형제 사이에는 대소관계가 정해지지 않는다
# 힙의 시간 복잡도는 삽입, 삭제 모두다 O(logN) 이다
# 시간 복잡도가 저렇게 나오는 이유는 전체 원소의 반만큼의 값과 비교하기 대문에 그렇다


# 0을 포함한 Heap

class MaxHeap(object):
	def __init__(self):
		self.queue = []
	# 삽입 하는 함수
	def insert(self, n):
		self.queue.append(n)
		# last_index = 큐 자료구조형의 마지막 index를 의미한다
		last_index = len(self.queue) - 1
		# 그 마지막 인덱스가 0보다 크거나 같을때 까지 반복한다
		while 0 <= last_index:
			# 부모 인덱스는 last_index
			parent_index = self.parent(last_index)
			if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
				self.swap(last_index, parent_index)
				last_index = parent_index
			else:
				break
	# 삭제 함수
	# [11, 6, 3, 1]
	# [1,6,3,11]
	def delete(self):
		last_index = len(self.queue) - 1
		if last_index < 0:
			return -1
		self.swap(0, last_index)
		# [11]
		maxv = self.queue.pop()
		# pop() 한 후 재정렬
		self.maxHeapify(0)
		print(maxv)
		return maxv

	def maxHeapify(self, i):
		# i = 0
		# leftchild = 1
		# rightchild = 2
		# max_index = 0
		# 좌, 우의 자식노드들을 찾아준다.
		left_index = self.leftchild(i)
		right_index = self.rightchild(i)
		max_index = i
		# [1, 6, 3]
		if left_index <= len(self.queue) - 1 and self.queue[max_index] < self.queue[left_index]:
			max_index = left_index
		if right_index <= len(self.queue) -1 and self.queue[max_index] < self.queue[right_index]:
			max_index = right_index
		# max_index = 1
		# i = 0
		if max_index != i:
			# [6, 1, 3]
			# 재정렬을 시키는거구나
			# 그럼 언젠간 max_index == i 가 될때가 오니까
			# 그때가 정렬이 다된 순간일거고
			self.swap(i, max_index)
			self.maxHeapify(max_index)


	def leftchild(self, index):
		return index*2 + 1

	def rightchild(self, index):
		return index*2 + 2

	def swap(self, last_index, parent_index):
		self.queue[last_index], self.queue[parent_index] = self.queue[parent_index], self.queue[last_index]
	
	def parent(self, last_index):
		return (last_index-1) // 2

# parent_index = 0
# last_index = 0

# heap = [1]
# 1<1 False

# 3
# heap = [1, 3]
# last_index = 1
# parent_index = (1-1) // 2 = 0
# queue[0] == 1
# parent_index = 0>=0
# queue[1] == 3 
# 1< 3 True
# swap()
# queue[1], queue[0] = queue[0], queue[1]

# heap = [3, 1]


# 11
# heap = [3, 1, 11]
# last_index = 2
# parent_index = 2-1 // 2 0

# queue[0] = 3 < que[2]
# 11, 3 = 3, 11
# queue[2], queue[0] = queue[0], queue[2]

# heap = [11, 1, 3]


# 6
# heap [11,1,3,6]
# last_index = 3
# parent_index = 2 // 2 = 1

# [11,6,3,1]
# queue[3], queue[1] = queue[1], queue[3]

