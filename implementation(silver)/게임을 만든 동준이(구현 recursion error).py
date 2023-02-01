# greedy


# 그럼 우선 두가지 상황을 나눠서 풀면 될거같에

# 문제는 이건데 왼쪽을 찾아봤을때 수가 없으면 패스지만
# 만약 그러한 수를 찾았다고 가정했을 때
# 이 문제 재귀로 풀면 될거 같은데
# 우선 왼쪽에 만약에 더 작은 값이 존재한다면


# 우선 재귀를 타고 타고 타고가서
# 정렬이 더이상 되지 않는 시점까지 내려가서 정렬을 시킨다음에
# 그 정렬된 시점을 level = arr 업데이트 해준다면
# 될거같은데
# 어려운데?

# 정렬이 완료된걸 어떻게 알지

import sys
sys.setrecursionlimit(10**6)

n = int(input())
level = [int(input()) for _ in range(n)]

# 우선 현재 값이 더 크다면 줄여야하기 때문에
# 현재 값보다 더 작은값이 있는지 확인
# 그럼 그 작은 값의 개수 만큼 줄인다
# 그럼 그 값은 해당 값만큼 감소했고
# 그 값을 업데이트 해주고
ans = 0

def check(val, arr):
	cnt = 0
	for i in arr:
		if val >= i:
			cnt += 1
	return cnt

def recursion(arr, val, index):
	global ans

	cnt = check(val, arr)

	if cnt == 0:
		return ans
	else:
		level[index] -= cnt
		ans += cnt
		recursion(arr, level[index], index)

for i in range(n):
	if i == len(level)-1:
		break
	lastVal = level[i]
	recursion(level[i+1:], lastVal, i)
print(ans)