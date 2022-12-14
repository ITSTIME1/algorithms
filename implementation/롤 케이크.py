arr = [_ for _ in range(1, int(input())+1)]
result = [0] * (len(arr)+1)
leng = []
ct = []
for i in range(int(input())):
	p, k = map(int, input().split())
	leng.append(k-p)
	cnt = 0
	for j in range(p, k+1):
		if result[j] != 0:
			pass
		else:
			result[j] += 1
			cnt+=1	
	ct.append(cnt)

c = max(leng)
l_ch = []
for j in range(len(leng)):
	if leng[j] == c:
		l_ch.append(j)
print(l_ch[0]+1)
print(ct.index(max(ct))+1)
# O(n2 + 2n)