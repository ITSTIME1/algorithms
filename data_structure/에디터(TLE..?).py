# 문제분석 
# B가 거슬리는새기네
# 시간초가 극악 무도하네;;
# 이걸 리스트를 하나 더 만들어서 할 줄은 생각도 못했네;
# insert 가 당연히 O(1) 만큼의 연산을 수행할 줄 알았는데 그게 아니었네


import sys
from collections import deque

string = deque((sys.stdin.readline().strip()))
m = int(sys.stdin.readline().strip())

cur = len(string)-1

def PCMD(s):
	global cur
	if cur == 0:
		string.appendleft(s)
	else:
		# insert 가 문제 insert 의 시간복잡도는
		# O(N)
		# 따라서 insert 함수를 썼기 때문에 최대 명령수 만큼
		# 최악의 경우를 생각해낸 방법이 되었다..
		string.insert(cur+1, s)
		cur = len(string)-1

def LCMD():
	global cur
	if cur == 0:
		pass
	else:
		cur-=1

def DCMD():
	global cur
	if cur == len(string)-1:
		pass
	else:
		cur += 1

def BCMD():
	# 이게 문제인데
	global cur 
	if cur == 0:
		if cur == 0 and len(string) == 2:
			del string[0]
		else:
			pass
	else:
		del string[cur]
		cur -= 1


def solve(arr):
	if arr[0] == "P":
		PCMD(arr[1])

	else:
		if arr[0] == "L":
			LCMD()
		elif arr[0] == "D":
			DCMD()
		elif arr[0] == "B":
			BCMD()

for _ in range(m):
	c = list(input().split())
	solve(c)

print("".join(string))


