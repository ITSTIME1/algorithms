import math

p1 = (4, 1)
p2 = (2, 3)


# 두점 사이의 거리 구하는 이게 잘못된건가?

a = p1[0]-p2[0]
b = p1[1]-p2[1]

result = math.sqrt(math.pow(abs(p1[0] - p2[0]), 2) + math.pow(abs(p1[1] - p2[1]), 2))

result1 = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

print(result)