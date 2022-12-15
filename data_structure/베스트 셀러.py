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
# 시간 복잡도 인데 아래로 갈수록 더 오래 걸린다
# 특히 위 알고리즘 같은경우 O(n + nlogn) 의 시간만큼 걸리게 되는데 이거 자체가 시간이 굉장히 오래걸리게 된다
# 때문에 가능한 시간복잡도를 줄일 수 있는 방향으로 코딩하는게 굉장히 좋을거 같다
# O(1)

# O(log n)

# O(n)

# O(n log n)

# O(n^2)

# O(n^3)

# O(2^n)

# O(n!)