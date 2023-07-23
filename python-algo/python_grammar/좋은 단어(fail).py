import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

string = [input().strip() for _ in range(n)]

def word_check(word):
	dic = {}
	for i in word:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1

	isCheck = True
	for i in dic.items():
		if i[1] % 2 != 0:
			isCheck = False
			break
	return isCheck


cnt = 0
for i in string:
	word = i
	check = word_check(word)

	if check == False:
		continue

	stack = []
	for j in range(len(word)):
		if len(stack) == 0:
			stack.append(word[j])
		else:
			if word[j] == stack[-1]:
				stack.pop()
			else:
				stack.append(word[j])

	if len(stack) == 0:
		cnt += 1
print(cnt)

