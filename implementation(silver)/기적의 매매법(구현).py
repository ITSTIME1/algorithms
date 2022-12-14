# 보유현금
money = int(input())
# 1 주당 주가 리스트
stock = list(map(int, input().split()))

# 준혁이의 스톡, 준혁이의 돈
# 성민이 스톡, 성민이 돈
jun_stock, jun_money = 0, money
sung_stock, sung_money = 0, money 

for i in range(len(stock)):
	if jun_money >= stock[i]:
		# 준현이의 스톡 옵션을 최대로 갱신
		# 100 // 10 += 10 주 갱신
		# 100 - stock[i] * jun_stock
		jun_stock  += jun_money // stock[i]
		jun_money = jun_money - (stock[i] * jun_stock)
	# # 마지막날이 왔을때 
	#  1월 14일의 자산은 (현금 + 1월 14일의 주가 × 주식 수)로 계산한다.
	if i == len(stock)-1:
		jun_money = jun_money + (stock[i] * jun_stock)
		break


# 성민이 해보자
# 처음 주식의 가격을 넣어놓고
up_count, down_count = 0, 0
for i in range(len(stock)-1):
	# 가격이 상승하면 uc += 1
	if stock[i] < stock[i+1]:
		up_count += 1
		# 전량 매도
		if up_count == 3:
			# up, down 카운트 전부 초기화하고
			up_count, down_count = 0, 0
			sung_money = sung_money + (stock[i+1] * sung_stock)
			sung_stock = 0
	else:
		down_count += 1
	# 전량매수
		if down_count == 3 and sung_money >= stock[i]:
			down_count, up_count = 0, 0 
			c = sung_money // stock[i+1]	
			sung_stock += c
			sung_money = sung_money - (stock[i+1] * c)

	
if jun_money > sung_money:
	print("BNP")
elif jun_money == sung_money:
	print("SAMESAME")
else:
	print("TIMING")