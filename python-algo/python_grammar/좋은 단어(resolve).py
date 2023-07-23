import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(n):
	string = input().strip()

	stack = []
	for j in range(len(string)):
		if len(stack) == 0:
			stack.append(string[j])
		else:
			if string[j] == stack[-1]:
				stack.pop()
			else:
				stack.append(string[j])

	if len(stack) == 0:
		cnt += 1

print(cnt)

# 뭔가 내가 너무 꼬이게 생각한거 같은데
