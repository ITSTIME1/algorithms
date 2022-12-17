
dic = {0: 'zero', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}


m, n = map(int, input().split())

arr = [i for i in range(m, n+1)]

ch = []
for i in arr:
	c = list(str(i))

	word = ""
	for j in c:
		word += dic[int(j)]
	ch.append((word, i))

ch.sort(key = lambda x: x[0])

s = [i[1] for i in ch]

for i in range(0, len(s), 10):
	print(*s[i:i+10], end = "\n")