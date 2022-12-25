# 문제분석

# solve
# 근데 시간초가;; 4080ms;;
# 단순 구현문제는 아닌거 같은데
# 너무 오래걸리게 푼것같다

import sys
x = int(sys.stdin.readline())

arr = [i for i in range(1, 1000000)]

x_sort = list(str(x))
x_sort.sort()

ans = []
for i in arr:
	if i > x:
		#71127
		check = list(str(i))
		new_word = []
		for j in check:
			if list(str(x)).count(j) == check.count(j):
				new_word.append(j)
		b = sorted(new_word)
		if "".join(x_sort) == "".join(b):
			ans.append("".join(new_word))

set_list = set(ans)
b = sorted(set_list)

c = 0
for i in range(len(b)):
	if int(b[i]) > x:
		c = b[i]
		break
print(c)
