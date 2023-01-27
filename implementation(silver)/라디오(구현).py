#

import sys
input = sys.stdin.readline


# 음 어디서 틀린거지?

a, b = map(int, input().split())
n = int(input())
zu = [int(input()) for _ in range(n)]

def one(arr, b):
	maxVal, minVal, cnt = max(a, b), min(a, b), 1
	max_go, min_go = max(arr[0], b), min(arr[0], b)
	# 루트에서 가는거
	root = maxVal - minVal
	
	# 즐겨찾기에서 가는거
	root_b = max_go - min_go

	if root == root_b:
		return root

	if root < root_b:
		return root
	else:
		cnt += root_b
		return cnt	


def notOne(arr): 
	maxVal = max(a, b)
	minVal = min(a, b)
	# 11
	root_a = maxVal - minVal

	li = []
	for i in range(len(arr)):
		mAx = max(arr[i], b)
		mIn = min(arr[i], b)
		li.append(mAx-mIn)

	li.sort()

	if li[0] > root_a:
		return root_a 
	else:
		return li[0] + 1

if n == 1:
	# 가고자하는 주파수가 즐겨찾기에 등록되어 있다면 바로 이동 1 == 이동횟수
	if b in zu:
		print(1)
	else:
		ans = one(zu, b)
		print(ans)
else:
	ans = notOne(zu)
	print(ans)


# 64 566
# 1
# 567



# 1 3
# 1
# 5