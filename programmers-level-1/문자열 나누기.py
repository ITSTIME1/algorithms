import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

s = "aaabbaccccabba"


dic = {}

s_d = list(s)

isActive = True 
answer = []
while len(s_d) != 0:
	first_word = s_d[0]
	dic[first_word] = 0
	dic["f2"] = 0

	for i in range(len(s_d)):
		if s_d[i] == first_word:
			dic[first_word] += 1
		else:
			dic["f2"] += 1
		# 개수가 같아질떄
		if dic[first_word] == dic["f2"]:
			ans = s_d[:i+1]
			a = "".join(ans)
			answer.append(a)
			del s_d[:i+1]
			isActive = False
			break
		else:
			isActive = True
	# 단어가 만들어졌으니
	if isActive == False:
		continue
	# 단어가 안만들어졌다는건 마지막에 남은 문자가 있다는거니까
	else:
		ans = "".join(s_d)
		answer.append(ans)
		s_d.clear()

print(len(answer))