import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline



# 이진 트리가 주어질때
# 이 이진 트리를 순회하면 어떤 결과가 나오는지 맞춰봐라는거지 
# 근데 문제는 그냥 재귀의 방법으로 하면 상관이 없는데

# 그럼 클래스화 시켜두면 되지 않을까.
# 클래스화를 시켜둔다는게

n = int(input())


in_list, pre_list, post_list = [], [], []
class Node:
	def __init__(self, root, left, right):
		self.leftChild = left
		self.rightChild = right
		self.data = root

def inorder(data):
	if data.leftChild != ".":
		inorder(tree[data.leftChild])
	
	in_list.append(data.data)

	if data.rightChild != ".":
		inorder(tree[data.rightChild])

def preorder(data):
	pre_list.append(data.data)
	if data.leftChild != ".":
		preorder(tree[data.leftChild])

	if data.rightChild != ".":
		preorder(tree[data.rightChild])
	
def postorder(data):
	if data.leftChild != ".":
		postorder(tree[data.leftChild])
	
	if data.rightChild != ".":
		postorder(tree[data.rightChild])
	
	post_list.append(data.data)

	


tree = {}
for i in range(n):
	root, left, right = input().split()
	tree[root] = Node(root, left, right)

inorder(tree["A"])
preorder(tree["A"])
postorder(tree["A"])

print("".join(pre_list))
print("".join(in_list))
print("".join(post_list))