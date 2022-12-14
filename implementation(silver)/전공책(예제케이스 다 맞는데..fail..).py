T = list(input().upper())
N = int(input())

t_len = len(T)
book = []
for i in range(N):
  m, b = input().split()  
book.append([m, b.upper()])

book.sort(key = lambda x : int(x[0]))
total, x, r_cnt = 0, 0, 0
dp = [False] * t_len

while True:
  false_index = []
  for i in range(t_len):
    if dp[i] == False:
      false_index.append(i)

  cnt = 0
  for j in false_index:
    for k in range(len(book)):
      if T[j] in list(book[k][1]):
        cnt+=1
  if False not in dp:
    x, r_cnt = 1, 0
    break
  # False 인 문자가 있지만 찾을 수 없는 문자열이면
  if len(false_index) != 0 and cnt == 0:
    x, r_cnt = 1, 1
    break
  # False 인 문자가 있고 찾을 수 있을때
  if len(false_index) != 0 and cnt > 0:
    max_index = []
    for i in range(len(book)):
      b = 0
      for j in range(len(false_index)):
        if T[false_index[j]] in list(book[i][1]):
          b+=1
      max_index.append(b)
    f_index = max_index.index(max(max_index))
    # max index 도 찾았고
    # 그럼 이 맥스 인덱스에서 원하는 문자열을 전부 True로 바꿔주면?
    check_string = list(book[f_index][1])
    for i in false_index:
      if T[i] in check_string:
        dp[i] = True
        check_string.remove(T[i])
    # swap? 
    # 튜플은 바꾸지 못하고 리스트는 바꿀 수 있으니까 여기서 바꿔주면 될거 같은데
    book[f_index][1] = "".join(check_string)
    total+=int(book[f_index][0])
# False 가 dp 에있고 false_index 가 0 이라는건 찾을 문자가 없다는거지
if x == 1 and r_cnt == 1:
  print(-1)
# 문자는 다 찾았고 False 인 문자에 없기 때문에 x= 1 인경우
elif x == 1 and r_cnt == 0:
  print(total)


# AAA
# 3
# 10000 BCD
# 20000 AAC
# 50000 DDD

# ADD
# 2
# 30 ADMMP
# 20 APPPP
# out : -1

# ADD
# 2
# 30 ADMMP
# 20 ADDPP
# out : 20
# wrong: 50

# ㅈㄴ 이상한 문제네 이거