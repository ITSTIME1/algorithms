# 문제분석 

# 일단 값들을 하나씩 받아올때마다 우선순위를 정한다
# 예를들어 처음 ㄷ르어온 값이 12 7 9 15 5 라면은
# 처음 정렬을 reverse 정렬을 수행해 내림차순으로 정리를한다
# 15 12 9 7 5
# 그리고나서 값을 가지고오고 그 값을 가지고 왔을때
# 첫번째값부터 비교해서 15보다 큰 값을 index 0번 자리에 넣어준다. 이럴때 deque를 활용한다면 appendleft를 통해서 넣을 수 있다.
import sys
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())
stack = deque([])


# O(n^3)
# 1500 * 1500 * 1500 = 33억 ㅋ

for i in range(n):
	num = list(map(int, input().split()))
	
	num.sort(reverse=True)

	if len(stack) == 0:
		for i in num:
			stack.append(i)
		continue

	for j in range(len(num)):
		for k in range(len(stack)):
			if stack[k] < num[j]:
				stack.appendleft(num[j])
				break


stack_list = list(stack)
stack_list.sort(reverse=True)
print(stack_list[n-1])







