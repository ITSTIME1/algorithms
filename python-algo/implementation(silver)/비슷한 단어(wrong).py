# 일단 만약 문자열의 개수가 같지 않다면
# 없는 문자가 2개 이상이면 아노딤
# 첫문자열이 DOG
# 비교문자가 DDG
# 라고한다면 없는 문자는 o 하나이기 때문에
# 중복되는 문자 중 하나를 이거랑 교체했을때 첫 문자열이랑 같다면 됨

# 하지만 DDD 라고 한다면
# 이떄는 O,G 두 문자가 들어갈 수 없기 때문에
# 이럴땐 문자열이 절대로 DOG 랑 같아질 수 없음
# 그럼...


# 문자열이 같을때는 이렇게 정리할 수 있을거 같음
# 1. 문자열의 길이가 같고, 없는 문자열이 없다면 DOG <=> GOD
# 2. 문자열의 길이가 같고, 
# 없는 문자열이 있고 그 없는 문자열의 개수가 2개이상이지 않다면
# DOG <=> GGD 가능 함 하나 밖에 없기 때문에, DOG DOL 이라면 무조건 가능
# 단 DOG GGG OD 가 없기 때문에 불가능
# DOO 없는 문자 G 하나 뿐이기 때문에 가능
# 3. 문자열의 길이가 다르다면, 문자열의 길이가 그럼 문자 하나만 뺄 수 있다는 조건때무넹
# 첫 문자의 길이랑 2이상 차이나면 안됨
# 만약 DOG 인데 DOGLL 이라면 2개의 문자가 더 있는거고
# 이런 경우 문자열이 같지 않은 문자열 두개 중 한개를 빼도 첫 문자와 비슷활 순 없음
# 만약 DOLL 이런 경우라면 문자열이 다 포함되지 않고 포함되지 않은 문자열이 2개 이상이된다면
# 비슷하게 될 순 없음 DOGL 같은 경우는 문자열은 다 포함하는데 L이라는 문자가 하나기 때문에
# 이 문자를 빼면 가능했음 

n = int(input())

word = [list(input()) for _ in range(n)]

first = word[0]
f_l = len(first)

dic = {}
for i in first:
	dic[i] = first.count(i)

# 1, 1, 1

# 2
# A
# B 
# 이 예제는 문자열이 다 포함되지 않았지만 B를 빼고 A를 넣으면 같은 문자열이 되므로 true

ans = 0
for i in range(1, len(word)):
	w = word[i]
	w_l = len(w)
	if w_l == f_l:
		cnt, not_fill = 0, []
		for i in w:
			c = w.count(i)
			if i in dic:
				# OO 이건 어떻게\?
				if dic[i] == c:
					cnt += 1
				else:
					max_num = max(dic[i], c)
					min_num = min(dic[i], c)
					cnt += max_num - min_num
			else:
				not_fill.append(i)
		if cnt >= f_l and len(not_fill) == 0:
			ans += 1
		elif cnt == 0 and len(not_fill) == 1:
			ans += 1
	else:
		max_num = max(w_l, f_l)
		min_num = min(w_l, f_l)

		if max_num - min_num <= 2:
			cnt, not_fill = 0, []
			for i in w:
				c = w.count(i)
				if i in dic:
					if dic[i] == c:
						cnt += 1
					else:
						max_num = max(dic[i], c)
						min_num = min(dic[i], c)
						cnt += max_num - min_num
				else:
					not_fill.append(i)
			# DOGL 문자열은 다 있고 길이도 2이상 차이가 나지 않고
			# 없는 문자열이 1개 인		
			# DOLL
			# 문자열이 다 없고 문자열이 다 없다면 
			if cnt >= f_l and len(not_fill) == 0:
				ans += 1

			# if cnt < f_l and len(not_fill) >= 2:


print(ans)