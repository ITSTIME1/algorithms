# import sys
# import heapq
# import math
# from collections import deque
# from itertools import permutations, combinations, product, combinations_with_replacement
# input = sys.stdin.readline




# 일단 거리가 최소가 되려면 지름길을 가는게 가장 베스트니까
# 지름길이라는게 더 빨리 가 수 있도록 만들어진 길이니까 

# 그럼 지름길을 최대한 많이 선택할수록 거리는 줄어드니까 문제에 목적에 부합되네

# 5 150
# 0 50 10 o
# 0 50 20 x
# 50 100 10 o
# 100 151 10
# 110 140 90

# 총 길이는 변하지 않지만
# 내가 가야하는길이는 변하지

# 그럼 따라서 그냥 50만큼 가는길이나 지름길을 통해 10만큼 가는길이나 지름길로 가는게 더 최소가 되기 떄문에
# 지름길을 선택한다면
# 10(지름길o) + 10(지름길o) + 10(지름길o) + 30(지름길을x) + 10(지름길x) = 70만큼 가게됨.

# 세번째 길에서 50만큼 가는거랑 10만큼 가는거랑 당연히 차이가 존재하기 때문에 10
# 그럼 100부터 시작하게 되는데 100 에서 151만큼은 갈 수 없기 때문에 패스
# 100에서 110만큼 가야되고 그럼 여기서 10만큼 간뒤
# 110 - 140까지 가는길을 찾아야하는데 문제는 지름길을 가지 않고 30만큼 가는거 지름길을 가면 90만큼 가게 되는데 결국 지름길을 가지 않는게 더 짧게 가는것이기 때문에
# 110 에서 30만큼 가게 되면 140만큼 가게 되는거고
# 거기에 140-10만큼 가야 150이기 때문에 여기서부터는 그냥 간다고 한다면 10만큼 가야한다

# 이렇게 하면 되네 너무 이상하게 생각했었다



# 2 100
# 10 60 40
# 50 90 20



# 가장 작은 시작점이 10이기 때문에 10부터 시작한다고 본다면


# 40(지름길o) + 40 = 80
# 지름길을 타면 그 만큼 갈 수 있기 때문에 다음은 60에서시작
# 그럼 다음 지름길은 이미 지나쳤기 때문에 못가니까
# 60-100까지는 그냥 가야됨 따라서 40만큼 가야되니

# 총 가야하는길은 80만큼이다.



# 8 900
# 0 10 9
# 20 60 45
# 50 70 15
# 80 190 100
# 140 160 14
# 160 180 14
# 420 901 5
# 450 900 0


# 그럼 도착순서대로 해볼까
# 도착순은 아니고 그럼 시작순이 가장 빠르면서 도착순도 빠른?


# 0 10 9
# 20 60 45
# 50 70 15
# 140 160 14
# 160 180 14
# 80 190 100
# 450 900 0
# 420 901 5

# sort를 그렇게 해야될거 같은데


# print(9+10+40+80+14+14+270)


# import sys
# import heapq
# import math
# from collections import deque
# from itertools import permutations, combinations, product, combinations_with_replacement
# input = sys.stdin.readline




# n, d = map(int, input().split())

# arr = [tuple(map(int, input().split())) for i in range(n)] 

# arr_sorted = sorted(arr, key=lambda x : (-x[1], -x[0]))

# print(arr_sorted)



다익스트라?
그리디가 안되는거같다 3번예제에서 막힌다. 그럼 다른 방법이 있다는 뜻이되고
bfs, 다익스트라 이 두개를 찾았는데 ;; 뭘까 이허무함.
그래프 풀때 다시 해보자.
# 마지막 예ㅔ주머지';
# [(0, 10, 9), 
# (20, 60, 45), 
# (50, 70, 15), 
# (80, 190, 100), 
# (140, 160, 14), 
# (160, 180, 14), 
# (420, 901, 5), 
# (450, 900, 0)]


