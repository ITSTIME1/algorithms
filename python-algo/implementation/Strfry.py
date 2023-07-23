import sys

N = int(sys.stdin.readline().rstrip())
imposi = "Impossible"
posi = "Possible"
for _ in range(N):
	a, b = sys.stdin.readline().rstrip().split()
	a = "".join(sorted(a))
	b = "".join(sorted(b))
	for i in range(len(a)):
		if a[i] != b[i]:
			
			flag = False
			break
		else:
			flag = True

	if flag == False:
		print(imposi.replace('""', ""))
	else:
		print(posi.replace('""', ""))


# 다른 사람 풀이

# import sys
# input = sys.stdin.readline

# N = int(input())

# for _ in range(N):
#     a, b = input().split()
#     print("Possible" if sorted(a) == sorted(b) else  "Impossible")