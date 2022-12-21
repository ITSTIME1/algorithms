# 문제분석
# i, j 부터 x, y 까지의 합을 구해라?


# pypy3는 시간초과
import sys

n, m = map(int, sys.stdin.readline().split())
dp = [list(sys.stdin.readline().split()) for _ in range(n)]


def go(di, dj, dx, dy):
	cnt = 0
	for i in range(di-1, dx):
		for j in range(dj-1, dy):
			cnt += int(dp[i][j])
	return cnt

for _ in range(int(sys.stdin.readline())):
	i, j, x, y = map(int, input().split())	
	ans = go(i, j, x, y)
	print(ans)
# for i in range(i-1, x):
# 	for j in range(j-1, y):
# 		dp[i][j]

# O(90000 * 10000)
