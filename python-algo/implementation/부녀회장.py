T = int(input())

for _ in range(T):
	k = int(input())
	n = int(input())

	people = [j for j in range(1, n+1)]
	for i in range(k):
		for m in range(1, n):
			people[m] += people[m-1]

	print(people[-1])

