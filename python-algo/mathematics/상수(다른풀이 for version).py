A, B = input().split()

first = ""
second = ""
for i in A:
	first = i + first
for i in B:
	second = i + second

print(first if first > second else second)