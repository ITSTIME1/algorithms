# 문제분석

# 카약 문제 인데
# 우선 첫번재 예제 때문에 헷갈린 문제인데

# 우선 출력의 줄 수를 처음에 1부터 시작하고
# 그럼 처음에 출력할 줄은 1번 카약의 순서가 된다.
# 그다음 출력할 줄은 2번이기 때문에 2번 카약이 된다
# 그다음 출력할 줄은 3번이기 떄문에 3번 카약의 순서를 출력해야 한다


# 즉 줄의 번호 = 카약의 번호
# 라는 답을 도출해 낼 수 있고
# 그렇다면 hash 에 저장해서
# 해당 카약의 번호를 key 값으로 해당 카약의 순서를 value 값으로 가진다면
# 해당 카약의 번호를 출력하면 출력의 결과가 나온다



# 그렇다면 해당 카약의 순서를 정하는 일인데..
# 결승선으로부터 떨어진 거리로 측정한다고 한다.

# 아 이건 이렇게 계산해야겠따

# 먼저 1등카약부터 차례대로 정하는거야


# 2번 카약 같은 경우는 마지막 2의 숫자로부터 결승선까지의 .이 0 이기 떄문에
#{2: (0, 1), }
# 되는거고
# 그다음 읽어오는 카약의번호는 1번 그 카약의 결승선까지의 거리는 5
#{2: (0, 1), 1: (5, 2), }
# 그다음 일거옹는 카약은 3번 결승선까지으 ㅣ거리는 7
#{2: (0, 1), 1: (5, 2), 3: (7, 3), 5: (7, 3)}
# 5다음 4가 들어왔는데 그 4는 앞에 있는 3, 5, 1보다 빠르다
# 때문에 원래 4의 거리는
#{2: (0, 1), 1: (5, 2), 3: (7, 3), 5: (7, 3), 4: (3, 4),  7: (4, 5), 8: (8, 6), 9: (2, 7), 6: (7, 8)}

# pre = 0

#  2: (0, 1),
#  9: (2, 2),
#  4: (3, 3),
#  7: (4, 4),
#  1: (5, 5),
#  3: (7, 6),
#  5: (7, 6),  
#  6: (7, 6),
#  8: (8, 7),

#  1: 5
#  2: 1
#  3: 6
#  4: 3
#  5: 6
#  6: 6
#  7: 4
#  8: 7
#  9: 2 
  
# 순서대로 맞춰진다

# 딕셔너리 내에서 번호를 교환하는 작업을 거쳐야하는데 

# 되게 까다로운데
# 순서를 바꿔줘야 한다는건데
# 일단 딕셔너리를 다 받아낸다음에
# item: 기준의 따라서 정렬을 dic 정렬을 시켜주고

# 그럼 item 기준의 등수를 바꿀려면
# pre 라는 변수를 하나 등록해준다음에
# 그 변수는 item[0] 거리순으로 계속 바꿔주면서
# 만약 item[0] != pre 다르다면
# 새로들어온 item[0] 값으로 바꿔주고
# 만약 새로들어온 값이 이전 pre 값이랑 같다면
# 그럼 같은 등수기 때문에
# 그 이전 등수랑 똑같은 등수를 딕셔너리에 등록해준다


r, c = map(int, input().split())

# 십진수 체크, 거리
def decimal(kac):
	decimal = False
	for i in range(len(kac)):
		if kac[i].isdigit():
			decimal = [kac[i], len(kac[i:])-2]
	return decimal



dic = {}
for i in range(r):
	kac = input()
	# 십진수를 체크해서
	# 십진수가 존재한다면 십진수를 반환하고
	# 만약 십진수가 존재하지 않는다면 십진수를 반환하지 않고 False 를 반환한다
	num = decimal(kac)
	
	if num == False:
		continue

	if num[0].isdigit():
		dic[int(num[0])] = [num[1], i+1]


# 거리순으로 정렬
sorted_dic = sorted(dic.items(), key = lambda item : item[1])

index = 1
pre = 0
for key, value in sorted_dic:
	if value[0] != pre:
		pre = value[0]
		value[1] = index
		index += 1
	else:
		value[1] = index-1

sorted_dic.sort()
print(sorted_dic)
for i in sorted_dic:
	print(i[1][1]+1)



# 뭔가 이거 브루트 포스로 찾아야하는 느낌인데
# 난 진짜 단순하게 구현한거고
# ㄷ다시 풀어봐야 겠다