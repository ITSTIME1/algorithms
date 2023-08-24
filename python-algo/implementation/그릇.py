# 이전 뚜겅에 영향을 받네
# 처음 뚜겅이 없다면 무조건 10cm 쌓이고
import sys
# from collections import deque
input = sys.stdin.readline

s = deque(input().strip())
s = input().strip()

a = []
total = 0
while s:
	index = s.popleft()
	if not a :
		a.append(index)
		total += 10
		continue
	if a[-1] == index:
		total += 5
	else:
		total += 10
	a.append(index)

print(total)



total = 10
for i in range(1, len(s)):
	if s[i] != s[i-1]:
		total += 10
		continue
	total += 5

print(total)