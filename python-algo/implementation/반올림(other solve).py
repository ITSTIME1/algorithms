a = int(input())
array = []

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

for i in range(0,a):
  array.append(input())

result = []
for i in range(0, len(array)):
  length = len(list(str(array[i])))
  k = array[i]
  for j in range(1, length):
    if str(k)[length-j:length-j+1] == '5':
      k = str(int(k) + 10**(j-1))
      print(k)

    # round 함수는 오사오입 법칙을 따르는데
    # 0~4 까지의 수면 반올림을 할 수 없기 때문에
    # 무조건 내림(*버림)을 하게 되지만
    # 5라면 앞자리 수가 홀수냐 짝수냐에 따라
    # 다르게 적용된다
    # 예를 들어 2.5 ,3. 5
    # 두개의 숫자중 소수점 첫째자리에서 반올림 한다고 했을때
    # 0.5 자리에서 반올림을 하게 되는데
    # 이때 앞자리가 짝수라면 내림 버림을 하게 된다
    # 홀수라면 올린다
    # 이런것 때문에
    # 반올림 함수를 만들거나
    # 혹은 10제곱을 해줘서 만들어준다
    k = round(int(k),-j)
    print(k)
  result.append(k)

for i in range(0, len(result)):
  print(result[i])


# 반올림 함수 직접 만들기
# round 함수는 보통 실수형 자료형이 아닌
# 정수형을 반올림 할 때 오사오입 법칙을 따르는데
# 이건 우리가 기존에 알고 있던 반올림과
# 거리가 먼 것을 알 수 있다
# 때문에 반올림 할 때는 함수를 직접 만들어서
# 사용한다.

# i = 0 이라는건 소수점 첫째자리 라는 뜻
def fun_round(num, i=0):
  num = num * 10**(i)

