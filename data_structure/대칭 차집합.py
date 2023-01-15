# 문제분석

#  자연수를 원소로 갖고

#  두 집합이 a, b 가 있따

# 대칭 차집합?

# a-b, b-a  의 합집합을 대칭 차집합 이라고 한다.

import sys

a, b = map(int, sys.stdin.readline().split())
print(len(set(list(map(int, input().split()))) ^ set(list(map(int, input().split())))))
# arr = set(list(map(int, input().split())))
# brr = set(list(map(int, input().split())))

# print(len(arr ^ brr))



