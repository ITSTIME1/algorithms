import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n*n 칸의 지뢰찾기 판이 있고
m은 지뢰의 개수를
빈칸은 . = 비어있는 칸을 나타낸다

지뢰를 찾지 않는한 게임은 계속된다.items
그럼 끝가지 지뢰를 찾지 않았다고 했을때
전체에서 - m개를 빼면 = 지뢰가 아닌 칸의 수가 나오고
m개의 칸은 반드시 지뢰라고 한다.

아

시물레이션으로 상하좌우 그리고 대각선까지 다 찾아보면서
해당칸 주변의 지뢰가몇개있는지를 알려주면되네
그걸 숫자로 표현하는거고
지뢰가 주변에 없다는걸 알려면 0번을 놓아주면되고
어짜피 지뢰가 있으며눔조건 숫자로알려주어야 하니까
아직 열지 않는 부분은 .점이라고 하네

행을 하나씩 읽어오면서
각 행마다 상하좌우값을 확인한다음

범위는 x의 마지막 점까지
예를들어 1행을 본다면
0~2 까지 반복을 시행하고
0에서 시뮬 1에서 시뮬 2에서시뮬 나머지는 다 온점
아근데
이럴 순 있네
순서대로 열지 않고 뛰엄뛰엄 열 수 있으니
그런점은 따로 온점으로 구해야되겠는데


xxx.....
xxxx....
xxxx....
xxxxx...
xxxxx...
xxxxx...
xxx.....
xxxxx...

이게원본이지만

xxx.....
xxxx....
xxxx.x.. <- 이런식으로 되어있으면 중간에 온점이 있기 때문에 이때의 온점은 열리지 않는 칸이다 그렇기에 continue x인 지점만 확인하면 될듯
xxxxx...
xxxxx...
xxxxx...
xxx.....
xxxxx...

# 오케이 짜보자
