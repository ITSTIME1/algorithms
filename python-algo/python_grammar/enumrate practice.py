import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
idx = 0
result = []

data = list(map(int, input().split()))
index = [x for x in range(1, n + 1)]

temp = data.pop(idx)
result.append(index.pop(idx))

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    result.append(index.pop(idx))
    print(index)


for r in result:
    print(r, end=' ')



# 그니까 이 알고리즘을 한마디로 정의하자면
# 그냥 자료구조나 똑같은거 같다

# 일단 처음 풍선을 터트리고 시작한다고 했으므로
# 이 풍선을 터트려서 없애야 한다 즉 리스트에서 없애야하므로
# 리스트에 그 값을 없애게 되면
# 그 외의 값이 그 자리를 채우게 된다
# 이렇게 되면 리스트의 변화는 길이가 -1 된 상태이고
# 그럼 해당 인덱스의 값들은 전부 바뀌어져 있는 상태이다
# 이때 3을 뽑게 되면
# [2,1,-3,-1] 의 값만 남게 되므로 idx 가 2로 넘어가야 되는상태이다
# 그럼 2로 넘어갔을때 temp 값은 -3이 되고 그 값또한 빼게된다면
# [2,1,-1] 상태가 되면서 리스트의 길이는 3 그리고 현재의 idx = 2 + - 3 인상태 ㅇ그러면 두게를 더하게되면 -1이고 3의 더해 
# 최초로 양수인값인 2 % 3을 나눈 나머지가 인덱스가 된다 그렇게 된다면 -1인 값이 temp로 리턴이ㅗ디고
# -1을 가지고 있는 값이 index에서 팝되게 되면서
# 순서가 맞춰진다.
