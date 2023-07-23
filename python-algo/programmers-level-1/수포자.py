import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


one = [1,2,3,4,5]
two = [2,1,2,3,2,4,2,5]
three = [3,3,1,1,2,2,4,4,5,5]

# 규칙은 저렇게 이어지니까

# 최대 10000 문제로 구성되어져 있으니까

# 6번째 문자라고 한다면
# 해당 번째 문제 % 문제의 길이 - 1 하게 되면 해당 문제의 답이 나오네
# 6 % 5 == 1-1 = 0
# 7 % 5 == 2=1 = 1

answers = [1,2,3,4,5]
dic = {"1": 0, "2": 0, "3": 0}

for i in range(len(answers)):
	if answers[i] == one[i%len(one)]:
		dic["1"] += 1

	if answers[i] == two[i%len(two)]:
		dic["2"] += 1

	if answers[i] == three[i%len(three)]:
		dic['3'] += 1
maxVal = [int(k) for k,v in dic.items() if max(dic.values()) == v]
maxVal.sort()
print(maxVal)