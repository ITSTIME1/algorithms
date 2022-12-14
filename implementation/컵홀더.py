N = int(input())
arr = input()
c = arr.count("LL")
if arr.count("LL") >= 2:
	print(len(arr) - arr.count("LL") + 1)
else:
	print(N)
