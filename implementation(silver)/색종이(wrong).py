import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

total = 100 * n

s = []
for i in range(n):
	w, h = map(int, input().split())
	s.append((w, h))


# 사각형의 순서를 정해주고
s = sorted(s, key=lambda x:x[0])



# 아.. 겹치는 부분이 여러개 있을 수 있으니까
# 그 겹치는 수의 개수만큼도 고려해야되는거네
# 그럼 결국 겹쳐지는 개수만큼만 빼면되니까
# 사실 그걸 고려를 해줘야하는거구나
# 그렇게하면 그냥 2차원 배열을 돌면서
# x + 10  y + 10만큼의 
# 정사각형의 넓이만큼 1을 채워서
# 원래 있던 곳의 1은 무시된다 = 곧 겹치는 부분은 무시되는거니까
# 그랬을때 2차원 배열의 1의 개수를 카운팅하면 된다.
def dis(f, sec):
	global total

	if f[0] <= sec[0] <= f[0] + 10 and f[1] <= sec[1] + 10 <= f[1]+10:
		x = f[0] + 10 - sec[0]
		y = f[1] + 10 - (sec[1] + 10)
		total -= x*y


for i in range(n-1):
	dis(s[i], s[i+1])

print(total)

# 1. 겹치는 사각형이 어떤 사각형과 어떤 사각형인지를 먼저 찾고
# 2. 두 사각형사이의 겹쳐진 가로의 길이 =10-abs((x2-x1))
# 3. 두 사각형사이의 겹쳐진 세로의 길이 =10-abs((y2-y1))

# 4. 이 두사각형의 가로와 세로의 길이를 찾았으니까 두개를 곱하고 총 넓이에서 - 빼주면 끝/

# 그럼 사각형이 겹쳤다는건 어떻게 판단할건데

# 가로의 길이가 총 10이라고 햇으므로

# width = 10
# height = 10

# 만약 두 번째 사각형이 x좌표가 첫번재 사각형의 x좌표보다 크거나 같고 그리고
# 첫번째 사각형의 최대x좌표보다 작거나 같다면 겹치지는거
# 그럼 위 식을 넣어주는거지
# 그리고 구한값을 total - dis()
# 빼주면 가ㅡㄴㅇ할거 가틍넫
# 그럼 사각형마다 찾아야하기 떄문에

# x좌표를 순서대로 세우는게 중요할거 같에
# 어짜피 x좌표는 고정되어있으니까
# 그 x좌표값이 곧 사각형의 순서가 되므로
# 1,2비교하고
# 2,3비교할 ㅅ ㅜ있지
#  더 이상 겹치는 사각형의 부분이 없다면 즉 i, i+1 값을 순서대로 검사하면서 간다면
#  끝날거 같은데

