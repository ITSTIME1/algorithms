# 문제분석 


# N*N 크기의 숫자들이 2차원으로 주어졌을 때
# 모든 수는 자신보다 한 칸 크다고 한다.
# 이 뜻은 index 0칸에 있는 값들은 index 1칸에 있는 값보다 작다는 것. (본인 칸 위의 한정)

# 즉 arr[0][0] = 12
# arr[1][0] = 13 

# 위의 값들처럼 열의 값은 동일하지만 행의 값이 달라졌을때 "행의 값+1 차이이고, 열의 값은 동일할 때 행의 값이 더 큰 쪽이 작은 쪽보다 무조건 크다."


# 그렇다면 이렇게 풀어볼 수 있을거 같은데

# 1. 리스트의 크기가 5인 리스트를 만든다.
# 2. 이렇게 하면 될거 같은데.
# 3. 우선 처음에 리스트에서 가장 큰 값을 찾아서 pre 에 저장해두고
# 4. 그 값을 기준으로 그 값보다 작고 리스트에 포함안된 값들 중 가장 큰 값을 찾고
# 5. 그렇게 반복해서 리스트가 다 채워졌을 때 while문을 종료한다면 리스트의 5번째의 값까지 찾을 수 있을거 같은데
import sys
from itertools import permutations, combinations, product, combinations_with_replacement

input = sys.stdin.readline


n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]



maxVal = 0
for _ in range(n):
	num = list(input().split())
	for j in num:
		if maxVal < int(j):
			maxVal = int(j)
	arr[_] = num

ans = [maxVal]

while len(ans) != n:
	check = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			if maxVal > int(arr[i][j]) and int(arr[i][j]) not in ans:
				check.append(int(arr[i][j]))

	a = max(check)
	ans.append(a)

print(ans[n-1])


print(sys.getsizeof(arr))