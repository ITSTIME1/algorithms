# 문제분석

# 비밀번호를 찾는 프로그램을 만드는거네

# n 만큼 사이트 주소와 비밀번호를 받아서
# 중복이 안되니까
# key : value 로 저장해두고
# 찾을 사이트를 m만큼 입력받으면서
# 찾아오면 되겟는데

import sys

n, m = map(int, sys.stdin.readline().strip().split())

dic = {}
for _ in range(n):
	site, pas = input().split()
	dic[site] = pas

for _ in range(m):
	find = sys.stdin.readline().strip()
	print(dic[find])
