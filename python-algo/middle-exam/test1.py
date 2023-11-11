# f = open("score.txt", "r")

# lines = f.readlines()

# for line in lines:
# 	# 맨끝 개행문자 제거
# 	line = line.rstrip()
# 	# 받아온 문장을 리스트로 변환
# 	# 공백을 기준으로
# 	words = line.split()
# 	# 인덱스 기준 2부터 끝까지 전부스코어
# 	scores = words[2:]

# 	total = sum(scores)

# 	mean = total / len(scores)

# 	# total과 평균을 출력하는데 평균은 두자리까지만 나타냄
# 	print(f'{total}, {mean:.2f}')


# with open("scores.txt", "r") as file:
# 	file = readlines()

# 	for line in lines:
# 		line = line.rstrip()
# 		words = line.split()
# 		scores = words[2:]
# 		total = sum(scores)
# 		mena = total / len(scores)

# 		print(f'{total}, {mena:.2f}')


# 자동으로 파일 닫힘

# 파이썬에서 클래스를 사용할때 
# 모든 필드는 self로 참조하며, 모든 함수내에 있는 메소드는
# 첫번째는 반드시 self임

# private 하게 만든다면 self.__name
# 외부에서 접근을 하지 못함

# 클래스 변수라고 하는 것은
# 모든 객체들에 의해 공유되는 변수임
# 클래스 이름.count이런 식으로 사용함.

# 상속을 하게 될때는 반드시
# init에 첫번째 문장에 부모의 생성자를 초기화 해주어야함
# 부모가 없는데 상속을 어케 할까 그치?
# 그렇기 떄문에 부모를 먼저 만들어주어야겠지

class Parent():
	def __init__(self, name):
		self.__name = name


	def __str__(self):
		return "good"

class Child(Parent):
	count = 0
	def __init__(self, grade='A', name="default"):
		# 이렇게 부모를 먼저 만들어주는거지
		super().__init__(name)
		self.__grade = grade
		Child.count+=1;

	def getGrade(self):
		return self.__grade

	def __str__(self):
		return "nice"




a = Child()
print("%d, %c\n" % (a.count, a.getGrade()))
c = Child("B")
print("{count}, {grade}".format(count = a.count, grade = a.getGrade()))
# __str__()은 오브젝트 메서드인데 모든 클래스는 오브젝트를 상속받고 있기 때문에
# 결국 부모 메서드를 재정의한 오버로딩 하게 된 것이다.
# 이렇게 오버로딩하게 되면 어떤 객체의 str함수를 호출하게 될 것인지를 예측해 볼 수 있는데
# 이런 경우 자식부터 호출하게 된다. 다형성의 특징이지.
# 부모의 메서드가 먼저 호출되게 되는 다형성의 특징
print(Child().__str__())
