# 그래프(graph) 는 비선형 방식의 데이터 구조이다.

# 비선형 이란? (non-linear-structure)
# 1개의 노드에 여러개의 노드 가 연결되어 있을 수 있는걸 말한다.
# 비례식으로 나타내면 1:n 관계이다
# 앞서 트리를 배웠을때도 똑같이 비선형 구조라고 얘기했었는데
# 비선형 방식의 데이터구조엔 트리와 그래프가 있다

# 때문의 최대 가질 수 있는 노드개수가 2로 한정 짓는다면 이진트리라는걸 알 수 있는데
# 그 이진 트리에서도 하나의 정점의 2개의 자식노드들이 있다라는 것.
# 이것 또한 1:n의 관계에 해당하게 된다.

# 때문에 그래프에서 비선형 구조라고 한다면 한개의 정점의 다중 정점들을 가지고 있구나 생각하면 된다.
# 이런 그래프를 표현하는 방식은 두가지가 있는데

# 1. adjacency list (인접 리스트 방법이다)
# 일전에도 구현해본적이 있는데 관련 개념만 알고 그래프의 대한 문제 풀이가 없어서 까먹었으니
# 그래프의 구현을 한번 해보겠다.


# 그래프는 부모노드가 존재하지 않는다
# 그럼 부모-자식간의 관계가 없다라는건가

# 트리에서는 그래프를 순회 한다고 해서 dfs 방법이 3가지 정도 존재했다


# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = {}

	# function to add an edge to graph
	# u : unmarked, v : 정점
	def addEdge(self, u, v):
		if u in self.graph:
			self.graph[u].append(v)
		else:
			self.graph[u] = [v]

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex

		# {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

	
    def DFS(self):
        # create a set to store all visited vertices
        visited = set()
    # call the recursive helper function to print DFS traversal starting from all
    # vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# 0, 1, 2, 3
g.DFS(0)
print()
print(g.graph)


# 이코드는 코너케이스를 처리할때 문제가 되는데
# 연결이 끊어진 그래프에서는 모든 정점에 도달 할 수 없다
# 왜냐하면 도달가능한 정점만 돌기 때문에