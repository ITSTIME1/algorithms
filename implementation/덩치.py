# 1등과 꼴등
# 그 외 나머지는 2등
# import time
# start = time.time()

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]
check_array = [2] * N
w = []
h = []
for i in range(len(array)):
	# 몸무게
	w.append(array[i][0])
	# 키
	h.append(array[i][1])
# 오름차순 큰 값대로
# 내림 차순 작은 값대로
own_w = max(w)
own_h = max(h)

# 제일 작은 값들만
lower_w = min(w)
lower_h = min(h)


position = 0
for j in range(len(array)):
	# 가장 큰 값이라면
	if(array[j][0] == own_w and array[j][1] == own_h):
		position = j
	# 가장 작은 값이라면
	if(array[j][0] == lower_w and array[j][1] == lower_h):
		check_array[j] = N
check_array[position] = 1
str_list = list(map(str, check_array))
print(" ".join(str_list))


# print(f"{time.time() - start:.2f} sec")



# t = int(input())
# a = []
# for i in range(t):
#     a.append(input().split())
# a_len = len(a)
# seq = []
# for i in range(a_len):
#     cnt = 1
#     for j in range(a_len):
#         if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
#             cnt += 1
#     seq.append(cnt)
# for i in seq:
#     print(i, end=' ')


# runtime error