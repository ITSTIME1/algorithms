N = int(input())

for _ in range(N):
	st = list(input())
	for i in range(len(st)):
		if i == 0:
			st[i] = st[0].upper()
			break
	print("".join(st))
	