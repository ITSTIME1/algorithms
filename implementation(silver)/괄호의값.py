# 계산하는 방법을 좀 구체화해보자


# 일단 열린 괄호가 왔을때

# 내가 어디부분에서 계산ㅇ르 할지가 중요한데

# 열린괄호가 나왔다면

# 1. 서로다른 닫힌괄호가 올경우 괄호 못만듬
# 2. 서로다르지 않은 괄호가 올경우 계산을 할 수 있음

# 3. 계산을 시작할 불리언을 하나 만들어둔다면
# 계산을 시작하는건지 아님 추가해야되는지 알 수 있음
# 만약 계산을 시작하고 있다면
# 안에 () []의 개수를 세면됨
# () = 1
# [[]] = 2개가 나타났음
# 그렇다면 1개라면 그냥 하나만 있는거니까 t 합계에 해당하는 점수 증가
# 만약 2개 이상이라면 제곱해서 합계추가 3**2 = 9


# 4. 서로 같은 괄호의 닫힌괄호가 왔을경우 (게임시작하고 있을때) 한 덩어리가 끝났다는걸 알기 위해서
# 괄호의 남아 있는 값은 무조건 한개여야됨
# 그럼 만약 괄호의 남아있는 값이 1개이고 닫힌괄호가 왔을때
# 이전 의 합계에 닫힌괄호가 왔으니 게임을 종료한다는 불리언 값을 바꿔주고
# () [] 따라 이전 합계를 곱해서 total 합해줌


# 5.이후 게임이 종료되고 나서 열린 괄호 혹은 닫힌 괄호가 왔을때
# 다시 게임시작 위 과정 반복

# 6. 마지막 토탈값 출력


# # 굉장히 까다로운데


import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


string = input()


total = 0
start = False
check = []


stand_start = ""
open, close = 0, 0
for i in range(len(string)):
	# 열린괄호 둘중에 하나가 오고 게임이 시작되고 있지 않다면
	# 열린괄호부터 나오지 않는다면 불가능함
	if string[i] == "(" and start == False:
		start = True
		stand_start = string[i]
		continue

	if string[i] == "[" and start == False:
		start = True
		stand_start = string[i]
		continue

	if string[i] == "(" and start == True:
		check.append(string[i])

	elif string[i] == "[" and start == True:
		check.append(string[i])

	elif string[i] == ")" and start == True:
		word = check[-1] + string[i]
		if word == "()":
			open += 1
		check.pop()

	elif string[i] == "]" and start == True:
		word = check[-1] + string[i]
		if word == "[]":
			close += 1
		check.pop()
		continue

	# 1, 2
	if len(check) == 1 and string[i] == ")" and start == True:
		start = False
		word = check[-1] + string[i]
		ans = 0
		if open == 1:
			ans += 2*open
		elif open >= 2:
			ans += 2**open

		elif close == 1:
			ans += 3*open

		elif close >= 2:
			ans += 3**open


		if word == "()":
			total += 2*ans

		elif word == "[]":
			total += 3*ans


print(total)










