
# '''

# 	namedtuple = 이름 붙은 필드를 갖는 튜플 서브 클래스를 만들기 위한 팩토리 함수다.
# 	deque = 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너.
# 	Counter = 해시 가능한 객체를 세는데 사용하는 딕셔너리 서브 클래스다.
# 	OrderedDict = 항목이 추가된 순서를 기억하는 딕셔너리 서브클래스다.
# 	defaultDict = 누락된 값을 제공하기 위해 팩토리 함수를 호출하는
# 	딕셔너리 서브 클래스
	
# 	namedtuple 에 들어갈 typename은 생성할 필드이름
# 	그리고 filed_names는 튜플이 갖는 필드들을 말하는데
# 	이게 바로 필드의 이름이됨 그래서 해당 필드의 이름을 가지고 
# 	접근이 가능함.

# 	['x', 'y'] 이렇게 리스트로 구분짓는게 가능하고
# 	'x y' 이런식으로 공백을 통해서 구분하는게 가능하고
# 	'x,y' 콤마를 통해서 구분하는것도 가능함.


# '''

# from collections import deque, Counter, OrderedDict, defaultdict
# import operator
# text = list("sausages")

# a = Counter(text)
# print(a)

# # # 파이썬에서 시퀀스라고 하면
# # 리스트, 튜플, range, 문자열이 있음

# # 리스트, 튜플, range, 문자열이 존재함
# text = "Manyoftile"
# # 이게 문자단위로 읽어버리는구나
# # 시퀀스 자료형의 개수대로 읽어버리네
# # 즉 문자열의 개수만큼 읽어 버린다는거네
# print(Counter(text))
# # 예제 처럼 하기 위해서는 split 공백으로 구분한거고
# # python3.5에서는 입력된 순서를 보장하지 않았음
# # 하지만 python3.6버전으로 업그레이드 되면서
# # 순서가 기본적으로 보장
# # 아마 python3.5에서는 딕셔너리의 순서를 보장하지 않았기 때문에
# # 순서를 보장하기 위한 방법을 사용했었나 보네

# d= OrderedDict()
# dd = {}
# dd['a'] = 100
# dd['b'] = 200
# dd['c'] = 300
# dd['d'] = 400

# d['a'] = 100
# d['b'] = 200
# d['c'] = 300
# d['d'] = 400


# for k, v in dd.items():
# 	print(k, v)

# print("\n")

# for k, v in d.items():
# 	print(k ,v)


# # 딕셔너리에 있는 값을 정렬하기 위해서 key 그리고 value에 따라서 정렬 기준을 잡을 수 있음
# a = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
# # 단 operator 패키지 모듈을 불러와서 사용해야함
# # 하지만 이걸 value값에 따라서 정렬 할 수 있음
# print(a)


# # sorted()만 하게 되면 하나의 새로운 리스트를 만들어서 주게 되는데
# # 만약 정렬을 유지한 상태에서 itesm()값을 바로 가지고 오고 싶다면

# # 이런식으로 사용이 가능함
# for k, v in OrderedDict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)).items():
# 	print(k, v)

# # defaultdict는 기본값으로 초기화한 딕셔너리를 생성할 수 있자나

# # 이렇게 하면이제 값은 0 으로 초기화함
# # 따라서 어떤 키값들이 공통적인 value를 가지고 있어야 한다면
# # defaultdict 사용하는것을 고려해볼 수 있음
# d = defaultdict(lambda : 0)

# # 이렇게 리스트를 갖게 할 수도 있음
# # 이런식으로 리스트를 초기화할 수 있다.
# d = defaultdict(list)
# print(d)


# for i in range(10):
# 	d[i].append(i+1);

# print(d)


# # 지금까지 배운것이 디큐, 딕셔너리, orderedict
# # defaultdict
# # list comprehesion

# arr = []
# for i in range(10):
# 	arr.append(i * 2)


# # 우 ㅣ문장을 바꿔보면
# arr = [i * 2 for i in range(10)]
# # 이라고 표현할 수 있음

# # 이렇게 참인 경우만 따로 넣어주는 것도 가능하고
# arr1 = [i for i in range(10) if i % 2 == 0]

# # 이런것도 가능함.
# # 하지만 보기엔 매우 불편함.
# arr2 = [i if i % 2 == 0 else -i for i in range(10)]

# arr3 = [c for c in range(4) for r in range(3)]


# # 이건 어떻게해석하냐면 앞에 있는 for문을 먼저보고
# c가 0 이면 c를 리스트에 저장하는데 이때 r이 3번 반복이자나
# 즉 4개의 원소를 반복하면서 3번씩 반복하라는거지

# for c in range(4):
# 	for r in range(3):
# 		arr.append(c)


# # 이걸 풀어쓰면
# # 이렇게 된다는거야
# arr = [c for c in range(4) for r in range(3)]

