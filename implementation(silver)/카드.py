# 문제분석

# 숫자카드를 n장 가지고 있다고 할 때

# 그 숫자카드 n장에 각각 정수가 하나 적혀있다고 한다.

# 준규가 가지고 있는 카드가 주어졌을때

# 가장 많이 가지고 있는 정수를 구하라?

# 가장 많이 가지고 있는 정수가 여러가지라면
# 작은 것을 출력해라

# 아 되게 간단한거같은데

# 1
# 2
# 1
# 2
# 1
# 1: 3
# 2: 2


# 1
# 2
# 1
# 2
# 1
# 2
# 1:3
# 2:3

# 가장 많이 가지고 있는 정수가 동일한 개수를 가지고 있지 않을경우
# 그냥 많이 가지고 있는걸 출력하면 될거고

# 가장 많이 가지고 있는 수가 동일하다면
# 가장 작은걸 출력한다.

# hash 를 이용했을때
# max함수를 이용해서 key 를 얻는다면
# maxvalue 가 여러개라도\
# 맨 앞에 있는 key 값 하나만 출력하게 된다
# 하지만 리스트커프리헨션을 사용하게 된다면
# maxValue 에 해당하는 모든 키 값들을 다 가지고 올 수 있다
# 딱 이문제에서 사용하기 좋은 것 같네

# n^2 시간초과가 나니까


import sys
input = sys.stdin.readline

N = int(input())

# 이부분 시간초과를 해결해야 하는데
# in을 쓰면 시간초과인데
# set 을 써보면 될거 같은데


# set 에서 시간복잡도는 리스트에 비해서 int 메서드는 O(1) 의 시간복잡도를 요구한다
# 아니면 리스트를 사용해서 만들어야 할까
# TLE;;
number_check, dic = [], {}
for i in range(N):
	num = int(input())
	number_check.append(num)

number_set = set(number_check)

for i in number_set:
	dic[i] = number_check.count(i)

# python 에서 set = > hashtable로 구성되어져있다
filter_dic = [key for key, value in dic.items() if max(dic.values()) == value]
# 정렬 오름차순으로
filter_dic.sort()
if len(filter_dic) >= 2:
	print(filter_dic[0])
else:
	print(filter_dic[0])
	