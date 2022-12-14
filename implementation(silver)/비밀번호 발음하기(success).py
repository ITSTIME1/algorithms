# 단어에 모음이 있는지 확인.
# <%s> is acceptable % (string)
# <%s> is not acceptable % (string)

# 3개씩 탐색
# 
excep_word = ["a", "e", "i", "o", "u"]
# <eep> is not acceptable
# <houctuh> is not acceptable

while True:
	string = input()
	if string == "end":
		break
	# 길이 5
	else:
		cnt = 0
		# 단어에 모음이 포함되어 있다면
		for i in list(string):
			if i in excep_word:
				cnt+=1
				break

		if cnt == 1:
			if len(list(string)) == 1:
				print("<%s> is acceptable." % string)
			else:
				x = 0
				for i in range(len(list(string))-2):
					mo, za = 0, 0
					word = string[i] + string[i+1] + string[i+2] 	
					for j in range(len(list(word))):
						if word[j] in excep_word:
							mo += 1
						else:
							za += 1
					#[pto]
					if mo == 3 or za == 3:
						x = 3
						break
					# 저 위 경우 제외하고 자 2 모 1 혹은 모 1 자 2
					else:
						# 모음 2개가 혹은 자음 2개가 연속인지
						# 확인하고 혹은 같은 연속이 아니라 ee oo 인지
						for c in range(len(list(word))-1):
							# 같은 글자가 인지
							# jj ss
							# 같은 글자가 연속 두번이 오는지
							if word[c] == word[c+1]:
								if word[c] + word[c+1] == "ee" or word[c] + word[c+1] == "oo":
									x = 0
								else:
									# 같은 데 ee 나 oo가 아니면
									# jj 이런 경우
									x = 3
									break
							else:
								x = 0

						if x == 3:
							break
				if x == 3:
					print("<%s> is not acceptable." % string)
				else:
					print("<%s> is acceptable." % string)
		else:
			print("<%s> is not acceptable." % string)