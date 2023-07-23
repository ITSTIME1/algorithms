import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
ma = min(a, b)
mb = max(a, b)
i = 1
c = mb-ma-1
tmp = []

if ma == mb or ma+1 == mb:
	c = 0
	print(c)
else:
	while i <= c: 
		ma += 1
		i += 1
		tmp.append(ma)

	print(c)
	print(*tmp, end = " ")

