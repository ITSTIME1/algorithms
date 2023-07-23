T = int(input())


for i in range(T):
	a, b = list(input().split(" "))
	a_l, b_l = list(a), list(b)
	a_l.sort()
	b_l.sort()
	if "".join(a_l) == "".join(b_l):
		print("%s & %s are anagrams." % (a, b))
	else:
		print("%s & %s are NOT anagrams." % (a, b))
