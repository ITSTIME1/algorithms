from itertools import combinations

ar = [1, 2, 3, 4]
for i in combinations(ar , 3):
	print(list(i))
	print(sum(list(i)))

# test