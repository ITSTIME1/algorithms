# collections 모듈은 리스트, 튜플, 딕셔너리, 셋 등을 확장하여 대안을 제공한다.

# namedtuple() => 이름 붙은 필드를 갖는 튜플 서브 클래스를 만들기 위한 팩토리함수.
# deque => 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
# Counter => 해시 가능한 객체를 세는 데 사용하는 딕셔너리 서브 클래스
# OrderedDict => 항목이 추가된 순서를 기억하는 딕셔너리 서브 클래스
# defaultDict => 누락된 값을 제공하기 위해 팩토리 함수를 호출하는 딕셔너리 서브 클래스

# 시퀀스란?
# 파이썬에서 가장 기본적인 데이터 구조는 시퀀스다.
# 시퀀스란 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조다.
# 파이썬에서는 여섯가지 시퀀스 유형이 존재한다. list, tuple, dictionary, 문자열(String), 바이트배열, range객체, 바이트 시퀀스

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
import operator
# # 내가 생성한 튜플객체를 정의
# # 결국 'x y'는 필드이름이 됨 c언어의 struct 처럼 멤버를 가지고 있는 셈이다.
# # 이때 rename이라는 매개변수가 존재하는데
# # rename = true로 할시에 예약어를 사용하게 되면 자동으로 positional 한 이름으로 매개변수의 이름을 바꿔준다.
# Point = namedtuple("Point", 'x, y')


# # namedtuple은 튜플객체가 만들어졌을때, 튜플의 이름이 객체의 이름으로 보여지며
# # 필드의 값을 보여준다.
# # 이후 인덱스 뿐만 아니라 필드의 이름으로도 접근이 가능하다.
# # 만약 튜플에 지정될 매개변수가 필드는 3개인데 두개만 넘겨주었다 이런 경우
# # namedTuple은 mostright parameter 방식을 가지기 때문에
# # 가장 오른쪽에 있는 매개변수부터 채우게 된다.
# # 예를들어 멤버변수가 x, y, z가 존재한다고 가정해볼때
# # Point(1, 2) 두개의 변수만 넘겨주게 된다면, mostright parameter 방식에 의해서
# # z = 2, y = 1로 채워지게 되며, 넘겨지지 않은 파라미터에서 required 에러를 만나게 된다.
# p = Point(1, 2)
# print(p.x, p.y)
# print(p[0], p[1])


# # deuqe는 삽입과 삭제를 O(1)의 성능을 보여주는 리스트류 컨테이너다.
# # deque 같은 경우는 queue 자료구조와 list 자료구조를 일반화 시켜둔 것이다.
# # 일반 list보다 성능이 우수하다.
# # 또한 deque는 thread-safe하다.

# # append() = > 데크의 오른쪽에 채우게된다.
# # appendleft() => 데크의 왼쪽에 채우게된다.
# # pop() => 데크의 오른쪽 요소를 제거하고 반환한다.
# # popleft() => 데크의 왼쪽 요소를 제거하고 반환한다.
# # clear() => 모든 요소를 제거하고 길이가 0이 되도록 한다.
# # insert(i, x) => 데크의 i위치에 x를 삽입한다.
# # rotate(n=1) => 데크를 n단계 오른쪽으로 회전한다.
# # 만약 n이 음수라면 왼쪽으로 회전한다.

# # 결국 오른쪽 회전이라고 한다면 가장 끝에 있는 원소가 가장 앞에 오게되니까
# # d = deque()
# # d.appendleft(d.pop()) == d.rotate(n=1)

# # 그리고 왼쪽 회전이라면 왼쪽에 있는 원소가 가장 뒤로 갈테니까
# # d.append(d.popleft()) = d.rotate(-1)

# # 데크를 만들게 되면
# # 헬로를 가지고 있는 디큐를 하나 만든다.
# # 그럼 디큐 객체가 Hello를 리스트단위로 분리해서 가지고 있다.
# d = deque("Hello");
# print(d)


