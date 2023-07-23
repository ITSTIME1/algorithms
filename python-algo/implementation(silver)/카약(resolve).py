# 문제분석



# 뒤에서 부터 검사해보면서

# isdigit() 으로 숫자를 판별한다음
# 그 숫자의 거리를 저장해두고
# 만약 다음 숫자의 거리가 이전 숫자의 거리보다 크다면 다음 순위로 지정해주고

# 만약 이전 숫자의 거리와 다음 숫자의 거리가 동일하다면
# 같은 등수로 측정해준다

# 이때 1열씩 확인할때마다 숫자가 3개의 카약의 길이가 존재하기 떄문에
# 열마다 같은 수가 존재할 수 있다
# 맨뒤에서부터 검사하기 때문에
# 그다음 열을 검사할대 이미 dic 에들어가 있는 경우는
# 취급하지 않는다
# 만약 dic 에 저장되어있지 않은 카약이라면
# 위의 조건들 대로 코딩하면 등수를 매길 수 있을거 같다


r, c = map(int, input().split())


ma = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(r):
	kac = input()
	ma[_] = kac

# f, s를 제외하고 해도 상관은 없을거 같긴하다
# 그냥 숫자만 판별하는거기 때문에
# 뭐 상관은 없을거 같긴한데


dic = {}
pre, index = 0, 1
for i in range(len(ma[0])-1, -1, -1):
	for j in range(r):
		# 현재 문자가 = 숫자 and 그 숫자가 hash에 입력되어 있찌 않다면
		if ma[j][i].isdigit() and ma[j][i] not in dic:
			# 만약 현재 위치가 이전의 있던 위치와 다르다면
			#  만약 현재 위치가 이전 숫자의 위치와 같다면
			# 1: (6, 2) 3: (8, )
			if pre != i:
				dic[ma[j][i]] = index
				pre = i
				index += 1
				continue
			elif pre == i:
				dic[ma[j][i]] = index-1

		# 현재 문자가 = 숫자 and 그 숫자가 hash에 입력이 되어있다면 패스
		if ma[j][i].isdigit() and ma[j][i] in dic:
			continue
			
for i in range(1, 10):
	print(dic[str(i)])