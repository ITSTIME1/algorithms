n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort()

dic = {}
for i in arr:
	dic[i] = 0


for i in arr:
	c = []
	for j in range(i, i+5):
		if j in arr:
			c.append(j)
	dic[i] = 5 - len(c)

sorted_dic = sorted(dic.items(), key = lambda x : x[1])

print(sorted_dic[0][1])