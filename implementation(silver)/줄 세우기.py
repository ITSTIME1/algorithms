import sys
import heapq
import math
from string import ascii_uppercase
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



n = int(input())

alpha = list(ascii_uppercase)


name = [input().strip() for i in range(n)]



# 첫 문자들의 상태가 오름차순인 상태냐가 아니라
# 그 상태가 오름차순으로 가지냐인거지
# 즉 단어 전체를 고려해야되는 문제인거
	
# 첫 문자가 나오고
index = alpha.index(name[0][0])

if sorted(name) == name:
	print("INCREASING")
elif sorted(name, reverse=True) == name:
	print("DECREASING")
else:
	print("NEITHER")
# D, I = 0, 0
# for i in name:
# 	pr = alpha.index(i[0])

# 	if index > pr:
# 		D += 1
# 		index = pr
# 	elif index == pr:
# 		continue
# 	else:
# 		I += 1
# 		index = pr


# if D == 0 and I != 0:
# 	print("INCREASING")
# elif D != 0 and I == 0:
# 	print("DECREASING")
# else:
# 	print("NEITHER")