# # stack을 구현하는것.
# # 1~5까지의 수를 넣고
# # 스택의 특징은 가장 LIFO
# # 가장 마지막에 넣은게 가장 먼저 나온다.
# for i in range(1, 6):
# 	d.append(i)

# # 따라서 5가 가장 먼저 넣어졌고
# # d.pop() 하면 가장 뒤에 있는 것이 꺼내지기 때문에
# # 스택을 구현한다고 할 수 있다.
# for i in range(len(d)):
# 	print(d.pop())

# # 큐는 가장 FIFO
# # 가장 먼저 들어간게 가장 먼저 나오는 구조다
# for i in range(1, 6):
# 	d.appendleft(i);

# # 이렇게 구현한 이유는 1~5까지 먼저 들여보내면 가장 첫번째에 들어오게 되니는 데이터는
# # 5가 될테니까
# # 결국 가장 먼저 들어온 데이터가 가장 끝에 있게 된다.
# # 리스트로 표현해보자면
# # 따라서 d의 길이만큼 pop한다면 queue를 구현하는 예제가 된다.
# for i in range(len(d)):
# 	print(d.pop())

# #Counter
# #Counter는 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환한다.
# #요소가 딕셔너리 키로 저장되고, 개수가 딕셔너리 값으로 저장된다.


# # 문자열을 갖는 list
# text = list("sausages")
# print(text)

# # text 시퀀스 자료형의 각각의 요소들이 key값으로 그리고 그것들의 개수가 값으로 들어간다.
# # 마찬가지로 딕셔너리 형태로 반환
# c = Counter(text)
# print(c)


# # orderedDict
# # 순서를 보장해주는 딕셔너리다.
# # 기존 딕셔너리에서는 순서가 보장이 되지 않는다.
# # 순서가 보장아 인된다는 것은
# # 저장하는 순서대로 저장이 되지 않고, 랜덤하게 저장이 된다는 것을 의미한다.
# # 따라서 이런 문제를 해결하기 위해서 값을 입력하는 순서가 유지되어야 한다면
# # orderedDict를 활용해볼 수 있다.


# # 딕셔너리 정렬방법
# # dict = {'A' :1,'D' :2,'C' :3,'B' :4}

# # sorted 함수는 정렬해서 반환해준다.
# # key 값을 기준으로 정렬한다.
# sorted_dict = sorted(dict.items())

# # 만약 딕셔너리를 value에 의해서 정렬하고 싶다면 어떻게 해야 할까
# # key매개변수에 operator.itemgetter(1)을 삽입해주면
# # key값을 기준으로 정렬이 된다.
# # 기본 오름차순
# # sorted는 항상 리스트를 반환한다
# # 문자열을 넘기더라도 정렬된 상태의 문자배열을 리턴
# # 어떤 자료형에 상관없이 리스트를 반환
# # sorted 숫자형과 문자형 간에는  < 연산자가 지원이 안됨
# # 즉 논리적으로 비교가 가능해야 된다는것.
# # 같은 자료형끼리 되어 있다고 하더라도 none 자료형이 껴있다면 대소구분을 할 수 없음
# # 정렬자체가 대소구분을 하는 것이기 때문에
# # reverse=True라고 한다면 내림차순으로 만들어준다.
# # 그럼 아래 같은 문장인 경우 내림차순으로 정렬하는데 key값이 아닌 value 값을 기준으로 정렬하게 된다.
# sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
# # 이런경우 원래는 정렬이 되지 않는데
# # int함수가 리스트에 적용이 되어서 
# # 문자를 Int로 바꿔준다.
# # 단 반환하는 값은 자료형 그대로를 넘겨준다.
# # sort()는 기존배열을 바꿔주게 되고
# # sorted() 함수는 기존 배열을 건들지 않고 정렬하고 반환해준다.

# # sorted(["2", 1], key=int)
# # print(sorted_dict)
# # for i in sorted_dict:
# # 	print(i)

# # orderedDict
# # 정렬상태를 유지시키는 딕셔너리
# for k, v in OrderedDict(sorted(dict.items(), key=operator.itemgetter(1))).items():
# 	print(k, v)



