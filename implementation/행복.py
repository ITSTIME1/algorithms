N = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(max(arr) - min(arr))