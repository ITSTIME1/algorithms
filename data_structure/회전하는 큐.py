# 다시 짜야된다

# 문제분석

# 첫번째 연산은 = 첫번재 원소를 뽑아내는거
# 두번째 연산은 = 왼쪽으로 한칸 이동시키는거 -> 첫번째 원소를 빼서 마지막으로 넣어주는 연산
# 세번째 연산은 = 오른쪽 마지막 원소를 빼서 왼쪽 맨 앞으로 넣어준다.

from collections import deque
import itertools

n, m = map(int, input().split())
m_list = list(map(int, input().split()))

num = deque()
for i in range(n):
	num.append(i)

arr = deque()

for i in range(n):
	arr.append([i, i+1])
# m_list 를 가지고 오면서?

def correct(arr):
	arr.popleft()
	num.popleft()

def left_cal(arr, find, what):
	global ans
	for i in range(what):
		c = arr.popleft()
		arr.append(c)
		ans += 1

	if arr[0][1] == find:
		correct(arr)

def right_cal(arr, find, what):
	global ans
	for i in range(what):
		c = arr.pop()
		arr.appendleft(c)
		ans += 1

	if arr[0][1] == find:
		correct(arr)


		
ans = 0
for i in range(len(m_list)):
	# [1, 2, 3]
	find = m_list[i]
	# [0, 1]
	# [1, 2]
	# [2, 3]
	# [3, 4]
	if arr[0][1] == find:
		correct(arr)
		continue
	else:
		# check = index를 찾는거
		check = 0
		for i in range(len(arr)):
			if arr[i][1] == find:
				check = i 
		# 각각의 수의 개수가 얼마나 남았는지 보고
		# [0, 1, 2, 3, 4, 5, 6, 7]
		# [1, 2, 3, 4, 5, 6, 7, 8]
		leftVal = len(list(itertools.islice(num, 0, check)))
		rightVal = len(list(itertools.islice(num, check, len(num))))
		# 왼쪽으로 갈지 오른쪽으로 갈지
		what = min(leftVal, rightVal)
		if what == leftVal:
			left_cal(arr, find, what)
		else:
			right_cal(arr, find, what)


		# arr == [0, 1, 2, 3, 4, 5]
		# m_list = [3, 4, 5, 6]
print(ans)