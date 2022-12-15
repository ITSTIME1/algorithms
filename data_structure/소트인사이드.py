# 문제분석


import sys

n = list(sys.stdin.readline().strip())

# 내림차순은 = 큰수부터

n.sort(reverse=True)
print("".join(n))