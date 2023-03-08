import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = 30



# 약수의 합을 확장해서 생각해보면 합이 아닌 개수를 구할때도 똑같은 방식으로 구할 수 있다.
# 여기서 마지막 자기 자신을 나눠 == 0 이 되는 것도 생각해야 되기 때문에 마지막에 n을 추가해서
# 총 개수를 리턴한다.

arr = [i for i in range(1, n//2+1) if n % i == 0]
arr.append(n)
print(arr)