# # defaultdict는 기본값을 0으로 초기화 시키는 딕셔너리
# # 좋네..
# d = defaultdict(lambda : 0)
# # list타입으로 값을 결정하라고 한다.
# # 안에 들어갈 데이터 타입을 지정해주면된다.
# d = defaultdict()
# # d['first']
# # d['second']
# print(d)

# # 리스트 컴프리헨션

# arr = [[c] for r in range(4) for c in range(3)]
# arr = [[i for i in range(4)] for c in range(3)]

# # 이렇게도 쓸 수 있고
# for i in range(3):
# 	arr.append([i for i in range(4)])

# # arr = [[], [], []]
# # for i in range(3):
# # 	for j in range(4):
# # 		arr[i][j] = j

# for r in range(4):
# 	for c in range(3):
# 		arr.append([r])


# dict1 = {1:'first', 2:'second', 3:'third'}

# # key value를 바꿔서 출력하고 싶다
# dict2 = {val:key for key, val in dict1.items()}

# subjects = ['math', 'history', 'english', 'computer'] 
# scores = [98, 80, 75, 100]

# # 만약 두객체를 하나씩 맵핑해서 {'math' : 98 } 이런식으로
# dict3 = {key:val for key, val in zip(subjects, scores)}
# print(dict3)

# # enumerate 시퀀스 데이터를 받아서 index와 함께 출력해주는 것을 말함


# e = enumerate(['A', 'B', 'C'])
# print(e)
# for i in range(3):
# 	print(next(e))



# # zip 도 튜플반환
# for i in zip(subjects, scores):
# 	key, val = i
# 	print(key, val)

# # for i in enumerate(["A", "B", "C"], start = 10):
# 	print(i)

# 리스트 두개가 이쏙
# 이걸 두개를 객체를 하나로 묶어서 dict만든다고 ㅏㅎ낟면
keys = [1,2,3]
values = ["a", "b", "c"]

d = dict(zip(keys, values))
print(d)


pairs = zip([1,2,3], ['A','B','C'])


# 이렇게 되면 집핑되서 tuple로 반환하게 되니까
# # 만약 이걸 unzipping 하게 된다면
# for i in pairs:
# 	print(i)

# unzipping한다는건 객체를 다시 되돌린다는걸 의미하니까
nums, letters = zip(*pairs)
print(nums, letters)


g = lambda x : x**x
print((lambda x: x**x)(2))
print(g(2))

# map은 결국 iterable한 객체의 요소들을 함수를 적용하겠다는 의미
# 함수 int를 적용하겠다. arr의 요소들은
arr = ['1', '2', '3']
arr1 = ['1', '2', '3']
s = list(map(int, arr))
print(s)

f = lambda x, y : (int(x)*2, int(y)*2)
a = list(map(f, arr, arr1))
print(a)

# map = 함수를 적용한 결과를 map객체로 반환 -> 이후 원하는 데이터 형태로 바꾸어서 사용
# filter = 시퀀스 자료형들을 함수를 적용하고 나서 -> 이때 True를 반환하는 값만 묶어서 반환

ar = [1,2,3,4,5]
f = lambda x : x % 2 == 0
print(list(filter(f, ar)))

f = lambda x : True if x % 2 == 0 else False
print(list(filter(f, ar)))





# 시퀀스 객체들은 iteration을 제공한다.


# iter = obj.__iter__()
# while True:
# 	try:
# 		x = iter.__next__()
# 	except:


# yield 값을 반환하면서, 코드의 실행을 함수의 바깥에 양보

# 시퀀스 객체를 yield할때는 yield from 시퀀스 사용

# def mult_generator():
# 	arr = [1,2,3,4]
# 	yield from arr

# g = mult_generator()
# print(list(g))


def trace(func):
	# 클로저가 구현되어져 있는 내부함수에서
	# 데코레이터를 사용한 함수의 매개변수와 동일하게 만들어준다.
	def wrapper(a, b):
		r = func(a, b)
		print(r)
		return r

	return wrapper

@trace
def add(a, b):
	return a + b

a = add(1, 2)
print(a)
