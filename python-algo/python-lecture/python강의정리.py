# # # sep 는 문자열 사이에 들어가는 하나의 문자열
# # # 따라서 구분문자임
# # # 공백을 포함할 수 있음
# # print("우리", "학교", "화이팅", sep=' ')


# # # end는 문자열의 끝에 붙게 되는 문자임
# # # end도 공백문자가 포함될 수 있음
# # print("우리 학교", "나이스", end = " good")


# # # 입력함수는 input()
# # # input("입력하세요 : ")
# # # 함수안에 문자열을 지정해줄 수 있고, 생략해줄 수 있음
# # # 단 input함수로 입력받게 되는 모든 값들은 전부 문자열임
# # # 따라서 숫자를 입력한다고 하더라도 input()함수를 통해서 입력을 받았기 대문에
# # # 문자열로 받게 됨

# # # 만약 입력받은 값은 문자열이지만 int, float으로 전환하고 싶다고 한다면
# # # int(input()), flota(input())
# # # 원하는 데이터 타입으로 변환 시켜주면 가능함.

# # # c-style formatting
# # # format, f-sstring
# # # 문자열에 변수의 값을 넣을 수 있는 방법이
# # # 총 3가지 졵하는데
# # # 1. c스타일이라고 한다면 c에서 pritnf("%d", a)
# # # 이렇게 형식지정자를 지정해서 값을 출력할 수 있었다.
# # # 따라서 이런 형식지정자를 사용해서, 값을 출력할 수 있다.

# # apple = "I eat %d apples" % 4
# # print(apple)

# # # 이렇게 형식지정자를 사용해서 값을 대입해서 넣어줄 수 있고
# # number= "five apple"
# # day = 1


# # one = 'c'
# # bear = "What is that %s, %d, %c" % (number, day, one)

# # # c-style은 따라서 형식지정자를 이용해서, 변수를 바인딩 시키는 방식이다.
# # # 정수 문자열, 문자 float, 똑같이 출력이 되는것을 알 수 있다.

# # a = "%02d" % 1
# # print(a)


# # # 이런게 c-style이고
# # # format은 .format()함수를 사용해서 데이터를 바인딩 시키는 방식이다.
# # str1 = "name:  {}, age: {}".format("Kim", 45)

# # # 괄호안에 있는 값이 순차적으로 들어가게 된다.


# # str2 = "name : {}, grade: {}".format("taesun", "A")
# # print(str2)

# # # 혹은 인덱스 번호를 지정해줄 수 있다.
# # str2 = "name : {0}, grade: {1}".format("taesun", "A")
# # print(str2)

# # # 혹은 인덱스 번호를 지정하고 싶지 않거나, 괄호에 아무것도 넣고 싶지 않다면,  키워드를 사용해서 넣을 수 있다.
# # str2 = "name : {name}, grade: {grade}".format(name="taesun", grade="A")
# # print(str2)
# # str2 = "name : {grade}, grade: {name}".format(name="taesun", grade="A")
# # print(str2)

# # # 이렇게 키워드를 지정해서라도 값을 지정할 수 있고, 자리가 바뀌어도 키워드에 지정되어 있는 값은 정해져 있기 때문에
# # # 키워드값에 따라 정해진다.


# # # 왼쪽으로 정렬을 할건데 < , n칸을 기준으로 왼쪽으로 정렬해라
# # # 그렇게 정렬하고 난뒤 왼쪽에서부터 값을 채운다.
# # print("'{0:<20}'".format("hi"))
# # # 20칸을 기준으로 오른쪽으로 정렬할거고 그때 값을 넣어라
# # print("'{0:>20}'".format("hii hgia w"))


# # # nice를 출력하기 위해서 ^ 가운데 10칸을 기준으로 정렬을 수행한뒤 작성해
# # print("'{0:^10}'".format("nice"))

# # # 이렇게 하면 2칸을 확보하고, 오른쪽으로 정렬한다. 이후 한자리면 0을 두자리부터는 적지 않는다.
# # print("'{0:>02}'".format("10"))