# # n * 3인거지
# # n번의 3번만큼 돌아버리니까
# # 3n
# # 이것도 마찬가지 그저 괄호만 씌웠을뿐 똑같음
# # 원소에 대해서는 4번 반복하고 그걸 내부에서 3번 반복하는거니가
# arr = [[c] for c in range(4) for r in range(3)]


# # 이거는 우선적으로 배열 하나를 만든다는 느낌이 강함
# # 즉 4개의 배열을 초기화하고 그걸 3번 반복한다는거니까
# arr1= [[c for c in range(4)] for _ in range(3)]

# # 이것과 같으니까
# for i in range(3):
# 	for j in range(4):
# 		arr1.append(j)


# arr = [[c for c in range(4)] for _ in range(3)]

# flat_arr = [i for row in arr for i in row]


# # 딕셔너리 컴프리헨션도 가능하 

# dict2 = {key:value for key,value in dic.items() if key == "good"}


# arr = [i for i in range(21) if i % 2 == 0]
# print(arr)

arr1 = [[1,2,3],[4,5,-1]]
arr = [i for c in arr1 for i in c if i > 0]
print(arr)

# enumerate tuple 반환 인덱스와 함께
e = enumerate(["a","b","c"])
print(e)
for i in range(3):
	print(next(e))

# 튜플로 반환하니까 언패킹 하면 되겠지
# enumerate는 리스트 튜플 string등을 인덱스와 반환할 수 있고
# 시작값을 정할 수도 있음.
for i, k in enumerate(["A","B","C"], start=2):
	print(i, k)

# zip은 객체를 묶어주는 역할을함 튜플로
# 이때 시퀀스들의 길이가 다를경우 가장 짧은걸 기준으로 봄
# 따라서 나머지 긴 쪽은 객체를 묶지 않음

# zip 끼리 묶기 위해서 시퀀스 자료형들이 필요
pairs = zip([1,2,3], ["A","b","C"])

num, letters = zip(*pairs)
# unzipping이라고 하는것은 결국 zip되어 있는걸 각각 푸는건데
# 문제는 이 각각 푸는것이 
# 튜플로 풀린다는것
print(num, letters)


# filter 는 시퀀스의 각 요소를 함수에 적용한 후
# 값이 True인 것만 묶어서 반환한다.

arr = [1,2,3,4,5,6,7,8,9]
f = lambda x : x % 2 == 0
# arr에 있는 원소들을 f함수에 적용
# 이후 True인 값만 리턴한다.
# 즉 true인 값만 리스트로 묶어서 리턴함
print(list(filter(f, arr)))

# 람다 식에 조건을 이런식으로 거는것도 가능하다는것.
f = lambda x : True if x % 2 == 0 else False
print(list(filter(f, arr)))

# map은 각 요소들을 함수에 적용해서 나온 결과값들을 맵객체로 반환하고
# filter는 각 요소들에 대한 값중 참인것만 즉 True인 것만 반환하게 됨

def countdown(n):
	while n > 0:
		yield n
		n-= 1



for x in countdown(10):
	print(x, end = ' ')

# countdown 은 iterator임
# iterator함수에 yield가 있어 함수를 호출할때마다 값을 반환해서 가지고옴

# 객체.__iter__()해도 값을 가지고 올 수 있음
# 혹은 next()

# 튜플에다가 컴프리헨션을 적용시키면 gerator객체가 만들어짐

# 리스트는 생성하지 않음
# 따라서 만약 튜프에다가 리스트 컴프리헨션 방식을 사용했다면
# 해당 객체를 출력하며녀 generator객체가 출력됨
g = (2 * x for x in arr)
# 여기에서 객체가 출력됨
print(g)

for i in g:
	print(i, end = " ")
# 하지만 재사용 안됨
# 따라서 리스트 컴프리헨션 방식의 제너레이터를 사용할 경우
# yield를 사용하지 않아도 yield와 같은 효과를 내게 됨
# 하지만 리스트는 따로 만들지 않고
# 값을 반환해주는 용도이므로 1회성임
for i in g:
	print(i, end = " ")


# 클로우저라고 하는것은
# 외부함수에서 내부함수를 정의함
# 이후 외부함수는 내부함수 객체를 반환하는 형태가 클로저임


# 외부함수에서 함수를 받아주고
# 내부 함수를 호출하고 있는 클로저 형태임
# 이때 decorated()는 실제 수행하는 인수이고
# 호출하는 함수의 인자와 동일하게 설정해야함
def time_decorator(func):
	def decorated():
		start = time.time()
		func()
		end = time.time()
		print()
	return decorated



# assert는 디버깅 보조도구임
# assert 표현식, 진단메세지가 나옴


# assert price >= 0
# 즉 진단메세지는 값이 표현식이 거짓일때
# AssertionError로 표현함
# AssertionError를 표출 함

assert isinstance(10.2, int), 'Expected int'






