N = int(input())

result = [list(input()) for _ in range(N)]
# 8
# ..X..X..
# ..X..X..
# ..X..X..
# ..X..X..
# ..X..X..
# ..X..X..
# ..X..X..
# ..X..X..


# 가로 구하는 방법.

def width(result):
	zum_count = 0
	for i in range(len(result)):
		l_zum = []
		for j in range(len(result[i])):
			if result[i][j] == ".":
				l_zum.append(result[i][j])
			elif result[i][j] == "X":
				if l_zum.count(".") >= 2:
					zum_count += 1
					l_zum.clear()
				else:
					l_zum.clear()

		if l_zum.count(".") >= 2:
			zum_count+=1
						
	return zum_count

# 세로 구하는 방법

def height(result):
	hzum_count = 0
	for i in range(len(result)):
		h_zum = []
		for j in range(len(result[i])):
			if result[j][i] == ".":
				h_zum.append(result[j][i])
			elif result[j][i] == "X":
				if h_zum.count(".") >= 2:
					hzum_count += 1
					h_zum.clear()
				else:
					h_zum.clear()	
		if h_zum.count(".") >=2:
			hzum_count+=1
	return hzum_count


print(width(result), height(result))