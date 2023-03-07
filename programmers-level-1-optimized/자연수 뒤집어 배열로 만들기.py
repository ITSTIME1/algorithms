import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def digit_reverse(n):
	return list(map(int, reversed(n)))



# 여기서 알아야할 점은 python reversed() 함수가 존재하다는 걸 알아야함
# reversed() 함수는 문자를 역방향부터 참조함

# 우선 reversed() 함수를 이해해보자면
# 매개변수로 리스트, 튜플, 문자열로 이루어진 데이터를 받을 수 있다.
# 그렇기 때문에 위 예시에서는 문자열로 변환후 리스트의 넣어줄 때는 
# 역방향으로 먼저 참조한 뒤 int형으로 형변환을 하여 리스트에 넣어주게 된다.

# 단 set과 같이 순서 개념이 없어 인덱스로 접근할 수 없는 자료구조는 reversed()함수를 사용할 수 없다.

n = [1,2,3,4]
n = (1,2,3,4)
n = "1234"

a = digit_reverse(n)
print(a)