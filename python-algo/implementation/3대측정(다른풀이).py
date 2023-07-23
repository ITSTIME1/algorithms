N, K, L = map(int, input().split())

cnt = 0
tmp = []

for i in range(N):
	a, b, c = map(int, input().split())
	if a >= L and b >= L and c >=L:
		if a+b+c >= K:
			cnt+=1
			tmp.append(a)
			tmp.append(b)
			tmp.append(c)
print(cnt)
print(*tmp)

