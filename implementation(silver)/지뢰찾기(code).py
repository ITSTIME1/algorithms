import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

game = [input().strip() for _ in range(n)]
game_check = [input().strip() for _ in range(n)]

m = []
for i in range(len(game)):
	for j in range(len(game)):
		if game[i][j] == "*":
			m.append((i, j))

dic = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]

def simul(di, dj, game):
	total = 0
	for i in range(len(dic)):
		oi = di + dic[i][0] 
		oy = dj + dic[i][1]	
		if 0<= oi < n and 0<= oy < n:
			if game[oi][oy] == "*":
				total += 1
	return total



board_check_list = [["." for _ in range(n)] for _ in range(n)]

isActive = True
for i in range(len(game_check)):
	for j in range(len(game_check)):
		if game_check[i][j] == "x" and game[i][j] == ".":
			# 지뢰의 개수를 반환받고
			a = simul(i, j, game)
			board_check_list[i][j] = str(a)
		elif game[i][j] == "*" and game_check[i][j] == "x":
			isActive = False

# 지뢰가 있는 칸이 열려 있다면 모든 칸이 *
# 지뢰가 없으면서 열린칸은 아래처럼
if isActive == False:
	for i in m:
		c = i
		board_check_list[c[0]][c[1]] = "*"
	for i in board_check_list:
		print("".join(i), end = "\n")
else:
	for i in board_check_list:
		print("".join(i), end = "\n")





# 아맞네 아까는 지뢰를 밟으면 break 걸어서 무조건 해당하는 곳까지만
# 지뢰를 출력했었는데
# 지뢰릘 밟았어도 모든 구간에 있는 지뢰의 개수를 포함시켜주어야한다.







