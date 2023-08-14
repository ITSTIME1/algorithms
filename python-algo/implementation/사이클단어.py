
import sys
input = sys.stdin.readline


n = int(input())

a = [input().strip() for _ in range(n)]

# 단어들을 받아올때
# 해당 단어들을 0 부터 끝까지 읽어보면 될거 같으넫
# 그래씅ㄹ대 해당단어랑 맞으면 되는거고
first = a[0]
len = len(first)
li = []

for i in range(len):
 	remain = (i + len) % len
 	word = first[i:len] + first[:remain]

 	print(word)
 	li.append(word)

print(li)
