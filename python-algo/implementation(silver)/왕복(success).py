
import sys
N, K = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().strip().split()))
result = 0
k = K
# 22
total = sum(num)
def p(num):
	global result, k
	n = len(num)
	for i in range(n):
		k -= num[i]
		if k < 0:
			result = i+1
			break
	return result

# 왕복이 문제네
def w(num, total):
	global result, k
	n = len(num)
	isA = False
	for j in range(n):
		k -=num[j]
		if k < 0:
			break
		else:
			isA = True
	# 0도 주어진다고 하니까
	if isA == True:
		for i in range(n, -1, -1):
			k -= num[i-1]
			if k < 0:
				result = i
				break
	return result
# 편도
if K < sum(num):
	print(p(num))
# 왕복
elif K >= sum(num):
	print(w(num, total))

# 5 32
# 7 4 2 4 5