import datetime

# python에서는 파일을 여는 모드가 존재하는데
# 파일을 여는 모드라는 것은 해당 파일을 어떻게 처리할것인지를
# 정의하는 모드라고 할 수 있다.
# 만약 읽기 모드라면 읽기 전용모드로만 사용할 수 있고
# 만약 쓰기 모드라면 쓰기 모드로 열 수 있지
# 만약 해당 파일을 읽기 모드로 열고 싶다고 한다면 r을 모드에 넣어주면 되고
# 만약 쓰기 전용 모드라고 한다면 w를 넣어주면 되는거지
# 만약 읽기모드로 파일을 열려고 했는데
# 해당 파일이 존재하지 않는다면 에러가 발생해 r모드는
# w같은 경우는 쓰기 전용 모드인데
# 파일이 있으면 지우고 새로 생성해
# 따라서 해당 파일이 이미 존재하는 파일이라고 한다면
# 지우고 다시 생성한다는거야
# a같은 경우는 파일에 내용을 추가하는 모드야
# a모드 같은 경우는 파일에 내용을 추가하는 모드니까
# 해당 파일이 존재하지 않으면 일단 해당 파일을 생성해
# 생성하고 작성하는거지
# 만약 해당 파일이 존재한다면 내용을 추가하는 거겠지


# logfile = open("log.txt", 'a')

# outfile = open(r"/Users/itstime/name/newfile.txt", "w")

# # 파일을 읽기모드로 연다.
# readfile = open("/Users/itstime/afaf.txt", "r")
# # 통째로 읽어 문자열로 변환한다.
# # 해당 파일에 적혀 있는 문자열을 통째로 읽어들여서
# # 문자열로 반환한다.
# lines = readfile.read()
	
# # 이건 한 라인씩 문자열로 읽어서 반환하게 된다.
# # 오른쪽 끝 공백을 제거해주고
# # 즉 read()는 내용 전부를 읽지만
# # readline()같은 경우는 문자열 한단씩 읽어와서 보여주는것
# # 또한 이 readline()함수 같은 경우는 한 라인씩 읽어와서
# # 리스트로 반환해 그렇기 때문에 반복해서 어떠한 작업들을 할 수 있지
# eachline = readfile.readline().rstrip()

# # readline()이 리스트로 반환하기 때문에 for문으로 각 문자열들을 가지고올 수 있는거지
# for line in eachline:
# 	print(line)
# # 반드시 닫아주고
# eachline.close()

# # 지금처럼 파일을 읽거나 쓰거나 수정하는건 좋은데 
# # 문제는 파일을 수동으로 닫아야한다는건 변한없이 귀찮은 부분이야

# # 따라서 해당 부분을 자동으로 해줄 수 있는 with구문을 함께 사용하면 되는거지
	
# # 이 with구문은 해당 루트에 존재하는 파일을 w모드로 작성모드로 불러와서
# # outfile이라는 변수로 다루게 되는데
# with open("/Users/itstime/newFile.txt", 'w') as outfile:
# 	# outfile변수를 이용해서 write()로 작성모드기 떄문에
# 	# 작성을 할 수 있다.
# 	# with구문을 사용했기 때문에 자동으로 닫혀이기에 따로.close()문을 추가할 필요가 없다.
# 	for i in range(1, 11):
# 		outfile.write()


# # 읽기 모드로 열고
# with open("score.txt", 'r') as file:
# 	# readline 함수를 이용해서
# 	# 문자열을 한라인씩 읽어와서 리스트로 변환
# 	lines = file.readline()
# 	for line in lines:
# 		# 공백을 제거해주고
# 		line.rstrip()
# 		# 불러온 Line을 구성하는 단어들로 구분하고 싶기 떄문에
# 		# 공백으로 구분하면된다.
# 		# split()함수를 사용하게 되면
# 		# split()함수 내부에 지정한 구분 방식을 통해서
# 		# 구분하게 되고 
# 		# 그렇게 구분한거는 리스트로 반환된다.
# 		words = line.split()
# 		# 이거는 map()함수를 사용해서 words에 두번째 인덱스들을 int형으로 변환한 뒤 리스트로 만들어주고 잇따.
# 		scores = list(map(int, words[2:]))
# 		# 그렇게 변환한 scores들을 하나씩 가지고 와서
# 		total = 0
# 		for score in scores:
# 			total += score

# 		# 합을 평균내주면 mean이 나오게 되고
# 		mean = total / len(scores)
# 		# 불러온 Line을 출력해주면서
# 		# 마지막 문자열에 추가할것은 공백이다.
# 		print(line, end = " ")
# 		# 합을 출력해주고 있고, mean은 평균을 출력하고 있으며 mean에 대해 소수점 둘째짜리 까지 출력할 수 있음
# 		print(f"total = {total} mean = {mean:.2f}")

# 	# 모든 lines에 대한 작업이 끝났다면
# 	# 원래는 with구문을 사용하지 않았다면 직접 close()해주어야 했지만
# 	# with구문을 사용했기 때문에 close()를 직접해줄 필요가 없다.





class Circle(Parent):
	def __init__(self, radius = 1):
		# underbar 두개는 private한 변수임
		# 부모 클래스를 초기화
		# 만약 인자를 넘겨주게 되면
		# 부모의 인자로 넘어가는 부분을 초기화
		super().__init__(name)
		self.__radius = radius

	def getRadius(self):
		# getter메소드로도 __ private한 변수를 넘겨주어야함.
		return self.__radius


a = Circle(30)
print(a.getRadius())









