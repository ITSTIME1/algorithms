# pre-order 탐색방법을 살펴보자

# 루트노드를 먼저 방문
# 그다음 left 방문
# 마지막으로 right 방문

# 아까 in-order 방식에서는
# 왼쪽 - root - 오른쪽
# 순서대로 방문했었는데 이번엔
# 루트노드부터 방문한다
# 루트방문후에 왼쪽 오른쪽을 순차대로 방문하게 된다.

from queue import Queue

queue = Queue()

class Node:
	def __init__(self, val):
		self.leftChild = None
		self.rightChild = None
		self.data = val

	def insert(self, data):
		if data is None:
			return

		if self.leftChild is None:
			self.leftChild = Node(data)
			data = None
		elif self.rightChild is None:
			self.rightChild = Node(data)
			data = None
		else:
			queue.put(self.leftChild)
			queue.put(self.rightChild)


	# preorder traversal function
	# 전위순회
	def preorderTraversal(self, root):
		ret = []
		if root:
			ret.append(root.data)
			ret = ret + self.preorderTraversal(root.leftChild)
			ret = ret + self.preorderTraversal(root.rightChild)
		return ret	
	# 먼저 root data 부터 넣어주고
	# 그 루트 데이터를 넣고나서
	# 그다음 왼쪽을 넣어주고, 그다음 오른쪽을 넣어준다
	# 한번 이해해보니까 그렇게 어려운 로직은 아닌거 같다.

	# 위에 insert 하는 방식만 이해한다면 아래 재귀 형태는 이해가 간다.
