# 테스트 케이스
# 2 => 0, 1
T = int(input()) 



for i in range(T):
  p = int(input())
  for j in range(p):
    s, m = map(int, input().split())
    





# 테스트 케이스
# 2 => 0, 1
T = int(input()) 

people_grade = []
count = 0

for i in range(T):
  p = int(input())
  for j in range(p):
    # 각 테스트 케이스 마다 점수들을 리스트로 입력받는다.
    
    grade = list(map(int, input().split()))
    people_grade.append(grade)

    # 서류성적 순위대로 정렬
  mgrade = sorted(people_grade, key = lambda x : x[0])


    
    # 서류성적으로 나열한 것 중에서 가장 큰 값
  previous_grade = mgrade[0][1]

    # 5 지만 리스트로는 4니까 0, 1, 2, 3
  for k in range(p):
    if(previous_grade > mgrade[k][0]):
      count+=1
      previous_grade = mgrade[k][0]
    
    else:
      pass
    
print(count)
  
    # 적어도 하나가 다른 지원자의 성적보다 떨어지면 선발 안함


