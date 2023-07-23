import sys

N = int(sys.stdin.readline().rstrip())


array = [input() for _ in range(N)]

# 3 이면 0 ,1 ,2 

error = 0
group_word = 0
for i in range(len(array)):
	# happy, new, year
	word = array[i]
	for j in range(len(word)-1):
		# 두 문자가 연달아 다르다면
		if word[j] != word[j+1]:
			new_word = word[j+1:]
			if new_word.count(word[j]) > 0:
				error +=1

	if error == 0:
		group_word += 1

	# 다음 문자 검사를 위해서 error 의 개수를 초기화.
	error = 0


print(group_word)	




