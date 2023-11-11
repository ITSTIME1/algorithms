# numpy 에 대해서 배우는데
# numpy는 행렬연산에서 좋은 성능을 보이는 라이브러리임
# numpy의 핵심은 ndarray인데
# 선형대수, 푸리에 변환 같은 좋은 도구들도 제공해줌


# ndarray란 n차원 배열의 객체를 말함
# n차원이라고 하면 1차원 2차원을 말한다.
# 용어가나오는데
# axis : 차원의 번호
# rank : 차원의 개수
# shape : 배열의 차원을 나타내는 tuple
# 배열의 차원을 나타낸다는 것은 2행 3월 2*3짜리 행렬이라는것을의미.

# rank = 차원의개수 2차원 이면 rank = 2
# axis는 2행 axis는 3열
# shape : (2, 3)


# axes는 In numpy, dimesions are called axes라고 불리운다.


# [[0., 0., 0.],
#  [1., 1., 1.]]

# 만약에 이런 배열이 존재한다면 우리는 이걸 2차원 배열이라고 하고

# 이 배열은 axes가 2다라고 말한다.
# axes는 축의 복수형이다.

# 즉 axis 0 x축
# axis는 y축 이렇게 볼 수 있네

# axis는 plot의 축이라고 이해할 수 있다.x축y축과같
# axes는 이러한 축들을 표현하는 공간이다.

# 따라서 axes = 2라는것은 2차원 공간이라는 뜻이고
# axis0 = 행에 대항x축을의미하게되고
# axis1 = 열에 대한것을의미한다.
import numpy as np

# 0부터 14 총 15개의 정수를 
# 즉 0부터 n-1을 가진 n개의 값들을
# 3행 5열로 만들어준다.
a = np.arange(15).reshape(3, 5)

print(type(a))
# a.shape 하게되면 배열의 차원ㅇ르 나타내는 tuple이 나옴
# (n, m) => n행 m열을 의미한다.
print(a.shape)

# size를 하게 되면
# numpy객체에 대한 size는 배열 요소의 총 개수를 말한다.
# 3행 5열이기 때문에 3* 5 = 15개
# dtype은 자료형을 의미

# np.int32, np.int16등등
print(a.size)
print(a.dtype)
# 각 요소의 크기를 의미한다.
print(a.itemsize)

# ndarray를 생성하는 방법은 array(x)를 이용하는 방법과
# arange()를이용하는 방법과 linspace, zeros, ones empty, full이 존재한다.

a = np.array([1,2,3])

a = np.array([])
print(a)

# int, float이 섞여 있는 형태자나
# upcasting 되는구나
# int -> float으로 형변환이 되
s = np.array([1, 2, 3.0])
print(s)


# array는 list를 이용해서 만드는 방법이다.
d = np.array([[1, 2], [3,4]])
print(d)


# 두번째는 arange arange는 순차값을 가진 배열을 생성하는데
# arange(start, stop, step) step = interval 값을 주어
# 균등한 간격 evenly value를 리턴하게 된다.

# start = 1
# stop = 10
# interval = 2
# 즉 1부터 10까지 2칸의 간격을 이용해서 생성해 달라는것.
# 1 3 5 7 9
f = np.arange(1, 10, 0.5)
print(f)
# 1, 1.5, 2, 2.5 이렇게 생기겠네
# 1차원 배열을 생성해준다.
ff = np.arange(1, 10, 0.5)
# 만약 arange가 한개의 매개변수만 있는경우는
# 0~n-1순으로 초기화된다.
fd = np.arange(10)
print(fd)
# linspace도 마찬가지로 순차값을 가진 배열을 num개 생성하는데
# linspace는 stop을 지정해주어야함
# linspace는 start부터 end를 포함해서 생성해주고
# step을 지정해주지 않는다면, 일정 간격으로 계산해서 제공해준다.
a = np.linspace(1, 10, 5)
print(a)
# zeros(s)는 주어진 shape -> 차원을 의미하고, 이거에 따라서 0값으로 초기화된 배열을  리턴한다.
# 만약내가 shape로 2행 3열짜리를 0으로 채우라고 말하고 싶다면

s = np.zeros((100, 100))
print(s)
# s = np.ones((10, 10))
# print(s)

# empty는 말그대로 초기화되지 않은 배열을 shape 차원 만큼을 생성해주니까
# 따라서 어떤 값으로 초기화 될지는 모른다.
s = np.empty((10, 10))
print(s)

