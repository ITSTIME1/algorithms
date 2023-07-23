# # 이 문제는 영어 문장을 만드는 문제인데
# # 조건이있다



# # 1 번을 누르면 공백
# # 같은 숫자의 있는 문자를 입력해야 될 경우 ex)AC가 2번에 다 있다고 한다면
# # A를 입력하고 나서 w초 만큼 기다렸다가 C를 입력하면 된다 이 과정에서 A B C 가 있기 떄문에
# # C를 입력할려면 A를 입력했으니 p가 한번 추가되고 10초가 추가된 뒤 A B C C까지의 위치번을 눌러야 한다
# # C까지의 위치번이라는건 C의 인덱스+1 이라는 말이고
# # 만약 AB 라고 한다면 P+10+2가 추가된다.
# # 공백을 연속으로 입력할때는 기다릴 필요 없다 ( 오직 같은 패드의 문자를 입력해야 될 경우)


# 시간 복잡도 O(N^2)
key = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
                ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

p, w = map(int, input().split())
word = list(input())
# 총시간
last = ""
cnt = 0
# 각각의 키패드 번호
for i in range(len(word)):
	# 단어를 하나 가지고오고
	check = word[i]
	check_key = 0
	# 키패드 값확인
	# 가지고온 값의 키패드 값 확인
	cur_index = 0 
	lat_index = 0
	if check == " ":
		# 공백이 연속인지 확인
		cnt+=p
		last = check
		continue

	for j in range(len(key)):
		if check in key[j]:
			check_key = key[j].index(check) + 1
			cur_index = j+1
		if last in key[j]:
			lat_index = j+1
	
	if cur_index == lat_index:
		cnt += (w+(p*check_key))
	# 키패드가 다르다면
	else:
		cnt += p*(check_key)

	# 마지막 값을 교환
	last = check
print(cnt)