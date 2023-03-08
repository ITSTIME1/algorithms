import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 근데 이거는 set을 써도 될거같은데 라고 생각하면 하나 기억해야 될건
# set()자료구조는 순서를 보장하지 않음 그리고 결정적으로 1이 두번들어가 있는데
# set 같은 경우 리스트 내에 한 숫자만 남기고 같은 숫자는 전부 지워버리기 때문에
# set()자료형을 사용하는 문제가 아니라는걸 알 수 있고

# 그럼 가장 간단한 방법은 빈배열을 만들어주고 그 배열의 들어가는 숫자가 마지막에 있는 숫자랑 같지만 안흥면 된다.
# 그 이유는 1이 앞에 있고 뒤에 있다는것에서 힌트를 얻을 수 있는데
# 1이 앞에 있다는건 한번 들어오고 그 이후에 1이 들어오는건 쳐냈다는 애기가 될 수 있고
# 마지막에 1이 두번 들어왔는데 1을 하나 더 쳐낸거 보면 마지막에 들어온 1은 그 전의 1이 이미 들어와있기 때문에
# 쳐내진것으로 보인다.
# 따라서 1,3,0,1 이 가능하다

# 두번째 예제도 같은 방식으로 가능하다.

# 처음엔 for을 통해서 if else 를 통해 확인을 진행했고 아이디어도 똑같지만 좀더 최적화된 방법으로 구현해본다면

# [1, 1, 3, 3, 0, 1, 1]
# [1,3,0,1]

arr = []

# for i in arr:
# 	# 괄호를 제거하면 값이 나오지 않는다 그 이유는
# 	# 슬라이싱은 -1: 끝까지를 리스트로 만든것이기 때문에
# 	# 리스트와 리스트를 비교해야 값이 제대로 출력이 가능하다.
# 	# 하지만 괄호가 없는 i는 그저 배열 요소기 때문에 비교가 불가능 하기 때문에 안되는 것이다.
# 	if arr[-1:] == [i]:
# 		continue
# 	else:
# 		arr.append(i)


for c in s:
	if len(answer) == 0 or answer[-1] != c:
		answer.append(c)