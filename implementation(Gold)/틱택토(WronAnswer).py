
# 그럼 한줄씩 검사했을때
# 어떤 라인이든간에 시작이 x니까 한라인에 x가 두개 이상은 있어야하낟.
# 라인에서 해당 순서에 맞는 기호가 2개이고 다른 기호가 1개라면 가능
# 무조건 라인의 시작은 x->o->x순으로 되어야한다는것 


# 1. 한 라인을 검사할때 x가 두개가 아니면 미리 탈락 
# 2. 만약 라인이 x가 두개라면 그 다음 라인이 o로 시작해야됨
# 
# 음 어떤 방식인지는 알겠는데
# 이걸 어떻게 구현하지 

# 공백이 있을때
# 입력을 하나씩 받아오고
# string != end
# 입력을 받아온걸 검사하는데


# 공백이 있을때
	# 공백이 있는 라인이고 and '놓아야 하는 문자의 개수 + 공백 1 개수가' 놓지 말아야 할 문자보다 개수가 많다면 valid
		# 다음 라인에 놓아야 하는 문자를 = 놓지 말아야 할 문자로 치환
	# 공백이 없는 라인이고 and '놓아야 하는 문자의 개수가' 놓지 말아야 할 문자보다 개수가 많다면 valid
		# 다음 라인에 놓아야 하는 문자를 = 놓지 말아야 할 문자로 치환

	# 공백이 있는 경우는 가로, 세로, 대각선을 검사했을때 하나라도 연계되어 있는 문자가 나온다면
	# 해당 리스트를 순회하면서 가로, 세로, 대각선이 "XXX" or "OOO" 하나라도 이게 나온다면 valid
	# 그렇지 않다면 invalid


# 공백이 없을때
	# '놓아야 하는 문자가' 놓지 말아야 할 문자보다 개수가 많다면 valid
		# 다음 라인에 놓아야 하는 문자를 = 놓지 말아야 할 문자로 치환
		
	# 그렇지 않다면 invalid
	# 최종적으로 라인 모두가 valid라면 해당 게임판은 나올 수 있는 최종 상태임
import sys 
input = sys.stdin.readline



while True:
	s = input().strip()
	if s == "end":
		break

	a = list(s)

	s_list = [a[i:i+3] for i in range(0, len(a), 3)]


	# 공백이 있는 경우
	if "." in a:
		must = "X"
		cnt = 0
		check = [False, False, False] 
		for i in range(3):
			re = []
			for j in range(3):
				re.append(s_list[i][j])

			x_count = re.count("X")
			o_count = re.count("O")

			# xo.
			# 2 1
			# ox.
			# ..x
			# 공백이 있는경우
			if "." in re:
				# 공백이 한개인경우 
				if re.count(".") == 1 and must == "X":
					x_count += 1
	
				elif re.count(".") == 1 and must == "O":
					o_count += 1

				# 공백이 두개인경우
				# 공백이 두개라면 ..x, ..o 이렇게 될테니까 어떤 문자가 와야되는지만 알면
				# 만약 x가 와야되는 차례라면 x가 하나는 있어야 다른 하나가 오고 o가 올 수 있기 때문에
				if re.count(".") == 2 and must == "X" and "X" in re:
					x_count += 1
	
				elif re.count(".") == 2 and must == "O" and "O" in re:
					o_count += 1

			else:
				# 공백이 없는 경우
				if must == "X" and x_count > o_count and o_count != 0:
					x_count += 1
				else:
					break
	
				if must == "O" and o_count > x_count and x_count != 0:
					o_count += 1
				else:
					break


			if must == "X" and x_count > o_count:
				check[i] = True
				must = "O"
			elif must == "O" and o_count > x_count:
				check[i] = True
				must = "X"



		if False in check:
			print("invalid")
		else:
			cnt = 0
			for r in range(3):
				first = s_list[r][0]
				re = []
				for c in range(3):
					re.append(s_list[r][c])

				if first == "X" and  "".join(re) == "XXX" or first == "O" and "".join(re) == "OOO":
					cnt += 1
			
			# 세로
			for r in range(3):
				first = s_list[r][0]
				re = []
				for c in range(3):
					re.append(s_list[c][r])

				if first == "X" and  "".join(re) == "XXX" or first == "O" and "".join(re) == "OOO":
					cnt += 1


			# 대각선
			d_1 = s_list[0][0] + s_list[1][1] + s_list[2][2]
			if s_list[0][0] == "X" and d_1 == "XXX" or s_list[0][0] == "O" and d_1 == "OOO":
				cnt += 1

			d_2 = s_list[0][2] + s_list[1][1] + s_list[0][0]

			if s_list[0][2] == "X" and d_2 == "XXX" or s_list[0][2] == "O" and d_2 == "OOO":
				cnt += 1



			if cnt == 1:
				print("valid")
			else:
				print("invalid")

	else:	
		# 공백이 없는 경우
		must = "X"
		# 여기까지 잘들어옴
		check = [False, False, False]
		for i in range(3):
			re = []
			for j in range(3):
				re.append(s_list[i][j])

			x_count = re.count("X")
			o_count = re.count("O")

			if must == "X" and x_count > o_count and o_count != 0:
				check[i] = True
				must = "O"
			elif must == "O" and o_count > x_count and x_count != 0:
				check[i] = True
				must = "X"

		if False not in check:
			print("valid")
		else:
			print("invalid")
			# 한줄씩 비교할건데
			
