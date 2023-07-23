# N 이라는 카드 묶음이 정렬된 상태로 되어있다

# ex) 10, 20, 30장

# 두묶음식 골라서 합쳐나간 뒤 비교 횟수를 구하여라
# 10+20 = 30
# 30+30 = 60
# 총 비교횟수는 90번
# 10+20 = 1번 비교했고
# 30+30 = 2번 비교했고


# 큰 수랑 비교할 수록 비교값이 증가한다.

# 즉 효율적으로 할려면
# 입력값을 받은걸 정렬시킨다음(값이 작은 순서대로)
# 입력받은 묶음의 개수만큼 반복시켜 비교한다


# 3장이면 총 3번 반복할텐데 먼저 리스트에 있는 가장 작은 값을 기준으로 한다.
# 그 값이 기준이되고 처음에 그 다음 값을 더해준다
# 그럼 그 더한 값이 회수가 되고
# 그 회수를 이제 이전 변수에 저장해뒀던 값이랑 변경한다
# 그리고 나서 다음거랑 비교하면 30+30 즉 앞서 더했던 값에 남은 값을 더해주니 60이 된다

# 그럼 초반에 값이 나왔던 값을 따로 변수에 저장해주고
# 이후에 더했던 값이 나오면 그 값이랑 따로 저장한 회수값이랑 더해 결과를 도출한다.



# 카드 묶음의 개수
N  = int(input())

# 카드 묶음 장수 입력
N_list = []
previous_card = 0
first_result = 0
second_result = 0
for i in range(N):
  N_list.append(int(input()))
  N_list.sort()

# 두번 반복 0,1
for j in range(len(N_list)-1):
  # 두번 반복
  if(j == 0):
    previous_card = N_list[j]
    N_list.pop(j)
    first_result += previous_card + N_list[j]
  elif(j == 1):
    N_list.pop(0)
    second_result = first_result + N_list[0]

print(second_result+first_result)