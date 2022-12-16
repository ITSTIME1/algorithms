# 문제 분석

# while 의 범위를 어떻게 결정 해주냐에 따라 진짜 어마어마 하네
# while True 로 하면 이런 문제는 무조건 TLE

string = input()
find = input()
index, word = 0, 0
while index <= len(string) - len(find):
	if string[index:index+len(find)] == find:
		index += len(find)
		word += 1
	else:	
		index += 1 
print(word)