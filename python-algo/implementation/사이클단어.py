import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

word = [input().rstrip() for _ in range(N)]


for i in range(N):
	stand = word[i]

	for j in range(N):
		compare_word = deque(word[j])
		
		len_word = len(compare_word)
		flag = True
		while len_word > 0:
			compare_word.rotate(1)
			if "".join(compare_word) == stand:
				flag = False
				break
			len_word -= 1
		if not flag:
			word[j] = stand

print(len(set(word)))


