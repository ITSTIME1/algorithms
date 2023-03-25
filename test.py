import sys
import heapq
import math
import datetime 
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 46:40-01:10
time_1 = datetime.datetime.strptime("48:00", "%M:%S")
time_2 = datetime.datetime.strptime("47:50", "%M:%S")

get = time_1 - time_2
print(str(get)[2:])



a = "45:30"
b = "10"

next_time = a + dt.timedelta(seconds=30) # 30초 더하기
