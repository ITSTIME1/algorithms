
# 7일에만 일을한다고 했을떄도
# 즉n-1 일에 일을 한다고 했을때도
# 상담하는데 걸리는 횟수가 1일이라면
# 그 상담은 가능하기에
# 해당 액수도 포함해주어야 한다



n = int(input())

sang = []
for i in range(n):
	t, p = map(int, input().split())
	sang.append((t, p))

total = []
for i in range(n):
	s = sang[i]
	pay = 0
	if i+s[0] <= n:
		s = i+s[0]
		pay += sang[i][1]
		second = True
		for j in range(s, len(sang)+1):
			c = j + sang[j][0]
			if c <= n:
				second = True 
				pay += sang[j][1]
				for k in range(c, len(sang)+1):
					while k <= n:
						if k + sang[k][0] <= n:
							pay += sang[k][1]
							total.append(pay)
							pay -= sang[k][1]
						else:
							break
			else:
				second = False
				continue
		if second == False:
			total.append(pay)

print(total)