# 각 반복문을 10번 돌면서
# a 와 b 에서 카드 하나씩
# 뽑아들고
# 해당 뽑아든 카드를 가지고 와서 비교해서
# 이겼으면 acount += 1
# bcount+=1 해주고
# 비겼으면 d 로 그냥 pass

# 마지막에 acount bcount 중 누가 더
# 많은 승리를 했는지 판단.
a = list(map(int, input().split()))
b = list(map(int, input().split()))


N = 10
acount = 0
bcount = 0
for i in range(N):
	aCard, bCard = a[0], b[0]
	
	if aCard > bCard:
		acount+=1
	elif aCard < bCard:
		bcount+=1
	else:
		pass

	a.pop(0)
	b.pop(0)
if acount > bcount:
	print("A")
elif acount == bcount:
	print("D")
else:
	print("B")
