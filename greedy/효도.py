N = int(input())

cost = list(map(int, input().split()))

cost.sort()

# 1,2,4,5,6

sum = 0
for i in range(len(cost)-1):
  sum+=cost[i]


print(sum)