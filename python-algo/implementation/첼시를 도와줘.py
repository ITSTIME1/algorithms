import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
	p = int(sys.stdin.readline().rstrip())
	val = []
	play = []
	for i in range(p):
		c, s = input().rstrip().split()
		val.append(int(c))
		play.append(s)

	ch = val.index(max(val))
	print(play[ch])