# O(NlogN) 을 보장.

import sys
N = int(sys.stdin.readline())

array = [int(sys.stdin.readline()) for i in range(N) ]

array.sort()
print(*array, sep="\n")