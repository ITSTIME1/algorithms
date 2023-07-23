import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline
# 2번 예제 빼고 다맞게 나오는데


dartResult = "1S2D*3T"

# 음 여기서 10을 체크해야되는데
# 리스트로나누면 1, 0둘로 나눠지니..
# 이걸 어떻게 하나....

# 0~9니까

S = 1
D = 2
T = 3
d_l = list(map(str, str(dartResult)))

word = []

pre, index = 0, 0
for i in range(len(d_l)):
	if d_l[i].isdigit() == True:
		# 10 일 경우를 생각해주어야함.
		if len(word) != 0:
			if str(word[-1]) + str(d_l[i]) == "10":
				re = int(str(word[-1]) + str(d_l[i]))
				word.pop()
				word.append(re)
				continue

		word.append(int(d_l[i]))
		pre = index
		index += 1
	elif d_l[i] == "S":
		word[-1] = word[-1] ** S
	elif d_l[i] == "D":
		word[-1] = word[-1] ** D
	elif d_l[i] == "T":
		word[-1] = word[-1] ** T

	elif d_l[i] == "*":
		if pre != 0:
			word[pre] = word[pre] * 2
			word[pre-1] = word[pre-1] * 2
		elif pre == 0:
			word[pre] = word[pre] * 2

	elif d_l[i] == "#":
		word[pre] = word[pre] * -1


print(sum(word))






	