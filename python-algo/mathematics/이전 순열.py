import itertools
# N 숫자의 범위
N = int(input())
# permutations 쓰면 시간 초과남.

ar = list(map(int, input().split()))
# 비교할 숫자
# 순열을 반복하면서
# 해당 숫자가 몇번째인지 확인하고
# 그 숫자의 인덱스보다 하나 작은 인덱스가 
check = tuple(ar)
# 숫자 만들기
arr = [_ for _ in range(1, N+1)]

num = list(itertools.permutations(arr, N))
if check in num:
	result = num.index(check)
	if result == 0:
		print("-1")
	else:
		print(*num[result-1])

