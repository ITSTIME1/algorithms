import sys


# 1부터 시작해서
# 전체 숫자 - 생성자인숫자 = 생성자가 아닌 숫자
# total_num = [_ for _ in range(1, 10000)]
# create_num = []
# # 1~9999
# for i in range(1, 10000):
# 	# 11
# 	dn = i 
# 	for j in str(i):
# 		dn += int(j)
# 	create_num.append(dn)
# 	# dn = 0
# 	# dn += i + sum(ch)
# 	# create_num.append(dn)
# 	# total_list - create_num = remain_num
# re = sorted(list(set(total_num) - set(create_num)))
# print(*re, sep="\n")



# 어떤 수의 생성자인지 찾아야 된다면 내가 N 을 분해합 했을때 만약 이 숫자가 생성자에 포함된다면
# 이 수는 그 수의 생성자.
# 전체수 - 생성자가 있는 수 = 생성자가 없는 수가 되는데
# 이게 생성자가 있는 수를 담은 리스트
cr_num = []
N = int(sys.stdin.readline())
result = 0
for i in range(1, N+1):
	num = list(map(int, str(i)))	
	result = i + sum(num)
	# 198 + 1 + 9 + 8
	# 분해합 한 수가 216 이 된다면ㄱ
	# 이 분해합 한 수는 216의 생성자가 된다.
	# 분해합이 안구해진다? 왜지 ? num = 198 이라면 합해서 216이 나오니까 그 나온 수 198을
	# cr_num 에다가 넣어줬느넫?
	if result == N:
		cr_num.append(i)
		result = 0

print(cr_num[0] if len(cr_num) != 0 else "0")
