# 문제분석


# 보아하니.. hashmap?

# 압수당한 여학생들을 숫자로 매겨 리스트를 작성한데
# 그리고 압수한 귀걸이 뒤쪽에 여학생 번호와 a, b를 적어두었떼

# 정규일과와 방과후가 끝나면 받아간다고 한다
# 근데 이때 받아가지 못한 학생의 소녀의 이름을 알려주세요

# 압수당한 여학생의 수 = 압수당한 사람들의 수가 주아진다는것

# 번호가 여학생 이름 리스트와 순서가 일치한다
# 즉 1번 은 리스트의 처음 betty 라고 본다

# 번호가 처음 등장하는 것은 압수 되었음을
# 두번째로 등장하는 것은 돌려받았음을 의미 한다

# 리스트의 크기가 2개이상이면 바뀐거네
# 만약 두번째가 없었다면 리스트가 한개일 거니까




ans = []
while True:
	n = int(input())
	
	if n == 0:
		break

	dic = {}
	for i in range(n):
		girl = input()
		if girl not in dic:
			dic[girl] = [int(i), []]

	# {'Betty Boolean': [0, []], 'Alison Addaway': [1, []], 'Carrie Carryon': [2, []]}	
	for i in range((2*n)-1):
		num, al = input().split()
		for j in dic.values():
			if j[0] == int(num)-1:
				j[1].append(al)
	
	for k in dic.items():
		if len(k[1][1]) != 2:
			ans.append(k[0])

index = 1
for i in ans:
	print(str(index) + " " + i, end = "\n")
	index+=1

# ('Betty Boolean', [0, ['B', 'A']])
# ('Alison Addaway', [1, ['A']])
# ('Carrie Carryon', [2, ['B', 'A']])
# ('Helen Clark', [0, ['B']])
# ('Margaret Thatcher', [1, ['B', 'A']])

