# 문제분석
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 우선
# N+1 일째 되는날 퇴사한다고 했다
# 그렇기 때문에 N일째까지느 상담을 한다고한다
# 그랬을때 N일까지 얼마나 많은 상담을 진행할 수 있으며
# 그때 받는 금액은 어느정도 되는가


# 자 이때 고려해야할 사항은
# 상담을 잡을때마다의 기간이다.
# 만약 1일의 상담을 잡는다고 한다면
# 3일이 걸리게 되어 1일 2일 3일까지는 상담을 더 진행할 수 없다.
# 조건이 하루에 하나씩 상담을 잡는다고 했으니
# 다른 상담을 끌어서 하루에 몰아서 하는건 안된다는 것이다.
# 그렇게 생각해봤을때

# 만약에 예를 하나 들어보자면
# 첫상담을 잡는다면 3일동안 하지 못하기 때문에
# 3일까지는 상담하지 못하면서
# 4일부터 상담을 진행할 수 있다
# 만약 4일 상담하는일수가 N+1을 넘어가지만 않는다면
# 만약 4일에서 상담을 한다고 했을때 5일 걸린다고 한다면
# 총 8일에 종료되게 되는 것이다.
# 그렇다면 이미 N+1일의 퇴사해야 하는데 상담을 진행하는게 말이 안되기 때문에
# 그 기간이 N현재로부터 만약 현재가 1일이라면 + 3일 걸리면 4일째 
# 즉 이 N+currentDate < N+1 보다 작아야 상담이 가능하다는 말이된다.

# 그럼 1,4일 상담을 진행하게 되고
# 5일째 되는 날 상담을 진행하게 되는데
# 이때 고려해야될 사항은 또 5일에서 + 걸리는 상담일수를 했을때
# 5+2 < N+1 보다 작은지 보고 작다면 상담을 해도 된다
# 만약 오래 걸린다면 상담을 진행하면 안된다.

# 그럼 최악의 경우 상담의 필요한 기간은 무조건 1보다 크다
# 하지만 상담이 무조건 가능하다는건 아니기 때문에
# 1일부터 8일이 걸릴 수 있다
# 혹은 1일부터 7일이 걸릴 수도 있다
# 그렇기 때문에 최악의 경우를 고려하지면 아예 이익을 못볼 수도 있다.


# 최악의 경우 모든 일수가 N+1이 넘어가는 경우다
# 그렇게 되면 어떤 날짜에 상담을 잡으려고 해도 N+1이 넘어가기 때문에
# 상담을 진행할 수 없다.

# 이말인 즉 최대이익이 0이라는 말이된다.

# 일단 총 15일까지는 추어지기때문에 N+1인 최대입력풋의 최고일 수는 16일 된다.


# 그럼 일단 생각나는 구현은
# 하루를 정하고 그 하루부터 시작해서 모든 경우를 보는 행위.
# 즉 1일을 정했으면 1일에서부터 시작해서
# 가능한 일수라면 이동해 이익을 더해내고
# 그 이익을 1일 2일 3일 하루별로 
# 따로 하루별로 금액이나 기간의 대한 변동은 하지 않아도 되기 때문에
# 튜플로 해두면 될거 같고
# 우선 가장 최악의 경우 아예 최대이익이 없는 순간도 있다는걸 고려한다면 될거 같은데
# 최선의 경우 가장 처음부터 찾을 수 있겠네
# 하지만 처음부터 찾는게 가장 최선의 경우라는 보장은 없기 때문에
# 모든 경우를 다 고려해봐야 하긴 한다
.

1. 50 + 10 + 10 + 20 = 90



