import datetime 

logFile = open("log.txt", 'a')
sum = 0
while True:
	input_data = int(input("정수를 입력해"))

	try:
		if input_data == 0:
			print(f'sum = {sum}'); break

		elif input_data < 0:
			error = f'[{datetime.datetime.now()}] 시각에 오류가 발생 되었습니다.\n'
			raise RuntimeError(error)

		else:
			sum += input_data
	except RuntimeError as e:
		# write로 작성되는 것은 반드시 문자열 이어야 함
		# 따라서 문자열이 아니라면 str()으로 치환해주는것이 필요
		logFile.write(str(e))
		continue

logFile.close()


# 이걸 with구문으로 바꿀 수 있음


# r 은 읽기모드임 만약 파일이 없으면 오류가 발생됨
# w 는 쓰기 모드임 파일이 있으면 지우고 새로 생성함
# a 추가모드임 fp가 파일 끝으로 이동하여 내용을 작성할 수 이씅ㅁ

# r+ 읽고 쓰기가 가능 단 기존파일이 존재한다면 덮어씌워버림 r+도 마찬가지로 파일이 없다면 오류가 발생됨
# w+ 읽고 쓰기가 가능. 기존파일 지우고 씀 팡리이 있으면 지우고 새로 생성함.
# a+ 마찬가지로 읽고 쓰기가 가능 기존파일 끝부터 추가함.

# r은 읽기 전용모드이며 파일이 없으면 오류가 나고 r+ 읽고 쓰긱 ㅏ가능한 모드이며 기존팡리이 존재한다면 기존파일을 덮어씌운다.
# 마찬가지로 파일이 존재하지 않는경우는 오류가 발생된다.
# w는 쓰기 모드이며 w+ 도 읽고 쓰기가 가능한데 파일이 존재하는 경우 삭제하고 다시 생성한다. 그리고 작성
# a 파일에 내용을 추가하는 모드인데 만약 파일이 존재하지 않는다면
# 새로 생성하고 추가한다. a+도 읽고 쓰기 모드가 가능한데 
# 기존 파일이 존재한다면 기존 파일에 덮어 씌우기 가 된다.



# 열려진파일은 반드시 사용하고 난 후에 닫아야 한다.
# 파일을 읽어올때 read()를 사용하게 되면 문자 통째로 읽어오게 된다.
# readline은 문자열 단위로 읽어온다.
# realines는 문자열 단위를 리스트로 한번에 제공한다.

# readlines가 개행문자 단위로 불러오기 때문에
# 개행문자가 없다면 개행문자가 마지막으로 처음으로 나오는 구간까지 읽게 된다.
f = open("log.txt", "r")
a = f.readlines()
print(a)
print(type(a))

# 이런식으로 자동으로 파일을 다 사용하게 되면 닫는것도 가능함.
with open("log.txt", "r") as outfile:



