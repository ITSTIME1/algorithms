
# 4
N = int(input())
# 2 3 1
load_length = list(map(int, input().split()))

# 5 2 4 1
oil_price = list(map(int, input().split()))


# 1.처음엔 기름이 없기 때문에 기름을 넣고 시작한다
# 2.기름 값의 최소로 구할려면 적은 지역에서 많이 넣고 가야된다.
# 3.이전 가격과 비교 했을때 적은 가격이라면 이전 가격에서 다른 거리의 길이 만큼 곱해준다.

# 기름을 넣고 시작한다 기름은 첫번재 지역에서 넣고 가야 되니까
# 첫번째 지역의 기름은 oil_price[0]이 된다.
first_price = oil_price[0]
result = 0

# 0,1,2 3번
# 가는 거리 만큼 반복시켜주고
for i in range(len(load_length)):

  # 기준이 5니까
  # 5 <= 5
  # 5 <= 2
  if(first_price <= oil_price[i]):
    result += first_price * load_length[i]

  else:
    first_price = oil_price[i]
    result += first_price * load_length[i]

print(result)

