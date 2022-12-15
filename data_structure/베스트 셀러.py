n = int(input())


# O(n + nlogn)
# dic in 은 O(1)
book = {}
for _ in range(n):
	string = input()
	if string not in book:
		book[string] = 1
	else:
		book[string] += 1

# 1. 개수 우선 
# 2.문자열 우선
d1 = sorted(book.items(), key = lambda x : (-x[1], x[0]))
print(d1[0][0])

# n = 1000
# O(n) == 1000
# O(nlogn) = 9000
#
# O(1)

# O(log n)

# O(n)

# O(n log n)

# O(n^2)

# O(n^3)

# O(2^n)

# O(n!)