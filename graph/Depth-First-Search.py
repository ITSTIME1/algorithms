# DFS algorithm in Python


# DFS algorithm
# 야무지네.
def dfs(graph, start, visited=None):
    # 처음엔 none 이니까 visited 를 생성 하고
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    # 1
    # for next in graph[start] - visited:
    #     dfs(graph, next, visited)
    # return visited

    # 2
    # for i in graph[start]:
    #     if i not in visited:
    #         difs(graph, i, visited)


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')

