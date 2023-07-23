# 사전순으로 올 수를 구하는 함수.
# [1,3,6,5,4,1]
# 좋은 알고리즘을 하나 배웠다.

import sys
input = sys.stdin.readline

def nextPermutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    # [z,o,o]
    # [-1, z, o, o]
    # 때문에 값을 만들지 못하므로 False
    if i == -1:
        return False

 
    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1
 
    arr[i], arr[j] = arr[j], arr[i]
    # i+1 까지의 값을 result에 넣어주고
    # reversed 한 값을 extend 해서 list 요소들을 뒤에서부터 넣어주는 식으로 구현했구나
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result


t = int(input())

for _ in range(t):
    # 공백을 없애라고 했으니까
    string = list(input().strip())
    ans = nextPermutation(string)
        
    # 값을 반환하지 못한다면 False를 
    if not ans:
        print("".join(string))
    else:
        print("".join(ans))
