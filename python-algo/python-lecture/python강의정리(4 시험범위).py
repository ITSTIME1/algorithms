# # # python에서는 collections 모듈이 존재하는데
# # # collections 모듈은 리스트 ,튜플, 딕셔너리, 셋 등을 확장하여 대안을 제공한다.
# # # 즉 확장판이라고 생각하면 된다.
# # # 리스트의 확장인 디큐, namedtuple, defaultdict 같은것들.


# # # collections 모듈에서 namedtuple 메소드를 임포트한다.
# # # 1. namedtuple은 새로운 튜플 서브클래스를 리턴하게 되는데 이는 팩토리함수다. 필드 이름을 가지는 

# # # 2. collections.namedtuple(typename, field_names, rename=False, default = None)
# # # 3. 여기에서 typename은 객체처럼 생성할 이름을 넣어준다고 한다.
# # # 4. 그리고 이건 필드를 가질 수 있다고 한다.
# # # 5. 이 field_names는 sequence 이어야 시퀀스여야한다.
# # # 6. ['x', 'y']
# # # 7. 이렇게 혹은 'x y', 'x,y' 콤마나 공백으로 구분해서 필드를 가지게 된다.
# # # 8. 언더스코어로 시작하는것을 제외하고 필드의 이름으로 가질 수 있다.
# # # 9. field_names는 letter, digit, underscore를 유효한 식별자라고 보긴하지만
# # # 절대적으로 처음 싲가인 digit이거나, underscore이거나, keyword이면안된다. 


# # # rename은 초기에 default로 False로 되어 있다.
# # # if rename이 true로 되어 있다면, 유효하지 않은 식별자들은
# # # 자동적으로 positional names로 교체된다. positional name이라고 하는 것은 해당 필드가 위치한 인덱스를말한다.
# # # ['abc', 'def', 'ghi', 'abc']
# # # 이런 필드네임이 있다고 가정하자. 그럼 여기서 def는 함수 정의 키워드기 때문에
# # # rename=True로 되어 있다면 교환된다. def가 위치한 인덱스는 1번 따라서 _1 형태로 변환되게 된다.
# # # abc도 마찬가지로 _3으로 교환된다.
# # # 여기에서 default 는 None일 수 있고, iterable할 수 있다.
# # # default는 rightmost parameter 방식이기 떄문에
# # # [x, y, z] 라는 필드이름이 존재한다면 값이 매칭될떄
# # # (1,2)만 넘겨주게 되면 z부터 채어지게 된다는 뜻이다. 그러면 x는 인수가 없으니 will required argument가 될 것이다.
# # # from collections import namedtuple, deque, Counter, OrderedDict
# # # import operator
# # Point = namedtuple("Point", ['x','y'])

# # p = Point(11, y=22)
# # print(p)
# # # 필드이름으로도 정의가 가능하다.
# # # named tuple의 장점은 역시 tuple인데 어떤 tuple인지를 읽기쉽다 따라서 readable하다.

# # print(p.x, p.y)

# # # 세가지 방식모두다 가능
# # # named tuple도 튜플이기 때문에
# # # 언팩이 가능하고
# # x, y = p
# # print(x, y)
# # # 인덱스로도 접근이 가능하며
# # print(p[0], p[1])
# # # typename = employeeRecord
# # # type_fileds = name, age 문자열 시퀀스가 되고, 각 필드들을 comma로 구분하고 있다.
# # EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

# # # 결국 이름이 있는 필드들을 위한 튜플의 팩토리함수다.



# # # deque를 정리해보자
# # # deque는 stack, queue를 일반화 해둔 object이다.
# # # 1. 디큐는 thread-safe하다.
# # # 2. 메모리를 효율적으로 사용한다. 원소를 추가하거나 append, pop할
# # # 3. 두 방향으로 삽입삭제하는 것이다 약 O(1)시간복잡도를 보여준다.
# # # 4. 디큐에 maxlen이 한번 다차게 되면, 다 찬 이후에 추가하게 될때,
# # # unix의 tail 기능과 같이 추가되는 아이템의 개수만큼 corressponding of items 만큼
# # # 뒤에서부터 discared 폐기 되어진다.
# # # list와 다른 차이점은 pop(0)이나 insert하는 데걸리는 시간이 O(n)을보여준다.

# # # 디큐의 장점은 List보다 빠른 속도를 가지고 있다는것




# # # Counter를 정리해보자
# # # 1. Counter는 dict의 서브클래스다.
# # # 2. 해쉬가능객체를 딕셔너리로 변환시켜준다.
# # # 3. iterable한 객체를 그들의 요소가 key가되고 그들의 요소의 개수가 value가 된다.
# # # 4. key값으로는 0,음,양 정수범위는 다 key값으로 가질 수 있다.
# # # 5. 만약 key값을 조회했는데 해당 키 값이 없다면 missing items 라면 keyerror를 raise발생 시키는 대신 zero 를 리턴한다.


