N = int(input())

grade = []
for i in range(N):
	grade.append(int(input()))


for j in range(1, len(grade)):
	for k in range(j, 0, -1):
		if grade[k] < grade[k-1]:
			grade[k], grade[k-1] = grade[k-1], grade[k]
		else:
			break

print(*grade, sep="\n")
