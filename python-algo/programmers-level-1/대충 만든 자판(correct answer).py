

def check(word, arr2):
	a = []
	for i in range(len(arr2)):
		if word == arr2[i]:
			a.append(i)

	return min(a)



def solution(keymap, targets):
	arr = [list(i) for i in keymap]
	
	dic = {i: [] for i in targets}
	
	answer = []
	for i in targets:
		w = list(i)
		isActive = True
		for j in w:
			j_word = []
			for k in range(len(arr)):
				if j in arr[k]:
					if arr[k].count(j) >= 2:
						a = check(j, arr[k])
						j_word.append(a+1)
					else:
						a = arr[k].index(j)
						j_word.append(a+1)


			if len(j_word) == 0:
				answer.append(-1)
				isActive = False
				break
			else:
				isActive = True
				dic[i].append(min(j_word))

		if isActive == True:
			answer.append(sum(dic[i]))
			dic[i] = []

	return answer