# full은 shape를 어떠한 value로 initialize하기 위한 것.
# 따라서 어떤 특정한 값으로 shape만큼 초기화 하기 위한것임.
s = np.full((10, 10), 3)
print(s)


# 난수로 ndarray를 생성하는 방법
# random.randint(start, end, size=1)
# randint는 [start, end) 범위내에서 난수를생성하게 되는데
# 즉 [start, end) => start부터 end는 포함하지 않는 범위내에서
# 정수를 1개를 임의로 생성한다.
# 만약 인수를 1개만 주었을경우는 end로인식이 되고, 한개만 지정했을 경우에는
# 0~end-1사이의 정수를 1개생성한다.
# size=1 default로 1개가 생성이 되었는데, 
# 이때 size = n으로 설정한다면, n개 또는 shape s를 주게 된다면 s만큼 난수를 발생할 수 있다.

# shape는 tuple데이터 타입으로 주어진다.
s = np.random.randint(1, 10, size=(2,3))
print(s)

# rand는 균등분포인 m행 n열의 실수를 [0, 1) 사이에서 생성한다.
# 0을 포함하고 1보다 작은 공간에서 생성한다.
# 이 또한 인수가 한개만 지정된 경우, m개의 난수를 발생시킨다.
# ex) 10 인수 한개만 지정한 경우 0을포함하고 1을 포함하지 않는 범위 내에서
# 10개의 난수를 생성한다.

# 균등 분포인 m행 n열의 실수를 [0, 1) 사이에서 생성하게 되는데
# 이와 똑같은 명령어인 np.random.random_sample(s)
# 가 있다.
s = np.random.rand(10)
# rand를 사용했을때 균등분포 [0,1)사이에서 생성되는 것을
# m행,n열 즉 2행 3열로 차원을 맞춰서 생성하라는 얘기가 된다.
s1 = np.random.rand(2, 3)
print(s1)

# random_sample을 통해서 shape s를 인수로 넘겨주고 있으며,
# 2행 3열짜리 [0,1)을 생성하라는 의미가 된다.
s1 = np.random.random_sample((2,3))
print(s1)

# rand와 randn이 있다.
# rand는 위에서 균등분포인 [0,1)사이에서 난수를 생성하는것이지만
# randn은 가우시안 정규분포 (평균이0이고, 분산이1인) m행,n열의 실수를 생성한다.
# 이것도 마찬가지로 인수가 1개만 있는 경우에는 m개의 난수를 발생시킨다.
# random.standard_normal(s): 와 동일하다 
# random.normal(a, b, s) (평균이 a이고, 표준편차가 b인) 난수를 생성하고
# shape를 줄 수 있다.

# 0 부터 n-1 까지를 난수로 생성해서 1차원 리스트 형태로 반환

a = np.arange(5)

# 0~9까지 생성하는데 이때 데이터 타입은 float형태.
b = np.arange(10, dtype=np.float32)

# start = 3.14
# stop = 5
# step = 0.25
# 즉 3.14부터시작해서 4까지 0.25씩 끊어서 생성하라는것.
c = np.arange(3.1, 5, 0.25)
print(c)

# arange와 linspace의 차이라고 하면
# end를 포함해서 생성한다는것

# 0부터 0.2까지 step 6개의 단계를거쳐서 이떄 start,end는 포함해서 6개를 생성
a = np.linspace(0, 0.2, 6)

# 즉 step만큼씩 띄워서 3.1부터 end-1까지 생성하는데
# arange(start, end, step)
# # linspace는 start를 포함 end도 포함해서 num개를 생성한다.
# linspace(start, end ,num)
print(a)

# 2행3열짜리 데이터를 초기화 되지 않은 상태의 값을 생성.
a = np.empty((2, 3)) 
print(a, '\n')
# 2행 3열짜리 1로 채워진 행렬을 생성/
b = np.ones((2, 3)) 
print(b, '\n')
# 0으로 2행3열을 생성
c = np.zeros((2, 3)) 
print(c, '\n')
# 2행3열을 np.pi numpy에서 제공해주는 pi값으로 value로 초기화
d = np.full((2, 3), np.pi)
print(d)


# end하나만 지정했을 경우 0~end-1까지 정수1개를생성.
a = np.random.randint(10)
# start, end-1 까지 정수를 1개생성.
b = np.random.randint(1, 10)
print(b, '\n')

s = np.arange(1, 5, 3)
print(s)
s = np.linspace(1, 5, 3)

s = np.arange(10, step = 2)
print(f"{s} 이이잉")
s = np.random.randint(10, size=3)
print(s)