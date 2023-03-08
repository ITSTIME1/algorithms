import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# x, n을 입력받아서
# x부터 시작해서 x씩 증가하는 숫자를 n개 지니는 배열을 리턴하라.


# x=2, n=5 라고 한다면 2부터 시작해서 2씩 증가하는데 그 수의 개수가 5개 이하인 리스트를 리턴하라.

# 2, 4, 6, 8, 10


x, n = 2, 5 



# 그럼 이건 등차수열로 풀 수 있을것 같다
# 첫째항이 2
# 공차가 x인
# 일반항을 구한다면 2+(n-1)*x
# 2+(n-1)*2
# 2n
# n은 변수 2는 공차가 되버리는데
# 즉 등차수열의 일반항을 이용하면 이런식으로도 가능하다는걸 알 수 있다.

# 핵심.
# 이때 2는 공차이기 때문에 x만큼을 계속해서 곱해주어야 하는것이고
# n은 첫째항 둘째항의 의미이기 때문에 i값이 곱해져야한다
arr = [i * x for i in range(1, n+1)]
print(arr)