import math
from collections import deque


# 하뭐지;;
# 예제는 다 맞는데

# 현재 키패드에서 더 가까운걸 선택하는건 맞는거 같고
# 대각선으로 이동하는거 자체가 불가능한가?

# 4가지 방향으로만 이동할 수 있으니
# 만약 오른손이 3의위치에 가 있고
# 8을 눌러야 한다면8
# 누를 수 없는건가?

# 아 거리 계산에서 문제가 있었네
# 문제는 그거임
# 유클리드 거리 계산법을 사용하였는데
# 이 문제는 맨해튼 거리로만 풀 수있다

# 아 그 이유는 문제에서 상하좌우로만 이동할 수 있다고 나와 있으며
# 유클리드 거리 공식은 대각선의 직선의 거리를 계산하기 때문에
# 상하좌우로만 갈 수 있기 때문에 대각선은 못간다는게 맞다
# 맨해튼 거리로 풀어야만 풀 수 있는 문제라는 것이다.


def l(num, keypad):
    x, y = 0, 0
    isActive = True 
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == str(num):
                x, y = i, j
                isActive = False
                break
        if isActive == False:
            break
    
    return [x, y]

def distance(ori, c1, c2):
    a = abs(ori[0] - c1) + abs(ori[1] - c2)
   
    return a

def solution(numbers, hand):
    
    keypad = [["1", "2", "3"], 
              ["4", "5", "6"], 
              ["7", "8", "9"], 
              ["*", "0", "#"]]
    # 키패드를 만들어두는게 더 편할거 같은데?
    # 초기 손의 위치 설정
    # 행렬로 바꿔야 할거 같은데
    left = [3, 0]
    right = [3, 2]
    
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    
    # deque popleft 사용하기 위해서고
    answer = []
    n = deque(numbers)
    while len(n) != 0:
        # 우선 numbers 에서 숫자를 하나씩 빼오고
        num = n.popleft()
        # 해당 숫자의 좌표값을 가지고 와야 하는데
        # 왼쪽으로 눌러야 한다면
        if num in left_number:
            answer.append("L")
            c = l(num, keypad)
            left[0] = c[0]
            left[1] = c[1]
            
        # 오른쪽으로 눌러야 한다면
        elif num in right_number:
            answer.append("R")
            c = l(num, keypad)
            right[0] = c[0]
            right[1] = c[1]
        
        # 만약 어느 숫자도 왼손, 오른손으로 누르는게 아니라면
        else:
            c = l(num, keypad)
            c1, c2 = c[0], c[1]
            # left 와의 거리
            le = distance(left, c1, c2)
            # right 와의 거리
            re = distance(right, c1, c2) 
            # 어디가 더 큰지 비교
            # 왼쪽이 더 크다면
            if le < re:
                answer.append("L")
                left[0] = c1
                left[1] = c2
            # 오른쪽이 더 크다면
            elif le > re:
                answer.append("R")
                right[0] = c1
                right[1] = c2
            # 서로 같다면
            else:
                if hand == "left":
                    answer.append("L")
                    left[0] = c1
                    left[1] = c2
                else:
                    answer.append("R")
                    right[0] = c1
                    right[1] = c2

    
    
    ans = "".join(answer)
    return ans

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
a = solution(numbers, hand)
print(a)
# 내 풀이 정확성 60
# 좌표를 갱신하기 위해 난 완전탐색을 통해서 좌표를 찾았고
# 사실 좌표만 저장해두면 쉽게 구할 수 있었던 문제였다
# 좌표를 손으로 작성할까 하다가.. 안했는데 이게 효율성면에서 떨어졌고
# 그리고 아마 좌표 계산식이 뭔가 잘못된것 같다
# 맞네 거리 계산 방법이 잘못되었다
# 유클리드와, 맨해튼 거리 구하는 공식 차이가 알고리즘의 차이가 되었다

# 다른 솔루션 정확성 100
from collections import deque
import math

def solution(numbers, hand):
    
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
             4: (1, 0), 5: (1, 1), 6: (1, 2),
             7: (2, 0), 8: (2, 1), 9: (2, 2),
             "*": (3, 0), 0: (3, 1), "#": (3, 2)}
    # 초기 손의 위치 설정
    # 행렬로 바꿔야 할거 같은데
    left = '*'
    right = '#'
    
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    center_number = [2, 5, 8, 0]
    
    # deque popleft 사용하기 위해서고
    n = deque(numbers)
    answer = ""
    while len(n) != 0:
        num = n.popleft()
        if num in left_number:
            answer += "L"
            left = num
            
        elif num in right_number:
            answer += "R"
            right = num
            
        elif num in center_number:
            # 가운데 버튼을 누를땐 좌표 계산이 들어가야 하기 떄문에
            # 왼쪽 좌표와, 오른쪽 좌표를 각각 구해주고
            # 현재 좌표까지 다 구해준다음
            # 각각의 좌표를 abs()함수를 통해서 계산해주고 있다.
            # abs()절대값으로 나오는 함수다.
            currentPos = keypad[num]
            l_pos = keypad[left]
            r_pos = keypad[right]
           
           	le = math.sqrt(math.pow(currentPos[0] - l_pos[0], 2) + math.pow(currentPos[1] - l_pos[1], 2))
           	re = math.sqrt(math.pow(currentPos[1] - r_pos[1], 2) + math.pow(currentPos[1] - r_pos[1], 2))
 

            # le = abs(currentPos[0] - l_pos[0]) + abs(currentPos[1] - l_pos[1])
            # re = abs(currentPos[0] - r_pos[0]) + abs(currentPos[1] - r_pos[1])
            
            if le < re:
                answer += "L"
                left = num
            elif le > re:
                answer += "R"
                right = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                
                else:
                    answer += "R"
                    right = num

    return answer           

