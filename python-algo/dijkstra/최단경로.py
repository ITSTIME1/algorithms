

# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())

# start = int(input())

# INF = 1e9
# graph = [[] for _ in range(V+1)] 
# visited = [False] * (V+1)
# distance = [INF] * (V+1)


# for i in range(E):
#     # 방향 그래프기 때문에 u -> v로 가는걸 말함.
#     # u->v로 갈때 w만큼의 가중치가 듬
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))

# # 이렇게 그래프를 만들고
# def get_smallest():
#     min_value = INF
    
#     index = 0
    
   
#     for i in range(1, V+1):
#         # 3, 8이 있어야 하는데 
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
    
#     return index
            
    

# def dijkstra(start):
    
#     distance[start] = 0
#     visited[start] = True
    
    
#     for i in graph[start]:
#         distance[i[0]] = i[1]
   
#     for _ in range(V-1):
        
#         current = get_smallest()
#         visited[current] = True
        
#         for j in graph[current]:
#             cost = distance[current] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
                
# dijkstra(start)

# for n in distance[1:]:
#     print(n if n != INF else "INF")

# 오케이 이렇게 했을때 시간이 초과가 난다는건 알게 되었고
# 왜냐하면 선형탐색을 해야 되기 때문에모든 정점에대해서
# v-1 에서 * v만큼 또 탐색을 진행해야 되므로
# V^2인 것만큼 탐색하고 있다
# 따라서 V = 300,000
# 까지 주어질 수 있기 때문에 300000 * 300000 = 90000000000 만큼의 시간이 든다.
# 그렇기 때문에 이걸 O(n logn)의 시간복잡도로 만들기 위해서 우선순위 큐를 사용한다.


# 그럼 이제 이걸 우선순위 큐를 활용해서 한번 구현해보자
import sys
import heapq
input = sys.stdin.readline

INF = int(1e10)


V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V+1)] 

distance = [INF] * (V+1)
 

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))



def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 우선순위가 낮은것부터 계속 찾는데 왜그러지
        # 우선순위로 가장 비용이 적은걸 우선으로 뽑는다.
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
    
        for i in graph[now]:
            # 현재 가지고 있는 노드와 다음 노드의 거리를 합했을때
            # 그 cost비용이 현재 그 노드가 가지고 있는 비용보다 작다면 갱신한다.
            cost = distance[now] + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in distance[1:]:
    print(i if i != INF else "INF")