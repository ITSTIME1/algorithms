import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())


m = []
for i in range(n):
	word = input().strip().split()
	# [Save, As]
	count = 0
	for j in range(len(word)):
		if word[j][0].lower() not in m and word[j][0].upper() not in m:
			m.append(word[j][0])
			new_word = word[j].replace(word[j][0], "["+word[j][0]+"]", 1)
			word[j] = new_word
			break

		else:	
			count += 1

	if count == len(word):
		isActive = False
		for j in range(len(word)):
			for k in range(1, len(word[j])):
				# Format
				if word[j][k].upper() not in m and word[j][k].lower() not in m:
					m.append(word[j][k])
					new_word = word[j].replace(word[j][k], "["+word[j][k]+"]", 1)
					word[j] = new_word
					# 추가도는게 이상한
					isActive = True
					break
			if isActive == True:
				break

	print(*word)


	# 1. 단어의 첫 글자가 단축키로 지정되어 있는지 확인한다
	# 만약 단어의 첫 글자가 단축키로 지정되어 있지 않는다면 지정한다

	# 만약 한 단어의 첫글자가 단축키로 지정되어 있다고 한다면 두 단어 이상이라면 다음 단어도 똑같이 본다
	# 지정이 안되어있다면 지정한다
	# 만약 두 단어 전부 지정이 되어 있다면 word를 다시 탐색해서 지정안된 걸 찾는다
	# 지정안된게 있다면 그 단어를 바꾼다
