n, k = map(int, input().split())

coin_value_list = []
coin_deliver = 0

for i in range(n):
  coin_list = int(input())
  coin_value_list.append(coin_list)

  coin_value_list.sort(reverse=True)
for coin in coin_value_list:
  coin_deliver += k // coin
  k %= coin

print(coin_deliver)