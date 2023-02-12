import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline



n = int(input())

# B, C

queue = deque([])

in_list = []
class Node:

	def __init__(self, val):
		self.leftChild = None
		self.rightChild = None
		self.data = val

	def insert(self, data):
		pre = False
		dot = False

		# 여기서 처리를 해주면 될거 같은데..
		# 하..
		if data == ".":
			if self.leftChild is not None and self.rightChild is None:
				in_list.append(self.leftChild.data)
				dot = True
				

			elif self.rightChild is not None and self.leftChild is None:
				in_list.append(self.rightChild.data)
				dot = True

		# same?
		if self.data == data:
			pre = True
			return

		if data is None:
			return 

		if self.leftChild == None:
			self.leftChild = Node(data)
			data = None

		elif self.rightChild == None:
			self.rightChild = Node(data)
			data = None

		else:
			queue.append(self.leftChild)
			queue.append(self.rightChild)

		while len(queue) != 0:
			if pre == True:
				queue.popleft().insert(None)

			elif pre == False and dot == True:
				in_list.append(self.data)
				queue.popleft().insert(None)
				dot = False
			else:
				queue.popleft().insert(data)



tree_list = []
for i in range(n):
	root, left, right = input().split()	
	tree_list.append(root)
	tree_list.append(left)
	tree_list.append(right)


d = Node("A")
for i in tree_list:
	d.insert(i)

print(in_list)