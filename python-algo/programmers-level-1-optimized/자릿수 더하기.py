import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 자연수 n이 주어지면, n의 각 자릿수의 합을 구하는 함수
# 123 이면 1+2+3 을 리턴한다고 하는데
# n의 범위가 1억이하
# 재귀로 구현한 방법.

# 감탄 스럽네 수학을 이용한 원리로
# 자릿수를 10으로 나눈 나머지가 일의자리


# 1234 % 10
# 그럼 최초 나머지는 4 + 몫은 123이 되니 다시 123을 10으로 나누면
# 3이 되고 + 12
# 12를 다시 2 되고 1은 10보다 작으니까 마지막까지 온것으로 확인이 되었고
# 거꾸로 올라가면서 1+2+3+4가 되어 = 10이 된다는걸 알 수 있는 코드다.
# 이걸 재귀로 구현하네..

def sum_digit(number):
	if number < 10:
		return number
	return number%10 + sum_digit(number//10)

sum_digit(number)