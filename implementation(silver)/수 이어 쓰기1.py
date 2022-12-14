N = int(input())


result = 0
for i in range(len(str(N))):
	c = (N - (10**i) + 1)
	result += c
print(result)


def solution(N):
	return sum([(N-(10**i)+1) for i in range(len(str(N)))])

print(solution(N))	