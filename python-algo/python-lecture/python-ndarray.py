# # ndarray는 다차원 배열 객체
# # 같은 종류의 데이터만 배열에 담을 수 있음.

# # 용어 axes = 차원의 번호
# # rank = 차원의 개수
# # shape : 배열의 차원을 나타내는 tuple

# # rank = 2 라고 하는것은 차원이 2다라고 말하는것
# # axis = 2행 axis는 3열


# import numpy as np


# # 1차원 배열 생성
# # array로 생성이 가능
# a = np.array([1,2,3,4,5])
# print(a)

# # array안에 들어가는 인자는
# # 초기화된 리스트를 넣어준다.
# # 만약 빈리스트를 넣어주게 된다면 빈 리스트를 가진 객체가 생성이 되는것.
# b = np.array([])
# print(b)

# # arange()함수로도 생성할 수 있는데
# # arnage() 같은 경우 start, end, step
# # 순차값을 가진 배열을 생성해줌
# # 그래서 이때 x에 인자를 하나만 지정할 경우 end로 들어가게 되고
# # 0~ n-1까지의 배열을 생성하게 됨
# c = np.arange(10)
# # 이렇게 인자를 넘겨주게 된다면
# # start = 100, end = 200
# # 이고 step은 따로 주지 않았기 때문에 1씩 증가하는 순차값이 생성되게 되는데
# # 이때 주의해야 하는건 start는 포함하지만 end는 포함하지 않는 [start, end) 형식이라는걸 기억해야됨
# c = np.arange(100, 200)
# print(c)

# # 이건 step을 3으로 주는것
# # 100~200까지 3씩 증가하면서 생겨남
# c = np.arange(100, 200, 3.2)
# print(c) 
# print()

# # arange 같은 경우에는 [start, end ) 끝을 포함하지 않았지만
# # 만약 끝을 포함하고 싶다면 [start, end] 이런식이 되고 싶다면
# # linspace를 사용하면 된다.
# # linspace같은 경우 순차값을 생성한다는건 arange와 동일하다.
# # 단 step을 자동으로 결정한다.

# # 또한 linspace는 step을 자동으로 결정하기 때문에
# # stop값을 지정해주어야 한다.
# c = np.linspace(10, 20)
# print(c)

# # 자동으로 계산해서 넣어준다. 기본적으로 start, end를 포함한 상태로


# # 만약 배열 객체의 요소들을 전부 0으로 채우고 시팓면 zeros를 사용한다.
# # 이때 zeros() 함수 같은 경우에는 shape를 받게 된다.
# # shape는 차원을 받게 되는데 인수로 넘겨 받은 차원 만큼 zero요소를 포함한 배열을 생성하게 되는 것이다.
# # 예시로 (2,3 )을 넣게 된다면 2행 3열 짜리를 생성한다.


# linspace는 start, end, num num은 여기서 생성할 개수를 의미.
# array = np.linspace(10, 20)
# print(array)
# 배열 = np.zeros(array.shape)
# print(배열)

# # 마찬가지로 어떤 배열을 1로 채우고 싶다면 ones를 사용하면된다.
# # ones도 shape 즉 차원을 받기 떄문에
# # zeros에 넘겨준 인자와 같이 똑같이 넣어주게 된다면 해당 차원 만큼 1의 요소를 지닌 배열이 생성된다.


# # 2행 3열 짜리 1로 채운배열으 생성하라는것.
# array1 = np.ones((2,3))
# print(array1)

# # 만약 어떤 값이 들어가 있든지 상관없는 초기화되지 않은 배열을 생성하고 싶다면
# # empty를 이용한다.
# # empty는 어떠한 값으로 초기화 된게 아닌 그저 shape만 넘겨 초기화 되지 않은 인수들을 가지고 있는 객체들이ㅏㄷ.
# # 결국 쓰레기값이 들어가 있는 것이기 때문에, 이후 별도의 처리가 필요하거나 아님 쓰레기값을 가진 배열을 만들 목적이라면 empty를 사용한다.

# c = np.empty((2, 3))
# print(c)

# # 그럼 그와 반대로 초기화되지 않은 배열이라면 초기화 시킨 배열도 만들 수 있다.
# # full(s, value) 를 이용하게 된다면 차원 만큼 value를 가진 값으로 초기화 할 수 있다.

# s = np.full((2, 3), 3)
# print(s)


# 난수 생성방법
# random.randint(start, end, size= 1)
# randint함수를 사용해서 정수중 난수 size개를 뽑는 것을 만들 수 있다.
# start, end 를 지정한다면 end는 포함하지 않는 상태에서 size개를 뽑는다.

# 물론 인수가 한개라면 당연히 endㅗㄹ 들어가게 되고 end는 포함하지 않기 때문에 start, end - 1만큼의 수들중에서 난수가 발생될거라는건 알 수있고
# 이때 randint같은 경우 size = 무조건 n이 아니어도 되고, size가 shape 객체여도 된다.
# 따라서 size에 shape를 주게 되는 경우 shape객체 만큼의 난수가 발생된다는것이다.

import numpy as np
array = np.arange(10, 50, 3)
print(array)
random_randint = np.random.randint(10, 20, size=array.shape)
print(random_randint)


# 그다음 균등분포인 M행 n열의 실수를 [0, 1) 사이에서 생성
# np.random.rand(m, n) 인데 인수가 1개만 있는 경우에는 m개의 난수 발생.
# random.random_sample(s) = 동일한결과 임 단 shape s 를 튜플로 제공 그냥 m행 n열을 shape로 주게 된다는거지 ㅜ머

# 균등 분포라고하는것은 분포가 특정 범위 내에서 균등하게 나타나 있을 경우를 가리킨다.
# 즉 특정 범위 내에서 균등하게 값이 나타난다고 하면되겠네

# 가우시안 정규분포(평균이 0 이고 분산이 1인 ) m행 n열 의 실수를 생성한다.
# np.random.randn(m, n)
# 이렇게 생성하게 되는데 이도 마찬가지로 인수가 1개일경우 m개의 난수를 생성한다.
# 
a = np.random.randn(10,10)
print(np.random.standard_normal(a.shape))
# nomal함수는 평균이 a이고, 표준편차가 b인 shape s 의 실수를 생성할 수 있음
# 즉 평균과 표준편차를 조절할 수 있다는것
print(np.random.normal(10, 5, a.shape))













