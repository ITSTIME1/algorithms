import sys
input = sys.stdin.readline 


n, m = map(int, input().split())

grade = list(map(int, input().split()))



result = []
for i in range(m):
	s = list(input().strip().split())
	number = int(s[0])
	other = s[1:]
	
	s = [number, 0]
	# 성적 입력
	for j in range(len(other)):
		# 맞았다면
		if other[j] == "O":
			s[1] += grade[j]

	result.append(s)


print(*sorted(result, key=lambda x : (-x[1], x[0]))[0])

