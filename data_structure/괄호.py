# 문제분석

# 괄호를 채워라 이거 그냥 짝이 맞으면 되는거 아니야?

# ((())) 이런건 vps 라는건 짝이 전부 맞다는거자나
# 그럼 짝이 맞게끔 만들면되지



import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


# vps = yes
# no


def main(string):
	stack = []
	for i in string:
		if i == "(":
			stack.append(i)
		elif i == ")":
			if stack:
				check = stack[-1]
				if check == "(":
					stack.pop()
				else:
					stack.append(i)
			else:
				stack.append(i)

	if len(stack) == 0:
		return "YES"
	else:
		return "NO"

for _ in range(t):
	string = input().strip()
	ans = main(string)
	print(ans)