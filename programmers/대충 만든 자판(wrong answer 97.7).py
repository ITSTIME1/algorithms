import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 정확성 56?..

# 정확성이 더 떨어졌는데

# 오케이 아까 코드에서 하나만 실패인데 하나ㅡㄴㄴ뭔데..?
# 95.7...
def check(word, arr2):
	a = []
	for i in range(len(arr2)):
		if word == arr2[i]:
			a.append(i)

	return min(a)



def solution(keymap, targets):
	arr = [list(i) for i in keymap]
	answer = []
	dic = {i: 0 for i in targets}
	
	for i in targets:
		w = list(i)
		for j in w:
			j_word = []
			for k in range(len(arr)):
				if j in arr[k]:
					if arr[k].count(j) >= 2:
						a = check(j, arr[k])
						j_word.append(a+1)
					else:
						a = arr[k].index(j)

						j_word.append(a+1)


			if len(j_word) == 0:
				dic[i] = -1
				break
			else:
				dic[i] += min(j_word)

	for i in dic.values():
		answer.append(i)

	return answer

keymap = ["AGB", "BSSS"]
targets = ["CCC", "CCC"] 
a = solution(keymap, targets)
print(a)
