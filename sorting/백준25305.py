N, K = map(int, input().split())

# grade
grade = list(map(int, input().split()))

for i in range(N):
	min_index = i
	for j in range(i+1, len(grade)):
		if grade[min_index] > grade[j]:
			min_index = j
	grade[i], grade[min_index] = grade[min_index], grade[i]

print(grade[N-K])

grade.sort()
print(grade[N-K])