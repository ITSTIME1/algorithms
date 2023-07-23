# 문제분석

# dic 될거 같은데
# 4방위 해당 직사각형으
# B 일때가 좀 다르네 방향에 따라서 동서남북이 정해지기 때문에

# 컴공에 전화
# 복학신청 여부
# 수강지도 상담교수 누군지
# 학과내 전과도 가능한지


# 국장에전화
# 등록금 납부되어 있는지
T = int(input())

dic = {}
vector = ["북", "동", "남", "서"]
c = 0
for _ in vector:
	dic[_] = 0

def change(i):
	global c
	if i == "L":
		c -= 1
		if c < -4:
			c = -1
	else:
		c += 1
		if c > 3:
			c = 0

def dic_init(dic):
	for i in dic:
		dic[i] = 0
	c = 0

def solve(strc):
	global c
	for i in range(len(strc)):
		if strc[i] == "L" or strc[i] == "R":
			change(strc[i])
		else:
			if vector[c] == "북" and strc[i] == "F":
				dic["북"] += 1
			if vector[c] == "북" and strc[i] == "B":
				dic["남"] += 1
			if vector[c] == "서" and strc[i] == "F":
				dic["서"] += 1
			if vector[c] == "서" and strc[i] == "B":
				dic["동"] += 1
			if vector[c] == "동" and strc[i] == "F":
				dic["동"] += 1
			if vector[c] == "동" and strc[i] == "B":
				dic["서"] += 1
			if vector[c] == "남" and strc[i] == "F":
				dic["남"] += 1
			if vector[c] == "남" and strc[i] == "B":
				dic["북"] += 1

	ns_l, ew_l = [], []
	for i in dic.items():
		if i[0] == "북" or i[0] == "남":
			ns_l.append(i[1])
		else:
			ew_l.append(i[1])
	f, b = max(ns_l), max(ew_l)

	dic_init(dic)
	
	return f*b


for _ in range(T):
	string = list(input())
	c = solve(string)
	print(c)