import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


seoul = ["Jane", "Kim"]



"김서방은 {}에 있다".format(seoul.index('Kim'))

# 이 문제는 문자열을 다루는 문제인데
# 서울이라는 배열에서 kim의 위치를 찾는 문제이다.

# kim은 seoul배열에서 오직 한번만 나타나고
# 잘못된 값이 입력되는 경우는 없기 때문에
# 그냥 kim의 위치만 잘 반환해서 출력해주면 된다.

# python 의 format()함수를 사용해서 출력하는 방식을 이용하고 있다.
# format함수를 잘 사용하지 않았는데 이런 방법으로 한줄로 구현이 가능하다.
answer = "김서방은 {}에 있다.".format(seoul.index("Kim"))
print(answer)

# format()함수의 기본 사용법은
# .format(깂1, 값2, 값3)
# 그리고 포맷팅할 곳은 {}로 표현하여
# {}, {}, {}
# 이런식으로 index=0부터 앞쪽의 {}에 매개변수로 입력이 된다.
# 그렇게 되면 {값1}, {값2}, {값3} 이런식으로 입력이 되는것이다.

# 확장을 해본다면
# 구구단을 예로들 수 있을거 같은데 1부터9단까지 출력하는 구구단이 있다고가정해보자

# for i in range(1, 10):
# 	for j in range(1, 10):
# 		print("{} x {} = {}".format(i, j, i*j))


# 이번에 문자열의 중괄호의 인덱스를 넣어본다
# 우선 기본예제
s1 = "name : {}, city: {}".format("taesun", "paju")
print(s1)

# 인덱스를넣게된다면?
s2 = "name : {0}, city: {1}".format("taesun", "paju")
print(s2)
# 그럼 인덱스를 바꿔본다면?
# 출력의 결과에서 알 수 있듯이 인덱스의 번호를 {}안에 지정해준다면
# 해당 지정된 인덱스의 위치의 있는 값으로 포맷팅이 진행이된다.
s3 = "name : {1}, city: {0}".format("taesun", "paju")
print(s3)

# 중복을해도 그 위치의 똑같은 값이 들어간다.
s4 = "name : {0}, city: {1} name1: {0}".format("taesun", "paju")
print(s4)


