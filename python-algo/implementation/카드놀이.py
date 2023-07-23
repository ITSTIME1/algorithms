# A, B 숫자 카드를 받고
# 10라운드를 돌면서
# A, B의 숫자를 비교해서 
# 큰 숫자를 가진 A,B 둘중에 한명의 점수를 올리고
# 승자 +3 패자 +0

# if) 비겼다면 A,B +1 D 추가


# 그렇게 10라운드가 다 돌고나서
# 해당 점수를 비교했을때
# 점수가 높은 사람의 알파벳을 출력하고
# 만약 숫자가 같다면
# 제일 마지막 라운드에서 이긴 사람이 승리하는데 ( 이걸 어떻게 구하나)
# 위 경우들을 제외하면 무승부 D
# 즉 모든 경우가 다 같아서 마지막 라운드가 D 인경우
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ac, bc = 0, 0
total = []
for i in range(10):
	# 큰 숫자를 가진 상대방의 점수
	if A[i] > B[i]:
		ac+=3
		total.append("A")
	elif A[i] < B[i]:
		bc+=3
		total.append("B")
	elif A[i] == B[i]:
		ac+=1
		bc+=1
		total.append("D")


print(ac, bc)
if ac > bc:
	print("A")
elif ac < bc:
	print("B")
elif ac == bc:
	# 마지막 경기를 찾아야 되는데
	index = 0
	result = 0
	for i in range(len(total)):
		if total[i] == "D":
			continue
		else:
			index = i

	if index == 0:
		result = "D"
		print(result)
	else:
		result = total[index]
		print(result)




