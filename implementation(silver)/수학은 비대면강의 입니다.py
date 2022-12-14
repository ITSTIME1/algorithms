# 완전탐색 문제이지만
# 이런 연립방정식 문제는 가감법으로도 풀 수 있다.

a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000):
	for j in range(-999, 1000):
		if a*i + b*j == c and d*i + e*j == f:
			print(i, j)
			exit()

ax + by = c
dx + ey = f
# x = (c*e-b*f) // (a*e-b*d)
# y = (c*d-a*f) // (b*d-a*e)

