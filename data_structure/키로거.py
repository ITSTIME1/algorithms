import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 문자열의 길이가 100만정도그럼 하나씩 읽어들이면 굉장히..
# 백스페이스는 하이픈 "-"

# 커서의 바로앞에 글자가 존재한다면 그 글자를 지운다>
# 화살표 <>

# 커서의 위치를 움직이는건 왼쪽또는오른쪽으로 +1 만큼 움직인다


# 일단 화살표나 백스페이스가 없다면 문자 그대로 표현되어져 있다면
# 문자 그대로가 비밀버놓가 된다.

string = list(input().strip())
print(string)


# 화살표를 어떻게 처리할건지인데 왼쪽 오른쪽으로 이동가능하다고 했으니가
