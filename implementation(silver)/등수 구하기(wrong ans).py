
# 등수니까
# 만약 새로 들어온 값이 리스트 내에 존재하고
# 그럼 그 수의 인덱스를 가지고 온 뒤
# 그 인덱스의 + 1 하게 되면 등수이다
# 단
# 랭킹 리스트에 올라갈 ㅅ ㅜ있는 점수 p개가 주어지는거니까

# 즉 만약 p= 10 이라면
# 10개의 수만 랭킹 리스트에 올라갈 수 있다
# 둘재 줄에는 현재 랭킹 리스트에 있는 점수가
# 비오름차순으로 주어진다
# 만약 p개의 숫자가 넘도록 수가 있다면
# 새로 들어온 수가 리스트 내에 있는지 보고
# 만약 새로 들어온 점수가 기존 점수보다 크다면
# 리스트에 꽉 차서 올라갈 수 없다라는건
# 그 점수가 들어갈 수 없을 정도로 작거나 혹은
# 같은 점수인데도 그 점수가 가장 최하위에 있다면
# 들어갈 수 없다

# 수 들이 주어지고 
# 그럼 점수 n 개가 비 오름차순 = 내림 차순으로 주어지다는 말이되는거고
# new_num 새로운 숫자가 들어오며, 랭킹 리스트에는 p개의 숫자만 들어갈 수 있다 
n, new_num, p = map(int, input().split())
ranking = list(map(int, input().split()))
print(ranking)
r, x = 0, 0
if len(ranking) == 0:
	r = 1
	x = 1
if len(ranking) > p:
	r = -1
	x = 1

if x != 1:

	for i in range(len(ranking)):
		if len(ranking) >= p:
			if new_num in ranking:
				z = ranking.index(new_num)
				if z == p-1:
					r = -1
				else:
					ranking.insert(z, new_num)
					if len(ranking) > p:
						x = len(ranking) - p
						for i in range(x):
							ranking.pop()
					r = z
	
			else:
				for i in range(len(ranking)):
					if ranking[i] < new_num:
						ranking[i] = new_num
						r = i+1
						break
				break
				
	
		# 만약 랭킹 리스트가 꽉차있지 않다면
		else:
			# 만약 새로운 숫자가 리스트에 없고
			if new_num not in ranking:
				for i in range(len(ranking)):
					if ranking[i] > new_num:
						if i == len(ranking)-1:
							ranking.append(new_num)
							r = len(ranking)
							break
				break
			# 만약 새로운 숫자가 리스트에 있다면
			else:
				v = ranking.index(new_num)
				r = v+1
				break

print(r)

# 11 500 10
# 600 600 600 600 600 600 600 600 600 600 400