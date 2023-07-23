# 1부터 시작해서
# 전체 숫자 - 생성자인숫자 = 생성자가 아닌 숫자
total_num = [_ for _ in range(1, 10000)]
create_num = []
# 1~9999
for i in range(1, 10000):
	# 11
	dn = i 
	for j in str(i):
		dn += int(j)
	create_num.append(dn)
	# dn = 0
	# dn += i + sum(ch)
	# create_num.append(dn)
	# total_list - create_num = remain_num
re = sorted(list(set(total_num) - set(create_num)))
print(*re, sep="\n")
# result  = list(set(total_num) - set(create_num))
# print(*result, sep="\n")