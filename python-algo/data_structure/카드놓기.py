from collections import deque

N = int(input())
li = deque(map(int, input().split()))
after = deque(range(1, N+1))
before = deque()

while li:
    t = li.pop()
    a = after.popleft()
    print(t, a)
    if t == 1:
        before.appendleft(a)
    elif t == 2:
        before.insert(1, a)
    elif t == 3:
        before.append(a)
    print(before)
print(*before)