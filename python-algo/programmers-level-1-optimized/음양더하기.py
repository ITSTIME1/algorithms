import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 이 문제는 불리언으로 주어진 배열을 보고
# True 라면 +
# False 라면 -를 이용해서 정수들의 합을 구하는 문제다.



# sum함수를 사용해서 마지막에 합계를 구하게 되고 zip 함수를 사용하고 있다.
# 그럼 zip() 함수에 대해서 공부해봤으니 zip함수가 하는게 iterable한 객체를 하나로 엮어주는 기능을 한다는걸 알았다.
# 그렇다면 가지고온 불리언 요소가 True, False인지만 판단하면 되기 때문에
# 양수인지 음수인지만 판단을해주면 된다.
# 양수면 그대로 더해주게되고 음수라면 -붙여서 더해주게된다.
# a = sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# zip()함수는 iterable한 객체를 인자로 받고 튜플이나 리스트와 같은 형태의 자료구조 데이터를 받으면서
# 각 객체가 담고 있는 원소를 엮어주는 기능을 한다.

numbers = [1,2,3]
letters = ["A","B","C"]

# 엮는거니까 같은 인덱스의 위치에 있는 값들끼리 튜플로 묶어서 반환.
for pair in zip(numbers, letters):
	print(pair)


# zip()함수는 병렬처리도 가능하다.

for number, upper, lower in zip("12345", "ABCDE", "abcde"):
	print((number, upper, lower))

# 그럼 엮어 놓은 데이터를 다시 해체 할 수 있을까
num = [1,2,3,4,5]
letters=["a","b","c"]

# zip으로 우선 데이터를 엮어주고
pairs = list(zip(num, letters))
print(pairs)

# *통해서 묶여져 있는 데이터들을 n, l에 두개의 튜플로 나눠 담았다.
n, l = zip(*pairs)
print(n, l)


# 사전 변환도 가능한데
# key:value 형태의 딕셔너리 형태를 만들려고 할때
# 리스트 컴프리헨션 방법을 쓰던지 for문을 통해 if 조건처리 후 사전을 만들었다.
# zip을 이용해서 만드는 방법이 있는데
keys=[1,2,3]
values=["A","B","C"]

# 이런식으로 zip으로 key 와 value 값을 엮은 다음 dict으로 만들어주면 불필요한 조건들이 없다면
# 이렇게 한줄로 표현도 가능하다.
a = dict(zip(keys, values))
print(a)

# 만약 따로 조건이 추가되어야 할 때 for i in zip(keys, values): 를 통해서
# 얻은 튜플값으로 튜플값의 대한 조건을 건뒤 dict 추가해주는 방법도 사용할 수 있을 것 같다.


# 그럼 지금까지 zip에 넘기는 매개변수의 iterable한 객체들의 길이는 전부 동일했다.
# 그럼 zip에 넘기는 매개변수의 길이가 다르다면 어떻게 될까..


# 만약 인자의 길이가 다를 때는 가장 짧은 인자를 기준으로 데이터가 엮인다.
a = [1,2,3]
b = ["month"]
# (a, b) 형태로 묶으라는 의미가 될텐데
# a의길이는 3 b의 길이는 1이다
# 서로의 길이가 다르므로 어떻게 출력이 될까..?
# 출력해보면 짧은 데이터인 b를 기준으로 (1, "month") 하나만 튜플값으로 리턴한걸 확인할 수 있다.
# 그럼 나머지 값은? 짝이 맞지 않기 때문에 버려졌다고 보면 된다.
c = list(zip(a, b))




