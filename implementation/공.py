M = int(input())

cup = [1, 2, 3]
for i in range(M):
	x, y = map(int, input().split())

	xIn = cup.index(x)
	yIn = cup.index(y)

	cup[xIn], cup[yIn] = cup[yIn], cup[xIn]
print(cup[0])

# 1 2 3
# 3 2 1
# 2 3 1
# 2 1 3
# 3 1 2