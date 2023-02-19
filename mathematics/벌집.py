
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 중앙방 1번부터 n번방가지
# 최소 개수의 방을 지나서 갈대 그니까 방을 들리는 횟수를 최소로 하고 싶다는 얘기고

# 그때의 최소방의 개수를 구하라고 하는거네
# 그럼 벌집은 총6각형이자나



n = int(input())

cnt = 1
result = 0
while n > result:
	result += cnt * 6
	cnt += 1


print(cnt)