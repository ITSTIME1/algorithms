from collections import deque
import sys

N, K = map(int, sys.stdin.readline().rstrip())
# deque 를 생성하고
array = deque(i for i in range(1, N+1))

answer = []
while array:
    for j in range(K-1):
        array.append(array.popleft())
    answer.append(array.popleft())

print("<" + ", ".join(str(k) for k in answer) + ">")
