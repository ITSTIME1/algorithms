# 문제분석
# 일반적인 구현 방법으로 풀게 된다면 굉장히 숫자가 커진다
# 때문에 다른 사람이 힌트를 작성한것 에서 힌트를좀 얻을 수 있었는데
# '포함배제의 원리이다'
# 즉 전체경우의수 - 포함하지 않는 경우의 수 = 포함한 경우의수
# 가 되는것이다
# 간단한 수학적원리다

# 근데 이걸 어떠헥 수학적으로 나타내지
# 포함하지 않는 경우의 수를 어떻게 알아
# 유사한 아이디어 문제는 풀어봤는데
# 문제는 포함하지 않는 경우의 수 개수를 모른다는건데
# 보아하니 dfs, 백트래킹을 사용한다고 한다
# 아직 ㅏㄴㄴ 모르는데..

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
if m != 0:
	c = list(map(int, input().split()))
	arr = c

def ans(n, m):
	# 전체 경우의수는 10**n승의 값이 되고
	# 그 전체 경우에서 - 포함하지 않는 경우의 수 
	total = 10**n
if len(arr) != 0:
	ans(n, m)
else:
	print(10**n)