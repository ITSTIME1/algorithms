T = int(input())

for _ in range(T):
	n = int(input())
	soju_list = []
	school_list = []
	for i in range(n):
		s, soju = input().split()
		soju_list.append(int(soju))
		school_list.append(s)
	
	c = soju_list.index(max(soju_list))
	print(school_list[c])


