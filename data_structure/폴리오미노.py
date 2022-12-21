# 문제분석

# 일단 보드판이 주어진다고 한다면
# 내가 가지고 있는 폴리오미노 AAAABB 로 덮어야 한다
# 문제는 이걸 덮는게 중요한건
# 내가 가지고 있는 폴로오미노 개수로 덮을 수 있냐이다


# replace 함수를 사용하지 않고 푼 코드

string = input()

a, b, cnt, ans = "AAAA", "BB", 0, ""
for i in range(len(string)):
	if string[i] == "X":
		cnt += 1
	elif string[i] == ".":
		if cnt == 4:
			ans += a
		elif cnt == 2:
			ans += b
		ans += string[i]
		cnt = 0
	if cnt == 4:
		ans += a
		cnt = 0

if cnt == 4:
	ans += a
elif cnt == 2:
	ans += b


if len(string) != len(ans):
	print(-1)
else:
	print(ans)



# replace 함수를 사용하면 왼쪽부터 해당하는 문자열을 찾아서 치횐해준다
# board = input()

# board = board.replace("XXXX", "AAAA")
# board = board.replace("XX", "BB")

# if 'X' in board:
#     print(-1)
    
# else:
#     print(board)