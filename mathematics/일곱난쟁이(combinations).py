# 2309, 일곱 난쟁이
import sys
from itertools import combinations

dwarf = [int(sys.stdin.readline()) for _ in range(9)]
# 조합을 이용해 9명 중 7명 뽑음
seven = list(combinations(dwarf, 7))

for i in seven:
    if sum(i) == 100:
        ans = list(i)
        break

# 오름차순 출력
ans = sorted(ans)
for ans_ in ans:
    print(ans_)
