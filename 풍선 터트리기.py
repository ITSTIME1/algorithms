# 문제분석

import sys
input = sys.stdin.readline


n = int(input())
balloon = list(map(int, input().split()))

dic = {i: False for i in range(n)}

dic[0] = True
arr = [1]

cur = 0
while len(arr) != n:
	# 만약 ballon 현재 인덱스가 양수라면 더해주고
	# 음수라면 빼줄건데
	# 양수인데 index가 넘어가는 경우가 생기고
	# 음수인데 0보다 작아지는경우가 생긴다
	if balloon[cur] > 0:
		cur += balloon[cur]
		if cur > len(balloon) - 1:
			cur = 0
		if dic[cur] == False:
			dic[cur] = True
			arr.append(cur+1)
		else:
			while True:
				cur += 1

				if cur > len(balloon) - 1:
					cur = 0

				if dic[cur] == False:
					break
				
			dic[cur] = True
			arr.append(cur+1)
	else:
		cur -= abs(balloon[cur])
		if cur < 0:
			cur = len(balloon) - 1

		if dic[cur] == False:
			dic[cur] = True
			arr.append(cur+1)
		else:
			while True:
				cur -= 1
				if cur < 0:
					cur = len(balloon) - 1
				if dic[cur] == False:
					break

			dic[cur] = True
			arr.append(cur+1)
print(*arr)



# 진짜 왜틀린지 모르겠따

# 5
# -5 -5 -5 -5 -5