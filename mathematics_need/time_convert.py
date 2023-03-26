import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 요건 잊지 않았으면 좋겠는거지
# 되게 간단한건데도 어려워
def time(s):
	h = s // 3600
	m = (s // 60) % 60
	cho = s % 60
	return [h,m,cho]

a = time(30000)
print(a)




# def hms(s):
#     hours = s // 3600
#     s = s - hours*3600
#     mu = s // 60
#     ss = s - mu*60
#     print(hours, '시간', mu, '분', ss, '초 입니다.')

# b =hms(30000)
# print(b)


# def convert_to_preferred_format(sec):
#    sec = sec % (24 * 3600)
#    hour = sec // 3600
#    sec %= 3600
#    min = sec // 60
#    sec %= 60
#    print("seconds value in hours:",hour)
#    print("seconds value in minutes:",min)
#    return "%02d:%02d:%02d" % (hour, min, sec) 
# convert_to_preferred_format(30000)




