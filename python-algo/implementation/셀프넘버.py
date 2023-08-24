
import sys
input = sys.stdin.readline
num = [i for i in range(1, 10001)]

c = set()
for i in num:
	d = i
	for j in str(d):
		d += int(j)
	c.add(d)

s = list(set(num) - c)
s.sort()
for i in s:
	print(i, end = "\n")