# # # 문자열을 list로 변환시켜주고
# # text = list("sausages")
# # print(text)
# # # Counter를통해서 iterable한 객체를 넘겨주었으니
# # # iterable한 요소들이 이제 키값으로 들어가게 되고 해당 key에 해당하는 
# # # 개수가 value가 된다.
# # # 즉 Counter객체가 딕셔너리를 품고 있게된다.
# # c = Counter(text)

# # print(c)
# # print(c['s'])

# # d  = OrderedDict()

# # d['a'] = 10
# # d['b'] = 20

# # for k ,v in d.items():
# # 	print(k, v)

# # # OrderedDict
# # # 순서를 보장해주는 dict너리이다.
# # # 기존 딕셔너리는 순서를 보장하지 않는다.
# # # 하지만 orderedDict는 순서를 보장한다.

# # # 딕셔너리 정렬방법
# # # sorted() 함수는 d.items() key,value쌍인것들을 key를 기준으로 정렬한다.
# # # 만약 키에대한 정렬이 아닌, value에 대한정렬을 하고 싶다고 했을떄
# # # operator 모듈에 있는 
# # # itemgetter()메소드에 1을 주게 되면
# # # 값으로 정렬이된다.
# # operator.itemgetter(1)
# from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
# import operator
# # a = sorted(d.items(), key=operator.itemgetter(1))

# d = {}
# d['a'] = 300
# d['b'] = 200
# d['c'] = 500
# d['d'] = 100
# d['e'] = 400

# for k, v in OrderedDict(sorted(d.items(), key=operator.itemgetter(1))).items():
# 	print(k , v)


# # defaultdict
# # 딕셔너리의 key의 value에 기본값을 지정하는 방법이 존재한다.
# # 람다식을 넣어서 0값을 주었다.
# c = defaultdict(lambda : 1)
# c['first']
# c['second']
# # 이런식으로 키값의 value를 기본값을 지정할 수 있다.
# print(c)
# # 좀 응용해보면
# # list를 넣어서
# # key에 의한 값이 리스트가 되게할 수 있다.

# # 이렇게하면 키에 의한 value를 리스트로 묶어낼 수 있다.
# find = defaultdict(list)
# # 이러한 리스트가 존재한다고 할때
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# # s를 하나씩 가져오면서
# for k, v in s:
# 	# k키에다가 v를 추가한다.
# 	# 신기하네..
# 	find[k].append(v)

# print(find)
# print(find.values())




# # 리스트 컴프리헨션이 무엇인지 알아보자
# # 리스트 컴프리헨션의 기본은 알고 있으니
# # 필터링을 보자

# # 뒤에 for문뒤에 if문을 삽입하여 짝수인 조건에만 값을 추가하도록 할 수 있다.
# # arr = [i for i in range(10) if i % 2 == 0]
# # # 만약 참인조건과 else조건을 동시에 만족해야한다면
# # # 그럴때는 추가할 문장 다음에 if else조건을 삽입한뒤 for문을 넣어주면 된다.
# # arr = [i if i % 2 == 0 else -i for i in range(10)]

# arr = [c for c in range(4) for r in range(3)] 
# print("1차원 리스트", arr)

# # 만약[[0,0,0],[1,1,1],[2,2,2]]
# # 하고 싶다면
# arr = [[c for i in range(3)] for c in range(3)]
# print(arr)

# arr = [[c] for c in range(4) for r in range(3)]
# print(arr)

# arr = []
# for r in range(4):
# 	for c in range(3):
# 		arr.append([r])

# arr=[[1, 2, 3], 
# 	[4, 5, 6], 
# 	[7, 8, 9], 
# 	[10, 11, 12]]

# # 2차원 배열을 편평화 시킬 수 있다.

# flat_arr = [i for row in arr for i in row]
# print(flat_arr)

# # for row in arr:
# # 	for i in row:
# # 		print(i, end = " ")


# # set에 대해서도 set comprehension이 되는데
# # 셋 컴프리헨션이 되려면, [] -> {}중괄호로 바꾼것 밖에 안됨

# arr = [1,2,3,4]
# new_set = {i*i for i in arr}
# print(new_set)


# # 딕셔너리에서도 컴프리헨션이가능

# dict1 = {1:'first', 2:'second', 3:'third'}

# # 키 value를 바꿔서 딕셔너리를 재구성 할수도 있음
# dict2 = {v:k for k, v in dict1.items()}
# print(dict2)


# # 오케이
# # enumerate
# # 시퀀스 (list, tuple, string 등) 데이터를 입력받아
# # index를 포함하는 enumerate객체를 반환하는 함수
# e = enumerate(['A', 'B', 'C'])

# # for i in range(3):
# # 	print(next(e))

# # 시작번호를 지정할 수도 있네
# # 신기하네
# for i in enumerate(['A', 'B', 'C'], start = 1):
# 	print(i)


