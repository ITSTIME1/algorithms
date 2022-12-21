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



# 이거랑 차원이 다른 걸 보여주네 진짜 시간 초과 안나려면 이것도 신경 써주어야 겠다
# 개인적으로 "".join 에서 시간초과가 날줄 알았는데 오히려 범위를 지정해준 것만으로도 이렇게 시간이 줄여진다는건 또 처음 알았다
# True 랑 시간 복잡도 차이가 크게 나나 보다
# while True
