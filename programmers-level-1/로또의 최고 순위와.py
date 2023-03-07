import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 1. 로또 번호와 모두 다 일치하는 경우 (최선 최악 둘다 1, 1)

# 2. 로또 번호가 모두 다 일치하지 않을경우
# 로또와 당첨번호 중 일치하는 개수 = 최악
# 로또와 당첨번호 중 일치하는 개수 + 0의 개수 = 최선




lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

dic = {"6": 1, "5": 2, "4": 3, "3": 4, "2": 5, "1": 6, "0": 6}

cor = 0
zero = 0

ans = []
answer = []

for i in range(len(lottos)):
	if lottos[i] in win_nums:
		cor += 1

	elif lottos[i] == 0:
		zero += 1

ans.append(cor+zero)
ans.append(cor)
# 0의 개수가 곧 0만 모두 맞히면 최선의 개수가 된다는 뜻
# 
# 이때는 0의 개수가 6개
# 맞은 개수가 0개
# 즉 맞은 개수가 없을때가 최악

# [cor+zero, cor]
# [6, 0]

for i in ans:
	answer.append(dic[str(i)])

print(answer)

	
# 음 뭔가 이게 맞을지 안맞을지 되게 긴가민가했는데 맞네..