# # zip함수
# # zip객체는 iterable한 객체들을 받고
# # 각 객체가 담고 있는 원소를 하나의 튜플로 묶어주는 함수
# # 만약 여러개의 iterable한 객체들을 받았을때, 길이가 짧은걸 기준으로 묶이고 나머지는 무시됨

# nums = [1,2,3]
# letters = ['A', 'B', 'C' ,'D']

# for pair in zip(letters, nums):
# 	# 튜플로 묶이기 때문에
# 	# 언패킹도 가능하다.
# 	print(type(pair))


# for n, l, u in zip("12345",['A','B','C','D','E'],"abcde"):
# 	# 결국 zip객체로 만든걸 각각 변수로 받아준다.
# 	print(n, l, u)

# keys= [1,2,3]
# values = ['A', 'B', 'C']

# # 이걸 zip으로 매핑시키면 
# # (A,1)
# df = dict(zip(values, keys))
# # zip의 첫번째 인수가 key값이되고 keys가 값이도네
# print(df)


# # zip함수를 사용한다음
# # 이렇게 zip 객체로 묶여잇는 pairs를
# # unzipping할 수 있는데
# # unzipping
# pairs = zip([1, 2, 3], ['A', 'B', 'C'])

# # 본래 iterable한 객체들이 zip함수에 의해서
# # 묶여있던걸 언패킹하는게 아니라
# # 언패킹은 그렇게 zip으로 혹은 튜플로 묶여진 것들을
# # 변수에 담기 위해서 사용되는거지만
# # unzipping은 zip되어 있는걸 다시 원상태로 돌려놓는다고 생각하면된다.
# # 이때 반환되는 값은 튜플이다.
# nums, letters = zip(*pairs)
# print(nums, letters)



# g = lambda x, y : x * y

# # 이건 그냥 람다함
# print(g(2, 3))
# arr1 = [1, 2, 3, 4]
# arr2 = [10, 20, 30, 40]


# f = lambda x, y : (x*2, y*2)
# # 함수 f를 적용
# # 그때 인수는 arr1에 있는 원소들만 받는게 아니라
# # arr1의 인수는 x로 arr2에 있는 원소는 y로가게 되면서
# # 최종적으로 람다에 의해 계산되어지는 값은 튜플값이 리턴되고
# # 튜플값이 리턴되면 list로 변경하면 (x*2, y*2) 형태로 리스트화 되어 있을것.
# print(list(map(f, arr1, arr2)))

# # 람다에 조건도 걸 수 있는데
# # 이게 필터 + lambda 조건 조합으로 사용하게 되면
# arr = [1,2,3,4,5,6,7,8,9]
# f = lambda x: x%2==0
# f1 = lambda x : True if x % 2 == 0 else False
# # 그럼 최종적으로 짝수인것만 filter에 의해서
# # 걸러져서 리스트로 만들게 되면 짝수가아닌 수가 list에 남아 있게 된다.
# # f1의 함수를 적용하게되면, 짝수인것은 True를 반환하니까
# # filter가 걸려있을때 filter는 함수에 적용하는 값들이 True를 리턴하는 것만
# # 반환하기 때문에 똑같이 x % 2 ==0 의 값들을 리턴하는것과 같은 효과이다.
# print(list(filter(f, arr)))

# # reduce는 
# from functools import reduce
# # 시퀀스의 각 요소를 차례대로 함수에 적용한후, 
# # 하나의 값을 반환하는 형식
# # 이때 계산결과가 x로 가게되고 이후에 올 값은 y에 위치하게 됨
# # 만약 x, y가 처음 계산하는 거라면 index == 0 and index == 1이라면
# # 처음 계산하는거니까
# # 이때는 x ,y에 그대로 대입
# # 계산결과가 끝나면 x로 값을 옮겨주고, 이후 새로운값을 y에 대입
# # iterable이 다끝나게 되면, 최종적인 값을 반환

# f3 = lambda x, y : x + y
# print(list(reduce(f3, arr)))

# # 시퀀스 객체들은 iteration을 제공한다.
# def multi_generatr():
# 	arr = [1,2,3,4]
# 	# 시퀀스 객체를 리턴할때는 yield from 객체를선언해서 리턴한다.
# 	yield from arr

# a = multi_generatr()
# print(list(a))
s = (x for x in range(10))

print(s)
for i in s:
	print(i)
# 리스트 컴프리헨션 방식의 generator를 만들면 이런식으로 된다.
# 하지만 이 값들은 다시 재사용이 불가능하다.
for i in s:
	print(i)

# 외부함수에서 내부함수를 정의하는 방법
# closure라고 하고 클로저라고 한다.
# 외부함수는 내부함수 객체를 반환한다.
def outer(num):
	def inner():
		print(num)
	return inner
	


def add(x, y):
	# assert 조건식, 진단메세지
	assert isinstance(x, int), 'Expected int'
	return x + y