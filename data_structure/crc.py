import sys
import heapq
import math

import zlib
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

#!/usr/bin/python
# -*- coding: cp949 -*-


# 32비트 unsigned 형으로 변환하는 함수 정의
def unsigned32(n):
  return n & 0xFFFFFFFFL



# 본격적인 프로그램 시작


# 테스트용 문자열 정의
s = "ABCD"

# 문자열의 CRC32 계산
result = unsigned32(zlib.crc32(str(s)))

# 16진수로 출력
print "%08X" % (result)
# 출력 결과: DB1720A5