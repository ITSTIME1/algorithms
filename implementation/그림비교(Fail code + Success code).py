# N = int(input())

# arr = [[input() for _ in range(5)] for _ in range(N)]

# count = []
# for i in range(len(arr)):
# 	check = arr[i]
# 	cnt = 0
# 	for j in range(len(check)):
# 		# ..X.... 한개씩 가지고온다.
# 		if i != len(arr)-1:
# 			if check[j] != arr[i+1][j]:
# 				cnt+=1
# 		else:
# 			if check[j] != arr[i-1][j]:
# 				cnt+=1 
# 	count.append((i+1, cnt-1))

# count_list = sorted(count, key = lambda x : (x[0], x[1]))
# print(*count_list[0])


def check(i,j):
	cnt = 0
	for a in range(5):
		for b in range(7):
			if n_list[i][a][b] != n_list[j][a][b]:
				cnt += 1
	return cnt

n = int(input())
n_list = []
for i in range(n):
	i_list= []
	for j in range(5):
		i_list.append(list(input()))
	n_list.append(i_list)

min_n = 36
for i in range(n):
	for j in range(i+1,n):
		num = check(i,j)
		print(num)
		if num < min_n:
			a,b = i,j
			min_n = num

print(a+1,b+1)