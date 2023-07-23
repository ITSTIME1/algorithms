
# 기준이 되는 점수를 잡아주다.
# 거기서 - 0.3 씩 최대 두번 해주면 해당 점수가 나온다
a_plus = 4.3
b_plus = 3.3
c_plus = 2.3
d_plus = 1.3
f = 0.0
def minus(num):
	return num - 0.6


def zero(num):
	return num - 0.3

T = int(input())
total_grade = 0
total_num = 0
for _ in range(T):
	book, grade, eng = input().split()
	# 총 학점으로 나누기 위해서 
	# grade 를 total 에 누적해서 더해줌.
	
	total_grade += int(grade)
	eng_check = list(eng)
	if eng_check[0] == "A":
		# minus, zero 로 나눔
		# 학점 * 성적  
		if eng_check[1] == "-":
			total_num += int(grade) * minus(a_plus)

		elif eng_check[1] == "0":
			total_num += int(grade) * zero(b_plus)

		else:
			total_num += int(grade) * a_plus
	elif eng_check[0] == "B":
		# minus, zero 로 나눔
		# 학점 * 성적  
		if eng_check[1] == "-":
			total_num += int(grade) * minus(b_plus)

		elif eng_check[1] == "0":
			total_num += int(grade) * zero(b_plus)

		else:
			total_num += int(grade) * b_plus
	elif eng_check[0] == "C":
		# minus, zero 로 나눔
		# 학점 * 성적  
		if eng_check[1] == "-":
			total_num += int(grade) * minus(c_plus)

		elif eng_check[1] == "0":
			total_num += int(grade) * zero(c_plus)

		else:
			total_num += int(grade) * c_plus
	elif eng_check[0] == "D":
		# minus, zero 로 나눔
		# 학점 * 성적  
		if eng_check[1] == "-":
			total_num += int(grade) * minus(d_plus)

		elif eng_check[1] == "0":
			total_num += int(grade) * zero(d_plus)

		else:
			total_num += int(grade) * d_plus
	elif eng_check[0] == "F":
		total_num += f
	else:
		pass
print("%.2f" % (round(total_num / total_grade + 10**-10, 2)))

# 사사오입 원칙을 알아야됨.(난 몰랐음.. 처음들음..)