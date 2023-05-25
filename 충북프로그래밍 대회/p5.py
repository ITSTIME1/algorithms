import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
    print(X)
    print(line)
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X