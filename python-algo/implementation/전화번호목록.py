import sys
input = sys.stdin.readline


t = int(input())

for i in range(t):
	n = int(input())

	number = [input().strip() for i in range(n)]
	# 문자열 정렬할때 문자열들이 오름차순으로 정렬이 되지만
	# 
	number.sort()
	# 이생각을 못했네..?
	ori = True
	for j in range(len(number)-1):
		stand = number[j]
		# 아까걸 으용해본다면
		if len(stand) > len(number[j+1]):
			continue

		# 접두어 끼리가 같다면 일관성이 없는거겠지
		if stand == number[j+1][:len(stand)]:
			ori = False
			break

	if not ori:
		print("NO")
	else:
		print("YES")
	



# 전화번호를 받을때 
	# 그냥 모든 길이만큼 다 짤라볼까?
	# 좋은걸 하나 배웠네
	# 숫자들이 Character 형태로 저장되어 있는경우
	# sort()를 하게 될 경우 크기 순서대로 정렬되는 것이 아니라
	# 숫자의 순서대로 정렬이 된다는것
	# 따라서 이 문제 같은경우 숫자의 순서대로 정렬이 된다고 한다면
	# 9991
	# 912
	# 이와 같은 경우 9는 같지만 1이 그다음로 먼저 오기 때문에 순서는 912, 9991로 되지만
	# 9991
	# 9994
	# 와 같은 경우 세자리 999까지는 같기 떄문에
	# 접두어일 확률이 높아진다.
	# 한 숫자 하나하나가 접두어가 될 확률이 많아지게 하기 때문에
	# 그러한 확률을 최대한 만들어두고 탐색하는 것 이 문제에 핵심이네
	# 그래서 999까지는 똑같게 되고 1이 먼저 오기 때문에
	# 접두사를 i, i+1 찾게될 확률이 높아진다.