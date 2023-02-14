# 너비우선탐색이라고

# 넓게 먼저 탐색하는 방법이다.

# dfs 같은경우 가장 왼쪽 부터 탐색을 했었는데
# 이건 처음 시작 하는 루트에서 그 루트와 인접한 노드들을 큐에 넣어준다음
# 큐에서 하나씩 popleft 해서 그 인접한 노드들도 queue에 추가하는 방식이다
# 이러케 인접한 것들 부터 먼저 방문한 뒤에
# 인접하지 않은 것들을 방문해나간다.


# BFS algorithm in Python


import collections

# BFS algorithm
def bfs(graph, root):

    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def bfs(graph, root):
    visited = set()

    queue = deque([str(root)])
    visited.add(str(root))

    while queue:
        vertex = queue.popleft()

        for v in graph[str(vertex)]:
            if str(v) not in visited:
                visited.add(str(v))
                queue.append(str(v))
    return visited


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
