N, P = map(int, input().split())
arr = []
arr.append(N)
x = N
while True:
    x = (x * N) % P
    if x not in arr:
        arr.append(x)
    else:
        break

idx = 0
print(x)
for i in range(len(arr)):
    if x == arr[i]:
       
        idx = i
        print(idx)
        
        break
print(len(arr)-idx)
