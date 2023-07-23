import sys
input = sys.stdin.readline

# A로 먼저 채우고 B로 채우는데
# A로 채우지 못한것들 중에서 B로 채울 수있다면 B로 채우고
# B로도 채우지 못한다면 그건 폴리오미노를 만들 수 없으므로 -1
# X를 제외한게 들어온다면 그건 "." 밖에 없음 

# 따라서 . 들어오면 새로운 문자열에 계속해서 더해가주고
# .들어오기 전까지 x를 저장해두었다가
# .들어오는 시점에서 x를 // 4 A로 채울 수 있을 만큼 채우고
# 못채우는 게 들어올 수 있음 XXX XX 그랬을때 2로 채울 수 있을 만큼 채운다
# 만약 2로 채우고도 2의 개수만큼 채운다 근데 여기서 검사해주어야 하는게
# 2로 나누어서 떨어져야 한다는 것이다. 따라서 2로 나누었는데 떨어지지 않는다면 그 시점에서 만들 수 없는 것이므로
# 폴리오미노를 만들 수 없다.

string = list(map(str, input().strip()))

	
s = ""

# 문자열ㅇ
new = ""
flag = True
for i in string:
	if i == ".":
		new += "AAAA" * int(len(s) // 4)
		s = s[len(s) // 4 * 4:]
		if len(s) % 2 == 0:
			new += "BB" * int(len(s) // 2)
		else:
			print("-1")
			s = ""
			flag = False
			break
		s = ""
		new += "."
	else:
		s += i

if s != "":
	new += "AAAA" * int(len(s) // 4)	
	s = s[len(s)//4 * 4:]
	if len(s) % 2 == 0:
		new += "BB" * int(len(s) // 2)
	else:
		print("-1")
		flag = False
	
if flag:
	print(new)