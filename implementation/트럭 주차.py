import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
from collections import defaultdict
input = sys.stdin.readline



# 문제정의는 맞는데
# 접근이 틀린거 같네
letters = "dongbina"
letter_dic = defaultdict(int)

for i in letters:
	letter_dic[i] += 1

print(letter_dic)