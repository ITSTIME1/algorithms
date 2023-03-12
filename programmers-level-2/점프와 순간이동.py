import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 5 까지 간다고 한다면 
# 0에서 출발하여

# 0 1 2 3 4 5 <- 까지 도달해야 된다는거고

# 건전지 사용량을 최소로하면서 도착하는 방법..



# 처음에만 무조건 한칸 점프

# 0 % 6 == 0 1
# 1 % 6 == 1 s
# 2 % 6 == 2 s
# 3 % 6 == 3
# 4 % 6 == 4 s 8 이 되버리기 때문에 도착지점을 넘어가게된다. 따라서 이럴때 k만큼 점프가 필요함 5-4 = 1
# 5 % 6 == 5

# 따라서 2번 건전지를 소모하면 가장적게 도착가능함.

# 0 % 7 = 0 1
# 1 % 7 = 1 s
# 2 % 7 = 2 k
# 3 % 7 = 3 s
# 4 % 7 = 4
# 5 % 7 = 5
# 6 % 7 = 6 

# 이런식으로 되버리네

# 그럼 결국 st + 1 * 2 == N 될 수 있다면 바로 s를 사용해도 된다는거네
# st += 1 이동하라는거고 그럼 거기서 다시 st * 2 해서 갈거니


N, st, cnt = 6, 0, 0

while st != 1:
	

print(cnt)




