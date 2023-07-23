import itertools

N = 9

arr = [int(input()) for i in range(N)]
arr.sort()

pr_list = list(itertools.permutations(arr, 7))
print(len(pr_list)) # 18만 가지
result = []
for i in range(len(pr_list)):
	check = pr_list[i]
	if sum(check) == 100:
		result.append(check)
	else:
		continue

print(*result[0], sep="\n")