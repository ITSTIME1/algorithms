import sys
import heapq
from queue import Queue
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline



# 각노드와 왼쪽 자식 노드, 오른쪽 자식노드가 주어진다
# 1, 2, 3  = 각노드, 왼쪽자식노드, 오른쪽 자식노드

# 그럼 노드의 개수가 7개라고 한다면
# a-g 까지의 노드가 존재하고

# 항상 a가 루트노드가 된다고
# 자식노드가 없다면 .이걸로 표현 한다

n = int(input())

# 트리를 이렇게 표현도 가능하구나
# tree[root] = [left, right] 형태 그럼 이걸 이용해서 트리를 순회할 수 있겠다.
tree = {}
for i in range(n):
	root, left, right = input().split()
	tree[root] = [left, right]


# 중위
in_list, pre_list, post_list = [], [], []
def inorder(data):
	if data != ".":
		# 왼쪽
		inorder(tree[data][0])
		# 루트
		in_list.append(data)
		# 오른쪽
		inorder(tree[data][1])

# 전위
def preorder(data):
	if data != ".":
		# 루트
		pre_list.append(data)
		# 왼쪽
		preorder(tree[data][0])
		# 오른쪽
		preorder(tree[data][1])

# 후위
def postorder(data):
	if data != ".":
		# 왼쪽
		postorder(tree[data][0])
		# 오른쪽
		postorder(tree[data][1])
		# 루트
		post_list.append(data)


# 처음 루트는 무조건 a라고 하니까
# 재귀를 이해하는게 가장 중요할거 같네
# 아마 내가 사용하는 방법은 클래스를 이용해서 하는거니까
# 클래스를 이용해서 하는걸 한번 해봐야겠따

preorder('A')
inorder('A')
postorder('A')


print("".join(pre_list), end = "\n")
print("".join(in_list), end = "\n")
print("".join(post_list))


# 파이썬으로 트리를 이렇게 표현이 가능하구나
# 순회도 위와 같은 방식으로 하면되고
# 구지 노드를 만들어서 하는것보다 편리한거같은데
# none == 여기서 . 와 같은 거네



