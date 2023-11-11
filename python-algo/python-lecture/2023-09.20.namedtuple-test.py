# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{j} * {i} = {i * j:2d}', end='\t')
#         print('%d * %d = %2d' % (j, i, i * j), end='\t')
#         print('%d * %d = %2d' % (j, i, i * j), end="\t")
#     print()  # 다음 줄로 넘어감



# def solution():
#     return 1, 2


# a = solution()
# print(type(a))

import collections

# 메소드가 없이 필드만 존재하는 클래스를 생성할 수 있음
Point = collections.namedtuple('Point', ['abc', 'def', 'ghi', 'abc'], rename=True)
# 각각의 값에 value를 부여
p = Point('change_1', 'change_2', 'change_3', 'change_4')
print(p)

# def와 같은 키워드를 사용할 수 없음
# abc 는 abstract class라는 의미에서 예약어를 사용할 수 없는거지
# 따라서 rename이 true라면 예약어를 사용했을때 자동적으로 positional 한 변수의 이름으로 변경해준다는것.
Point1 = collections.namedtuple('Point', ['abc', 'f', 'ghi', 's'], rename=False)
p1 = Point1(1, 2, 3, 4)
print(p1)


# deque, Counter
from collections import deque, Counter, OrderedDict

a = deque("Hello")

for i in a:
	print(i)


for i in range(len(a)-1, -1, -1):
	print(a[i])



text = list("Hello")
# 딕셔너리 형태로 만들어져 있고, 같은 값들이 몇번씩 나타나는지 알 수 있음.
a=  Counter(text)
print(type(a))


text1 = Counter("waWEFWEFAFEigjfwaef wae jpwaef wa".lower().split(" "))
print(text1)

d = OrderedDict()
d1 = {}
d['a'] = 100
d['b'] = 100
d['c'] = 100

d1['a'] = 100
d1['b'] = 100
d1['c'] = 100
print(d1)
print(d)


import collections, operator

dict = {'A' : 1, 'B' : 4, 'C':3}
print(sorted(dict.items()))
print(sorted(dict.items(), key=operator.itemgetter(1)))



for k, v in OrderedDict(sorted(d.items(), key=operator.itemgetter(1))).items():
	print(k ,v)


df = collections.defaultdict(lambda : 0)

df['nice']
print(df.items())



s1 = [i for i in range(10) if i % 2 == 0]
s = [i if i % 2 == 0 else -1 for i in range(10)]
print(s1)
print(s)



# 중첩 루프네
arr = [c for c in range(4) for r in range(3)]
print(arr)

for i in range(4):
	for j in range(3):
		print(i, end = "")

arr = []
for r in range(4):
	for c in range(3):
		arr.append([r])

print(arr)
arr = [[[c] for c in range(4)] for r in range(3)]
print(arr)



arr1 = [1,1,2,3,3,4]

new_set = {}
for i in arr1:
	print(i)

a=  [1,2,3,4]
b = ['a','b','c','d']
c = [11,12,13,14]
for i in enumerate(zip(a, b,c), start = 1):
	print(i)
	index, a = i
	print(index, a)


a = [1,2,3]
b= [1,2]
for one, two in zip(a, b):
	print(one, two)


test = [1,2,3,4]
f = lambda x : x//2
print(list(map(f, test)))

def countdown(n):
	while n > 0:
		try:
			yield n
			n-=1
		except StopIteration:
			break


def countdown_generator():
	arr = [1,2,3,4]
	yield from arr

index = 10
b =countdown_generator()
print(list(b))




a = countdown(10)
while index > 0:
	print(a.__next__())
	index-=1;

