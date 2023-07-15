

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
dic = {}

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] not in dic:
        dic[arr[i]] = [i, 1, arr[i]]
    else:
        dic[arr[i]][1] += 1 

result = sorted(dic.values(), key=lambda x:(-x[1], x[0]))


ar = []
for i in result:
    for j in range(i[1]):
        ar.append(i[2])
        
print(" ".join(map(str, ar)))