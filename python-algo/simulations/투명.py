n, m = map(int, input().split())

dic = [[0 for _ in range(100)] for _ in range(100)]


for _ in range(n):
	x1, y1, x2, y2 = map(int, input().split())

	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			dic[i-1][j-1] += 1

ans = 0
for i in range(100):
	for j in range(100):
		if dic[i][j] > m:
			ans += 1

print(ans)