# # # 이것은 앞에 있는것은 format()함수를 사용하고 있기 때문에
# # # index를 지정하고 있음을 알 수 있고, 인덱스 0번에 3.141592 값이 들어있는 것을 알 수 있다.
# # # 이후에 정렬은 존재하지 않고 0으로 되어 있기 때문에 0칸 확보한다. 이후
# # # 소수점 이하를 4자리로 제한한다.
# # print("{0:0.4f}".format(3.141592653)) 
# # # 마찬가지로 index는 0을 가르키고 있고, 12칸을 확보하라는 얘기가 되며
# # # 소수점 이하 4자리 까지 출력하라고 하고 있다.
# # print("{0:12.4f}".format(3.141592653))
# # # 숫자 + str은 둘주 ㅇ하나를 변경해주어야 한다.
# # # int -> str
# # # str -> int 로
	
# # # 백슬래시를 해석하기 위해서 \ 역슬래시를 하나더 추가했고
# # # 만약  백슬래시를 해석하지 않게 하려면
# # # r을 넣어주면 된다.
# # rs = 'c:\\newdata\\test'
# # rs = r'c:\\newdata\\test'

# # 리스트와 튜플의 가장 큰 차이점은
# # 리스트는 추가나 수정이나 삭제가 가능하다는 점이지만
# # 튜플은 추가나 수정이나 삭제가 되지 않는다.

# # 딕셔너리 같은 경우는 key의 중복이 있을 수없다.
# # 딕셔너리가 키와 값으로 이루어진 자료형이기 때문에 key 값을 설정할 수 있는데
# # 이때 키 값은 중복될 수 없고 list를 키로 사용할 수 없다.

# # import 모듈

# # 모듈이라고 하는것은 함수 또는 클래스들의 집합인데
# # 모듈을 불러오려면 해당 모듈이 같은 디렉터리에 존재해야한다.
# # 또한 모듈을 불러왔을때는 모듈.함수 이런식으로 사용해야 한다.
	
# # from을 사용하게 되면 모듈이름을 사용해서 함수를 실행시킬 필요 없으며
# # from 모듈이름 import 함수
# # 모듈들을 담고 있는 패키지를 찾아서 넣어줄 수 있다.
# # # 이런식으로 game패키지 안에 sound패키지 안에 increase모듈을 불러와서
# # # 해당 모듈과 관련된 함수를 가져올 수 있다.
# # from game.sound.increase import soundincrease


# # def func(a, b):
# # 	x = a*2
# # 	y = b*2
# # 	return x, y

# # # 현재 x, y변수에 Func() 함수 호출결과를 
# # # x, y로 반환하고 있다. 
# # # 하지만 반환을 받는 쪽에서는 x, y를 언패킹형식으로 받으려고 하고 있다.
# # # 함수는 값을 하나로만 반환하게 되는데 어떻게 두개의 값에 값을 넣을 수 있을까
# # # 파이썬은 함수가 리턴하는 값을 튜플로 묶어 처리하게 된다.
# # # 따라서 튜플의 특성상 변수를 언패킹해서 사용할 수 있다.
# # x, y = func(4, 5)
# # print(x, y)


# # 만약 함수에 여러개의 인수를 넘겨주게 된다면
# # 파이썬에서 함수의 인수들은 위치가 중요하다 따라서 이를 위치인수라고 우리는 표현하게 되고
# # 위치인수를 기반으로 값을 전달하게 된다.s
# # 위치인수로 값을 전달하는 것은 결국 인수들의 위치가 중요하다는 것을 의미하기 때문에
# # 만약 의도한 인수의 위치에 다른 값을 넣게 된다면 의도하지 않은 결과가 나올 수 있다.
# # 따라서 인수의 위치를 잘 보고 값을 전달해야 한다.


# # 지역변수와 전역변수
# # 지역변수는 말그대로 스코프 중심의 변수인데
# # 파이썬에서 보통 함수안에서 사용되는 함수로 본다.
# # 따라서 함수 내에서만 사용되어지고 함수의 종료시 의미가없다.stdin

# # 반면 전역변수라고 한다면 함수 밖에서 선언된 값들이고
# # 이러한 값들이 전역변수로 있으면, 전역적으로 접근해서 사용할 수 있게 된다.
# # 마찬가지로 함수 내부에서도 이 전역변수에 접근할 수 있다.


# radius = 12
# def calc_circle_area():
# 	print(radius)
# 	area = 0


# # 만약 이렇게 함수에 인수로 값을 직접 전달하게 되면
# # 함수의 지역변수인 radius는 
# # 전달받은 인수를 값으로 가지게 되지만
# # 만약 값으로 전달 하지 않게 되면
# # 지정된 인수가 있는데 전달하지 않았기 때문에 missing 에러가 발생하게 된다.
# # 따라서 디폴트인수가 아니라면 반드시 위치인수기반으로 인수를 넘겨주어야 한다.

