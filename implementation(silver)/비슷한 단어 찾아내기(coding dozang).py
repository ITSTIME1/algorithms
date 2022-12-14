# cat dog = 다른 문자
# cat cats = 같은 문자 길이는 다르지만 한개를 빼면 같은 문자가됨
# cat cut = u를 바꾸게 되면 같은문자
# cat cast = s를 빼면같은 문자
# cat at = c를 추가하면 같은문자
# cat acts = 문자열은 바꾸지 않는다는 가정하에 다른문자
# 길이를 맞추게 되도 cat != act 이기 때문에 다른문자


def onEditApart(s1, s2):

	# 우선 길이가 다른걸 본다면
	# cat cats 같은 것도 길이가 3 != 4로 다르기 때문에
	# cat 에 맞춘다면 s를 빼게 되면 같은 문자가 됨
	# cat cast 같은 경우도 s를 빼게 되면 cat 과 같은 문자가 됨
	# 하지만 cat acts 일 경우
	# s를 빼게 될경우 같은 문자가 되지 않아서 false
	sl, s2l = len(s1), len(s2)
	if sl != s2l:
		if sl > s2l:
			s1, s2 = s1, s2
		else:
			s1, s2 = s2, s1
		# s1 이 큰 문자이기 때문에

		for i in s1:
			if i not in s2:
				# 길이가 다름녀
				# 뺐을때 같은 문자가 되니ㅡㄴ게 있고
				# 해당 문자를 뺐는데 다른 문자가 되는게 있음
				c = s1.index(i)
				s1, s2 = list(s1), list(s2)
				del s1[c]

				if s1 == s2:
					print(True)
				else:
					print(False)
	else:
		cnt = 0
		for i in s1:
			if i not in s2:
				cnt += 1
		
		if cnt >= 1:
			check = []
			for i in s1:
				if i not in s2:
					check.append(i)
			if len(check) == 1:
				print(True)
			else:
				print(False)
		else:
			if s1 == s2:
				print(True)




print(onEditApart("cat", "dog"))
print(onEditApart("cat", "cats"))
print(onEditApart("cat", "cut"))
print(onEditApart("cat", "cast"))
print(onEditApart("cat", "at"))
print(onEditApart("cat", "acts"))