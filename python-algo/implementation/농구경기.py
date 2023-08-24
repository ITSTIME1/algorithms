import sys
from collections import Counter
input = sys.stdin.readline


# 이걸 시간적으로 더 줄여보자
# 어떻게 이게 더 오래걸리지
# 8ms나 차이난다고 그럴리가..
n = int(input())

tabel = Counter(input().strip()[0] for _ in range(n))
result = [k for k, v in tabel.items() if v >= 5]
if not result:
	print("PREDAJA")
else:
	result.sort()
	print("".join(result))




