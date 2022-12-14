# 문제분석


# 대문자 10문자로 이루어진 문자열이 있고
# 반지는 문자열의 시작과 끝이 연결된 형태로 문자가 새겨져있ㄷ
# 거꾸로 읽지 않는다

# 해당 문자열을 포함한 반지가 몇 개인지 발견하는 프로그램 작성
# ABCD
# 3
# ABCDXXXXXX
# YYYYABCDXX
# DCBAZZZZZZ

# # ABCD 라는 문자열을 찾아야 하는데
# # 일단 첫번째 문자열에선 ABCD 하나가 보이고 ans += 1
# # 두번재 문자열에 ABCD 가 하나 보이고 ans += 1
# # 세번째에는 DCBA 인데 문자열이 내가 구하고자 하는 문자열이랑 다르므로 x

# # 그럼 첫 예제는 이렇게 2개의 반지가 포함되어 있고

# XYZ
# 1
# ZAAAAAAAXY
# # 이건 예제 출력이 1개가 나온 예제인데
# # 거꾸로 읽지는 않지만 정상적으로 이어졌을때
# # 첫문자와 끝문자가 이어져 있다고 했으니까
# # XY에서 문자열이 끊겼지만 반지가 원이라는걸 생각해보면
# # XY-Z 로 연결이 된다는걸 알 수 있다
# # 때문에 해당 문자열도 XYZ 가 있다라는걸 알 수 있다 ans += 1



# PQR
# 3
# PQRAAAAPQR
# BBPQRBBBBB
# CCCCCCCCCC


# # 이 예제는 PQR 을 찾아야 하는데 보다싶이 첫 문자열에
# # PQR이 두개가 있는걸 확인할 수 있다 하지만 문제에서 원하는건
# # 단어가 몇개 포함되어 있는지를 원하는게 아니라
# # 내가 찾고자 하는 단어가 반지내에 얼마나 있는지를 원하는게 아니라
# # 해당 반지가 해당 문자열반지에 포함이 되어 있다라면
# # 1개든 2개든 3개든 상관없이 포함이 되기만 한다면
# # ans += 1 올릴 수 있다라는 얘기가 된다
# # 두번째 문자열 예제에서도 PQR이 보이기 때문에 ans += 1
# # 세번째 문자열 에서는 없기 때문에 올리지 않는다 
# # 결국엔 2개가 된ㄷ 

# # 그럼 문자열이 연결되어 있다라는게 중요한건데 


# # 그럼 첫문자가 해당하는 지점을 찾고..
# # 문자열의 길이만큼 더했을대 해당 문자가 나오는지 봐야 하나
# yzx
# 9 10 11
#   +0+1 = XYZ 

find_string = list(input())
nl = len(find_string)
ring = int(input())

arr = [input() for _ in range(ring)]

total = 0
for i in arr:
	ans = 0
	if "".join(find_string) in i:
		ans += 1

	if ans >= 1:
		total += 1
	else:
		ma = ""
		pos = 0
		for j in range(10):
			if find_string[0] == i[j]:
				pos = j 
	
		for c in range(nl):
			re = pos+c
			if re < nl:
				ma += i[re]
			else:
				ma += i[re % 10]

				
		if ma == "".join(find_string):
			total += 1
print(total)

# def other_solve():
		# ma = ""
		# pos = 0
		# for j in range(10):
		# 	if find_string[0] == i[j]:
		# 		pos = j 
	
		# for c in range(nl):
		# 	re = pos+c
		# 	if re < nl:
		# 		ma += i[re]
		# 	else:
		# 		ma += i[re % 10]

				
		# if ma == "".join(find_string):
		# 	total += 1
		# print(total)
	

# def solved():
	# ma = []
	# pos = 0
	# for j in range(10):
	# 	if find_string[0] == i[j]:
	# 		pos = j 
	
	# for c in range(nl):
	# 	re = pos+c
	# 	if re < nl:
	# 		ma.append(i[re])
	# 	else:
	# 		ch = re % 10
	# 		ma.append(i[ch])
	
	# if "".join(ma) == "".join(find_string):
	# 	total += 1
