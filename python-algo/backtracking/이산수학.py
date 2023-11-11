from itertools import combinations
	
# 공백으로 정수 범위 내에서 입력 받는다.
n = list(map(int, input().split()))

# index = n개의 정수들 중에서 r개를 뽑기 위해서 몇개를 뽑을건지에 대한 변수
index, cnt = 0, 0

# 공집합에 대한 표현
emptySet = "{}"


# 시간 복잡도는 O(2^n)
while index <= len(n):
	if index == 0:
		print(f'{emptySet}')
		index += 1
		cnt += 1
		continue

	for i in combinations(n, index):
		a = ",".join(map(str, i))
		print(f'{{{a}}}')
		cnt += 1
	index += 1


print(f'카디날리티 : {cnt}개')
print(6 + 26 + 10 + 5 + 7 + 18 + 8 + 18)