# # 그렇다면 만약 인수의 값은 넘겼지만 전역변수를 사용하려면 어떻게 해야할까
# # 만약 인수를 넘겨주는게 없다면 radius는 전역변수를 참조하게 된다 
# # 하지만 전역변수로 참조하게 되는건 값을 수정할 수 없기 때문에
# # global 키워드를 사용해서 해당 변수가 global 변수라는것을 알려주고
# # 값을 변경이 가능하게 만든다.
# calc_circle_area()



# # 키워드 인수를 지정할 수 있는데
# # 키워드 인수는 인수들의 이름을 키값으로하고 내가 넘겨주고자 하는 값을 value로 따지는 인수전달방식이다.
# # 만약 함수의 인자의 이름이 name, age, day 가 있다고 가정하면
# # name = 10, age = 20, day = 30
# # 이런 방식으로 인수를 넘겨주게 되면 인수의 위치가 바뀌더라도
# # 키워드의 키에다 값을 전달하는 것이기 때문에
# # 인수의 위치가 바뀌더라도 값을 정상적으로 전달할 수 있게 된다.


# # 만약 위치인수와 키워드인수가 있을때
# # 키워드 인수를 반드시 사용하게 하려면 어떻게 해야할까
# # 위치인수 , * , b, c,
# # 이런식으로 에스터리스크로 나눠주게 되면 에스터리스크 이후에 오는 값들은
# # 반드시 키워드로 값을 넘겨주어야 한다.

# # 위에서 잠깐 디폴트인수를 설명했었는데
# # 디폴트 인수라고 한다면 인수의 값을 전달하지 않더라도
# # 기본값을 가지는 인수를 말한다.
# # 따라서 전달할 인수 3개중 두개만 전달하게 되면
# # 1개는 전달하지 않았기 때문에
# # 정해진 인수에 값을 전달하지 않고 있으니 오류가 발생될 것을 예상할 수 있지만
# # 전달하지 않은 인수가 만약 디폴트 인수라면
# # 오류가 나지 않는다.
# # 왜냐하면 말그대로 인수가 전달되지 않을때 기본적으로 사용될 값으로 지정했기 때문이다.
# # 그럼 디폴트인수로 지정이 되어 있을때, 값을 전달하게 되면 어떤 값이 출력될까
# # 이때는 전달하게 된 값으로 초기화가 된다.
# # 따라서 전달한 값이 디폴트로 지정해둔 값보다 우선순위를 갖게 된다.

# # 만약 인수의 개수가 가변적이라고 한다면
# # 어떻게 처리할 수 있을까
# # 즉 해당 함수에 전달해야 될 인수으 개수가 예측이 되지 않느낟.
# # 그럴때는 가변인수를 사용하게 되는데

# # 말그대로 인수들의 개수가 가변적일때 사용하게 된다.
# # 그럴때 *scores, *args 등과 같이 인수의 이름앞에
# # 에스터리스크를 사용하게 되는데
# # 에스터리스크가 한개라면, 가변인수를 뜻하고
# # 에스터리스크가 두개라면, 키워드가변인수를 뜻한다.

# # 키워드 가벼인수도 결국 가변인수고 키워드로 받게 되는것을 의미한다.
# # 중요한건 가변인수는 *args로 받게 될때 튜플로 받게 된다는 것이다.
# # 따라서 함수내에서 언패킹해서 사용할 수 있다.
# # 만약 가변인수와 키워드인수를 혼용해서 쓴다면
# # 가변인수 -> 키워드 인수를 작성해야 한다.
# # *args, times=2
# # 이런식으로 작성을 해야 한다는 것이다.
# # 그러면 키워드가변인수로 인수를 넘겨주기 전까지의 값들은 전부 가변인수로 인지하고 가변인수에 값이 튜플로 넘어가게 된다는 것이다.

# # **kawargs 키워드 가변인수는 약간 독특한다.
# # 기본은 가변인수다. 가변적인 인수의 개수때문에 생겨나게 된것이고
# # 가변인수와의 차이점은 키워드 가변인수는 받은 인자들이 key:value형태로 넘어가게 된다는 것이ㅏㄷ.
# # 즉 키워드 가변인수 **kawargs 가 갖게 되는 데이터 자료형은 딕셔너리라는 얘기다.
# # 이 딕셔너리 자료형을 기반으로 데이터를 처리하게 된다.


