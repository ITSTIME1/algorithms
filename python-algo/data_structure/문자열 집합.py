# 문제분석

# 문제분석을 해보자

# 최대 1억까지 라면
# O(n^2)


# n개의 문자열은 집합 s에 포함되어 있는 문자열들
# m 개는 검사해야 하는 문자열

# 문자열이 포함되어 있어야 하는거지


# 그 문자열이 있나 확인해야 하는거구나  ㅇㅋ 집합 s에 같응ㄴ 문자열이 여러분 주어지는경우가 없기 때문에
# 따로 필터를 거칠 필요가 없어보인다
import sys
n, m = map(int, sys.stdin.readline().split())
# 문자열 s 
# 사실 n+m 만큼 받아도 되느데
# 해서 n 만큼만 따로 dic 넣고 다 돌렸으면 그 다음부터는 확인하면 되긴 하는데
# 음 이 방법도 O(n+1)
# 결국 O(n)에 해결 가능

# 딕셔너리에서 key 값을 찾는건 1 이기 때문
# 만약 리스트로 했다면 좀 걸렸겠따
dic = {}
for _ in range(n):
	string = input()
	if string not in dic:
		dic[string] = 1

cnt = 0
for _ in range(m):
	string = input()
	if string in dic:
		cnt += 1

print(cnt)
# 음 문제가 그렇게 어렵지 않네 만약 필터를 거쳐야 한다면 어려울 순 있었을거 같네

