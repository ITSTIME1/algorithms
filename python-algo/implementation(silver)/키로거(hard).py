import sys
from collections import deque
input = sys.stdin.readline



# 아이디어가 이거네 왼쪽 리스트와 오른족 리스트를 따로 만들어서
# 왼쪽 화살표가 나오면
# 왼쪽 리스트에 오른쪽 이동한 값을 넣어주고
# 오른쪽 화살표가 나오면 왼쪽 리스트의 마지막값을 넣어주고
# 그렇게 가장 또 왼쪽 이 나오면 오른쪽에 있는 값중 가장 첫번째 값을 넣어주고
# 그렇게 해서 마지막에 합쳐준다면 답이나오네


# 리스트를 하나가지고 인덱스를 이동하는 방법만 생각했었는데
# 스택과 큐의 조합이 신선하네
# 스택을 두개 만들어서 나눠서 저장하다니

# sss
t = int(input())


for _ in range(t):
	left = deque([])
	right = deque([])
	pwd = input().strip()

	for x in pwd:
		if x == ">":
			if right:
				left.append(right.popleft()) 
		elif x=="<":
			if left:
				right.appendleft(left.pop())
		elif x=="-":
			if left:
				left.pop()
		else:
			left.append(x)

	print("".join(left) + "".join(right))