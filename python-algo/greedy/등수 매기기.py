import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 간단한 문제
# 어짜피 절대값의 오차를 최소로 해주면되니까
# 1~N까지의 등수는 1씩 커지고 있기 떄문에
# 맞춰서 성적을 가장 작은 순서대로 맞춰준다면 가장작은 합을 얻을 수 있지.
n = int(input())

grade = [int(input()) for i in range(n)]
grade.sort()
for i in range(len(grade)):
	grade[i] = abs((i+1) - grade[i])

print(sum(grade))
