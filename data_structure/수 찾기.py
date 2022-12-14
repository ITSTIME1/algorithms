# 문제분석

# 정수범위를 넘어가지 않게끔 해놨네

# 1 부터 n 까지 n개의 정수가 주어졌을때
# 거기에 값이 존재한다면 1 존재하지 않는다면 0
# 근데 자연수 범위가 10만
# m도 10만까지

# 1~N 까지의 수
# 딕셔너리를 이용한 문제 그냥 리스트를 사용한다면
# 시간 초과가 난다 10만의 제곱번 만큼 순회하기 때문이다
# 하지만 딕셔너리에서 키 값을 찾는건 O(1)로 상수시간에 처리되기 때문에
# num_m 10만번의 연산만 진행한다면 충분히 1초안에 들어온다

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num_m = list(map(int, sys.stdin.readline().split()))
# num_m 에 있는 숫자들이 num에 있으면 된다

dic = {}
for i in num:
	dic[i] = 0


for i in num_m:
	if dic.get(i) == 0:
		print(1)
	else:
		print(0)