# # 딕셔너리를 처리하는 방법중 dict.keys()
# # 키들만 뽑아낼 수 있고
# # dict.values() 값들만 뽑아낼 수 있다.
# # 만약 모든 요소들을 뽑아내려면 dict.items()

# # dict.items()는 튜플형태로 (key, value) 받환하게 된다.


# # 만약 가변인수와 키워드 가변인수를 받는 함수가 있다고 하자
# def test(*args, **kawargs):
# 	print(args, kawargs)


# test(1, 2, name="good", core="nice")
# # 아까는 키워드 인수를 사용하게 되면 인수의 위치가 바뀌어도 된다고 하지 않았나?
# # 키워드 인수를 사용하게 되면 그게 맞다.
# # 하지만 지금 사용하고 있는건 키워드 가변인수를 사용하고 있다.
# # 키워드인수중에서 인수의 개수들이 가변적이기 때문에 사용하고 있지만
# # 제약사항이 존재하는게
# # 위 처럼 가변인수, 다음에 키워드 가변인수형태로 사용하게 되면
# # 1은 가변인수로 받아지게 되고
# # name부터는 키워드 인수로 지정되어 있기 때문에
# # 키워드 인수로 판단이된다.
# # 그렇게 키워드 가변인수가 그 값을 받게되고
# # 나머지 값을 받으려고 하지만 이미 가변인수와, 키워드 가변인수 모두 전달했기 때문에
# # 이후에 값은 무시된다.
# # 따라서 이때는 가변인수, 키워드 가변인수 순서대로 작성해주어야 한다.
# test(1, name="good", 2, core="nice")


# # test의 결과는 1, 2는 튜플이된다. 가변인수기 때문에
# # 가변인수가 가지는 값은 튜플이 되고, 그 뒤부터는 키워드 가변 인수로 받게 된다.
# # 키워드가변인수로 받았기 때문에 key:value 값으로 이루어진 딕셔너리를 만들었다.


# Doc->string이라고 있는데 
# 이는 함수가 리턴하게될 값이 어떤 데이터 타입인지를 명시해주는것이다.stdin


# 파이썬에서는 람다라는 한줄짜리 축약형 함수가 존재하는데
# lambda x, y : 식
# 이런식으로 lambda 다음에 인수가 들어가게 되고, 해당 인수를 가지고 식을 수행하게 된다.

# 해당 람다 함수  같은 경우에는 축약형 함수라고 되어 있기 때문에
# 만약 어떤값을 반환하려면 return문이필요하다
# 하지만 어떠한 리턴문도 없는것은 람다 함수같은 경우 자동으로 리턴하기 때문이다.stdin
# 따라서 식 계산이 끝나게 되면 자동으로 식에 의한 값이 리턴되게 된다.stdin

# g = lambda x, y : x ** y

# 이런식으로 값을 넣을 수 있다.
# g(10, 20)
# print(g(2,3))

# 람다 같은 경우 if, while등은 허용되지 않는다.
# 만약 함수처럼 인수를 지정하지 않고 사용한다면
# a = (lambda x, y, z : x + y + z)(firstValue, secondValue)
# print(a)

# 파이썬에서 try, catch 문에서 raise 를 사용하게 되는데
# raise역할은 예외를 발생시킨다.



# import datetime

# # datetime 모듈에 date클래스가 존재하고 date.이후로 나가는 것들은 전부 함수단위임
# a = datetime.date(2023, 9, 27)
# print(type(a))
# 1. 파일을 여는것
# 2. 에러발생
# 3. 로그파일 작성
import datetime
# 파일을 열때 모드들이 존재하는데
# a는 파일에 내용을 추가하는 모드다.
# 만약 해당파일이 존재하지 않는다면 해당파일을 우선생성한다.
logfile = open("log.txt", "a")
sum = 0
while True:
	data = int(input())
	try:
		if data > 0:
			sum += 1
		elif data < 0:
			now = datetime.date.now()
			raise RumtimeError(f"{now} RumTimeError : ")
		elif data == 0:
			break
	except RumtimeError as e:
		print(e)
		log.write(str(e))
		continue # 종료하지 않고 계속 할 수 있게끔

logfile.close()