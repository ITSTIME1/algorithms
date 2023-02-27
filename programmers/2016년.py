import sys
import heapq
import datetime
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


a = 5
b = 24

days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

b = days[datetime.date(2016, a, b).weekday()]
print(b)


