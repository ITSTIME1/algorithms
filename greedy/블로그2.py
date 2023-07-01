
import sys
from collections import Counter
import copy
input = sys.stdin.readline

n = int(input())
col = list(map(str, input().strip()))
dic = Counter(col)

mainColor = [k for k ,v in dic.items() if max(dic.values()) == v][0]
s = [col[i] for i in range(n) if col[i] != col[i-1] and col[i]!=mainColor]
print(len(s)+1)

