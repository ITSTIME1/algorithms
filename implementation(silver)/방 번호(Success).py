# # 문제 분석
# # 플라스틱 세트에는 0~9번까지의 수를 한 셋트로 판다
# # 다솜이의 방 번호가 주어졌을때 필요한 세트의 개수

# # 조건이 6 은 9를 뒤집을 수 있고 9는 6을 뒤집을 수 있다

# 9999
# 0~9 중 9가 있다면 9를 하나 써주면 될거고 그럼 한세트에서 9는 사용하게 된 것이고
# 그 다음 수가 9라면 9는 이미 하나 사용했기 때문에 6을 사용할 수 있으니 6을 사용하고
# 그다음 숫자가 또 9가 왔는데 9 와 6 모두 사용했다라면 셋트의 개수를 하나 늘려주고
# 9 와 6의 개수를 초기화 시켜주면 다시 사용할 수 있으며 세트의 개수는 늘어난다
# 왜냐하면 한세트가 추가 된다면 1도 두개 2도 두개 3도 두개

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0 ,1, 2, 3, 4, 5, 0, 7, 8, 0]
# 6, 9를 제외한 나머지 숫자들은 하나씩 더 생긴거고
# 그랬을대 9999 값은 총 2개의 셋트가 필요함



# 122
# 6과 9가 아니기 때문에 1을 사용할 수 있으면 1을 사용해주고
# 2를 사용할 수 있으면 2를 사용해주고
# 또 2를 가지고 왔을때 2는 이미 사용했기 때문에 셋트가 하나더 필요하다
# [0, X, X, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 그럼 1과 2는 는 한번씩 더 사용할 수 있으며 나머지 숫자들은 총 2번까지 사용가능하다

# 12635
# 같은 경우 1,2,6,3,5 전부 한 셋트에서 사용할 수 있기 때문에
# 사용해준다면 1셋트에서 끝낼 수 있음

# 888888
# 6과 9를 제외한 나머지 숫자들은 다른 숫자를 사용해서 차감할 수 없기 때문에
# 8을 한번 사용하게 되면 다음 숫자에서 8이 왔을때
# 어쩔 수 없이 셋트의 개수를 늘려주어야 한다
# 그렇게 된다면 총 6개의 셋트가 필요하며
# 셋트가 추가될수록 해당 수를 제외한 나머지 숫자들은 셋트가 증가한 수만큼 수가 증가하게 된다



# 이라면
# 122
# [0: 1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1]

# 1을 사용한다면 1을 차감
# [0: 1, 1:0, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1]
# 2를사용한다면 2를 차감
# [0: 1, 1:0, 2:0, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1]

# 또 2를사용하려고 봤는데 차감시킬 수 있는 상태가 아니기 때문에
# 셋트추가
# [0: 2, 1:1, 2:1, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2]
# 하게 된
# 음 뭔가 간단한거 같은데..
import sys
# 다솜이의 방이 주어지고
n = list(map(int, sys.stdin.readline().strip()))
dic = {}
for i in range(10):
	dic[i] = 1

set_cnt = 1
for i in range(len(n)):
	# 만약 값이 6또는 9라면
	# 각각의 값이 0 이 아니라면 하나 차감하고
	# 그 값이 6 또는 9라면
	c = n[i]
	if c == 6:
		if dic[c] != 0:
			dic[c] -= 1
		else:
			if dic[9] != 0:
				dic[9] -= 1
			else:
				set_cnt += 1
				for i in dic.items():
					dic[i[0]] += 1
				if dic[c] != 0:
					dic[c] -= 1
	elif c == 9:
		if dic[c] != 0:
			dic[c] -= 1
		else:
			if dic[6] != 0:
				dic[6] -= 1
			else:
				set_cnt += 1
				for i in dic.items():
					dic[i[0]] += 1
				if dic[c] != 0:
					dic[c] -= 1
	else:
		if dic[n[i]] != 0:
			dic[n[i]] -= 1
		else:
			n_i = n[i]
			# 세트수 올려주고
			set_cnt += 1
			# 세트수 올려준 만큼 번호 생성해주고
			for i in dic.items():
				dic[i[0]] += 1
			if dic[n_i] != 0:
				dic[n_i] -= 1
print(set_cnt)




