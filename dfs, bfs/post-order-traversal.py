# 후위순회


# 루트노드를 마지막에 방문한다

# 왼쪽 서브트리를 먼저 방문하고
# 그뒤를 이어서 오른쪽 서브트리를 방문하고
# 그리고 나서 root 노드를 방문하게 되는형태가 된다.
from queue import Queue
 
queue = Queue()
class Node:
   def __init__(self, val):
 
       self.leftChild = None
       self.rightChild = None
       self.data = val
 
 
# Insert Node
# 후위순회도 앞서 두 탐색 알고리즘 처럼
# 똑같은 방식으로 넣어지게 되는데

   def insert(self, data):
       if data is None:
           return
       if self.leftChild is None:
           self.leftChild = Node(data)
           #print(self.data, '-- Left -->', data)
           data = None
       elif self.rightChild is None:     
           self.rightChild = Node(data)
           #print(self.data, '-- Right -->', data)
           data = None
       else:
           queue.put(self.leftChild)
           queue.put(self.rightChild)
 
       while queue.empty() is False:
           queue.get().insert(data)
 
# Print tree
   def printTree(self):
       ret = []
       ret.append(self.data)
       if self.leftChild is not None:
           queue.put(self.leftChild)
       if self.rightChild is not None:
           queue.put(self.rightChild)
 
       #print (len(stack))
       while queue.empty() is False:
           ret = ret + queue.get().printTree() 
       return ret
 
 
# postorder traversal
# leftChild -> rightChild -> parent
# 여기가다르다
# 가장 마지막에 방문하게 끔 append(data가 가장 아래에 있는걸 확인할 수 있따.)

   def postorderTraversal(self, root):
       ret = []
       if root:
           ret = ret + self.postorderTraversal(root.leftChild)
           ret = ret + self.postorderTraversal(root.rightChild)
           ret.append(root.data)
       return ret
 
root = Node(27)
root.insert(14)
root.insert(5)
root.insert(10)
root.insert(6)
root.insert(31)
root.insert(9)
print("\n\nData is tree is = ", root.printTree())
 
print("\n\nresult of postorder traversal is = ", root.postorderTraversal(root))


# 그럼 정리해보자면
# 트리 탐색방법에는 3가지 트리 탐색방법이 있는데
# 1. 중위순회 - in-order-traversal 이라고 불리며 왼쪽-루트-오른쪽 순으로 탐색을 진행
# 2. 전위순회 - pre-order-traversal 이라고 불리며 루트 - 왼쪽 - 오른쪽 으로 탐색하는 방법이다.
# 3. 후위순회 - post-order-traversal 이라고 불리며 왼쪽- 오른쪽 - 루트 순으로 탐색을 진행 하는 방법.


# 그럼 여기서 트리와 그래프의 차이가 궁금한데 결정적인 차이 하나는
# 트리는 사이클이 없다
