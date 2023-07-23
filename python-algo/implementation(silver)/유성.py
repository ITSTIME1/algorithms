import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 문제분석

# 유성이 떨어졌을때의 사진을 복원하면 된다고 한다.

R, S = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(R)]

stand = R // 2 

# 유성 가장 아래
# 해당 유성의 좌표가 가장 중요한데
# 또한 그 해당 유성에서 각각의 거리가굉장히또 중요한데
# ㅅㅂ
뭐지;;

useng, dol = 0, 0
for i in range(0, stand):
	c = board[i]
	for j in c:
		if j == "X":
			useng = i


