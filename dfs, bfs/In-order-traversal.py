# in-order-traversal
# 중위순회라고도 하는데
# 왼쪽서브트리 - 루트 - 오른쪽 서브트리 처럼 되는 형태 
# 만약 왼쪽 서브트리의 왼쪽 서브트리가 탐색할게 없다면 오른쪽 서브트리를 탐색
# 루트에서 왼쪽 서브트리가 더 이상 탐색할 트리가 존재하지 않을경우
# 오른쪽 서브트리로 이동 해서 오른족 서브트리중 왼쪽 서브트리가 있다면
# 왼쪽 서브트리 탐색 만약 왼쪽 서브트리가 존재하지 않는다면 오른쪽 서브트리로 이동
# 반복

# 중위순회의 특징은 오름차순으로 정렬된다는것.
class Node:

	# init
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


	# insert node
	# 27 12
	# 데이터가 들어왔을때 현재 저장되어 있는 데이터보다
	# 작다면 왼쪽 크다면 오른쪽에 저장해주는데
	# 대신 조건은 처음에 None으로 초기화 되어 있기 때문에
	# 값이 존재하지 않고 있다
	# 때문에 left child, right child에 값이 존재하지 않을때만
	# 데이터를 저장시킨다.
	# 처음에 만약 첫 데이터가 존재하지 않는다면 그 첫 데이터를 넣어주는 작업을 먼저 진행해준다.
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)


			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)

		else:
			self.data = data

	def printTree(self):
		if self.left:
			self.left.printTree()

		print(self.data),

		if self.right:
			self.right.printTree()


	def inorderTraversal(self, root):
		res = []
		if root:
			# left -> current -> right
			res = self.inorderTraversal(root.left)
			print(res)
			res.append(root.data)
			res = res + self.inorderTraversal(root.right)
		return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.printTree())
print(root.inorderTraversal(root))
