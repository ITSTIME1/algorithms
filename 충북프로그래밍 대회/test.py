import sys
input = sys.stdin.readline

s, e = map(int, input().split())

if s < 2 or s > 9 or e < 2 or e > 9:
    print("\"INPUT ERROR!\"")
    exit()
    


# 5, 4
arr = []
if s > e:
    for i in range(s, e-1, -1):
        print(i)
        arr.append(i)    
else:
    # 4, 5
    for i in range(s, e+1):
        arr.append(i)


total = [""] * 10
for i in arr:
    for j in range(1, 10):
        total[j] += f'{i} * {j} = {i*j:2d}' +  "   " 

for i in total:
    print(i)
# list = [1,11,111,1111]  
# for i in list:
#     print(f'9 * {i:4} = {9*i}')