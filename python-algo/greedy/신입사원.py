# 선발 시험은 1차, 2차 나눠져있다

# 서류 심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지만 않으면 선발

# 다시말해 4 2 == 4 1 둘 중에 하나라도 다르면 떨어진다.


# 1. 모든 점수가 다 크다면합격
# 2. 모든 점수가 낮거나 둘 중에 하나라도 떨어진다면 탈락

# 서류 성적순으로 나열했을때 
# [5,5], [4,1] [3,2], [2, 3], [1, 4]
# 5,4,3,2,1 등 순으로 나열이 된다.


# 2등부터는 첫번째 성적과 비교했을때 적어도 하나가 높다면 선발한다. 하지만 2등[4,1] 1등과 비교했을때 높은 성적이 없으므로 탈락

# 3등은 1,2등과 비교했을때 높은 성적이 하나라도 있으면 선발
# 3등은 1등보다 낮지만 2등보다는 높은 점수가 있으므로 선발
# [5, 5], [3, 2], [2, 3], [1, 4] 선발


# 4등은 1,2,3등보다 더 높은점수가 있다면 선발
# 5등은 1,2,3,4등 보다 더 높은 점수가 있다면 선발 면접점수 중에 4가 있으므로 선발


# 총 뽑힐 수 있는 사람 수는 리스트의 길이이므로 4명
T = int(input())
first_grade = []
second_grade = []
test_case_1 = 1
test_case_2 = 1

# 0 1
for i in range(T):
  # 케이스 첫번째 로직
  if(i==0):
    people_input = int(input())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for j in range(people_input):
      list_first = list(map(int, input().split()))
      first_grade.append(list_first)
      first_grade.sort()
    man = first_grade[0][1]
    for j in range(1, people_input):
      if man > first_grade[j][1]:
        man = first_grade[j][1]
        test_case_1 += 1
  elif(i==1):
    second_input = int(input())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for k in range(second_input):
      list_second = list(map(int, input().split()))
      second_grade.append(list_second)
      second_grade.sort()
    man2 = second_grade[0][1]
    for l in range(1, second_input):
      if man2 > second_grade[l][1]:
        man2 = second_grade[l][1]
        test_case_2 += 1
    
print(test_case_1, test_case_2)







# 시간 초과 줄이기 첫번째 시도






# 선발 시험은 1차, 2차 나눠져있다

# 서류 심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지만 않으면 선발

# 다시말해 4 2 == 4 1 둘 중에 하나라도 다르면 떨어진다.


# 1. 모든 점수가 다 크다면합격 합격한 사람빼고 그다음이 1등이됨 
# 2. 모든 점수가 낮거나 둘 중에 하나라도 떨어진다면 탈락

# 서류 성적순으로 나열했을때 
# [5,5], [4,1] [3,2], [2, 3], [1, 4]
# 5,4,3,2,1 등 순으로 나열이 된다.


# 2등부터는 첫번째 성적과 비교했을때 적어도 하나가 높다면 선발한다. 하지만 2등[4,1] 1등과 비교했을때 높은 성적이 없으므로 탈락

# 3등은 1,2등과 비교했을때 높은 성적이 하나라도 있으면 선발
# 3등은 1등보다 낮지만 2등보다는 높은 점수가 있으므로 선발
# [5, 5], [3, 2], [2, 3], [1, 4] 선발


# 4등은 1,2,3등보다 더 높은점수가 있다면 선발
# 5등은 1,2,3,4등 보다 더 높은 점수가 있다면 선발 면접점수 중에 4가 있으므로 선발


# 총 뽑힐 수 있는 사람 수는 리스트의 길이이므로 4명

import sys


T = int(sys.stdin.readline())
first_grade = []
second_grade = []
test_case_1 = 1
test_case_2 = 1

# 0 1
for i in range(T):
  # 케이스 첫번째 로직
  if(i==0):
    people_input = int(sys.stdin.readline())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for j in range(people_input):
      list_first = list(map(int, sys.stdin.readline().split()))
      first_grade.append(list_first)
      first_grade.sort()
    man = first_grade[0][1]
    for j in range(1, people_input):
      if man > first_grade[j][1]:
        man = first_grade[j][1]
        test_case_1 += 1
  elif(i==1):
    second_input = int(sys.stdin.readline())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for k in range(second_input):
      list_second = list(map(int, sys.stdin.readline().split()))
      second_grade.append(list_second)
      second_grade.sort()
    man2 = second_grade[0][1]
    for l in range(1, second_input):
      if man2 > second_grade[l][1]:
        man2 = second_grade[l][1]
        test_case_2 += 1
    
print(test_case_1, test_case_2)





# 시간초 줄이기 두번째 시도


# 선발 시험은 1차, 2차 나눠져있다

# 서류 심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지만 않으면 선발

# 다시말해 4 2 == 4 1 둘 중에 하나라도 다르면 떨어진다.


# 1. 모든 점수가 다 크다면합격 합격한 사람빼고 그다음이 1등이됨 
# 2. 모든 점수가 낮거나 둘 중에 하나라도 떨어진다면 탈락

# 서류 성적순으로 나열했을때 
# [5,5], [4,1] [3,2], [2, 3], [1, 4]
# 5,4,3,2,1 등 순으로 나열이 된다.


# 2등부터는 첫번째 성적과 비교했을때 적어도 하나가 높다면 선발한다. 하지만 2등[4,1] 1등과 비교했을때 높은 성적이 없으므로 탈락

# 3등은 1,2등과 비교했을때 높은 성적이 하나라도 있으면 선발
# 3등은 1등보다 낮지만 2등보다는 높은 점수가 있으므로 선발
# [5, 5], [3, 2], [2, 3], [1, 4] 선발


# 4등은 1,2,3등보다 더 높은점수가 있다면 선발
# 5등은 1,2,3,4등 보다 더 높은 점수가 있다면 선발 면접점수 중에 4가 있으므로 선발


# 총 뽑힐 수 있는 사람 수는 리스트의 길이이므로 4명

import sys


T = int(sys.stdin.readline())
first_grade = []
second_grade = []
test_case_1 = 1
test_case_2 = 1

# 0 1
for i in range(T):
  # 케이스 첫번째 로직
  if(i==0):
    people_input = int(sys.stdin.readline())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for j in range(people_input):
      first_grade.append(list(map(int, sys.stdin.readline().split())))

      first_grade.sort()
           
    man = first_grade[0][1]
    for j in range(1, people_input):
      if man > first_grade[j][1]:
        man = first_grade[j][1]
        test_case_1 += 1
  elif(i==1):
    second_input = int(sys.stdin.readline())
    # 1, 6
    # 0, 1, 2, 3, 4 = 5번
    for k in range(second_input):
      second_grade.append(list(map(int, sys.stdin.readline().split())))
      second_grade.sort()
    man2 = second_grade[0][1]
    for l in range(1, second_input):
      if man2 > second_grade[l][1]:
        man2 = second_grade[l][1]
        test_case_2 += 1
    
print(test_case_1, test_case_2)



