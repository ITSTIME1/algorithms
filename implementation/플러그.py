import sys 

N = int(sys.stdin.readline().rstrip())


result = []
for i in range(N):
	count = 0
	dice = list(map(int, input().split()))

	for j in dice:
		# 3개 이상이다
		check = dice.count(j)
		if check == len(dice):
			result.append(10000+(j*1000))
		elif check == len(dice) - 1:
			result.append(1000+(j*100))
		else:
			result.append(max(dice) * 100)
		result = list(set(result))

print(max(result))
