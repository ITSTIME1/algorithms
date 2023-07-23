import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

an = list(map(int, input().split()))

an.sort()

# # 시간초과 걸리는건 당연한데
# dic = {str(i): 0 for i in an}

# for i in an:
# 	stand = i
# 	t = 0
# 	for j in range(len(an)):
# 		t += max(stand, an[j]) - min(stand, an[j])
# 	dic[str(stand)] = t

# dic_list = [k for k, v in dic.items() if min(dic.values()) == v]
# print(min(dic_list))
stand = len(an) // 2 + len(an) % 2

# 무조건 절반의 값들중 같은 총합이 있을 수 있으니까
# 그 절반의 값들중 하나의 아래값만 선택하면 베스트지
print(an[stand-1]	)
# 그럼 시간초과가 안걸리고 하는방법은.?
# 이 방법에서 알 수 있듯이 가운데에다가 두면 가장 베스트임
# 근데 가운데의 값이 딱 나누어떨어지지 않을수도 있는데

# 5라면
# 5//2 + 5 % 2 = 3
