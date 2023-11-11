# # # import numpy as np


# # # a = np.arange(20).reshape(4, 5)

# # # print(a.shape)
# # # # 4행 5열이니까
# # # # axes0, axes1이 존재하기 때문에
# # # # 2라고 나오는구나
# # # # ndim = rank니까
# # # # 차원의 개수
# # # print(a.ndim)
# # # print(len(a.shape))

# # # print(a.size)
# # # # 배열을 구성하고 있는 데이터 타입
# # # print(a.dtype)

# # # # 배열을 구성하고 있는 아이템들의 사이즈
# # # # 한개의 요소당 8바이트를 사용하고 있다는뜻
# # # print(a.itemsize)


# # # # 정리해보자면 axes는 차원의 번호를 말해
# # # # 만약 1차원이면 axes는 0밖에 없겠지
# # # # 2차원이면 axes는 두개가 생성이 될거고
# # # # axes가 두개면 결국 2차원이라는 소리니까
# # # # rank = 차원의 수
# # # # rank = 2라는건 2차원이라는 얘기
# # # # .shape = 튜플로 해당 배열의 차원을 리턴해줘
# # # # .dtype = 현재 원소들이 이루고 있는 데이터 타입을 보여주는거지
# # # # 현재 원소들이 이루고 있는 자료형태 다양함 int32, int64emd
# # # # 따라서 dtype은 원소들의 자료형을 말함

# # # # .itemsize = 각각의 아이템들이 차지하고 있는
# # # # 바이트 크기를 리턴함

# # # # arange() 는 마찬가지로
# # # # 선형 벡터를 만들어줄 수 있는데
# # # # ndarray를 만들어주는거지
# # # # 1차원
# # # # 즉 start, end 를 포함하지 않는 즉 end-1범위까지
# # # # 를 step수만큼 지정해준것 만큼 생성해준다는것
# # # # linspace(start, end, num)
# # # # linspace는 start부터 end를 포함해서 num개를 생성함

# # # # 이때 linspace는 step을 지정하는게 없이 개수만 지정하기 때문에
# # # # 간격은 자동으로 결정됨

# # # # zeros(s)
# # # # s만큼의 차원을 전부 0으로 채우게 되는데
# # # # s = 튜플형식으로 주어짐

# # # # ones(s)
# # # # 마찬가지로 s만큼의 크기로 주어지게 되는데
# # # # 튜플형식으로 주어짐


# # # # empty(s)
# # # # 어떠한 값도 초기화가 되지 않고
# # # # 차원의 크기 만큼 가비지 값으로 채워지게 됨

# # # # full(s, value)
# # # # 튜플의 크기 만큼 value로 채워줌

# # # a = np.arange(start, end, step)

# # # # 난수를 발생시키는것

# # # np.random.randint(start, end, size =1)
# # # # randint는 정수 난수를 발생시키는데
# # # # start, end 두개의 값 모두 지정되어 있다면
# # # # start  ~ end - 1범위까지의 정수를 size만큼 생성하게 된다.
# # # # 만약에 인수를 하나만 넘겼다면
# # # # 0~end-1만큼의 정수를 1개 생성하게 되는거야
# # # # size = n size = s도 가능해
# # # # 자연수로 지정한다면 size개수 만큼이 지정될거고
# # # # size = s 라고 한다면 shape만큼 채워질 수 있도록 발생될거니ㅏㄲ
# # # # size에 따라서 생성된다고 하는게 맞는거겠지

# # # # np.random.rand(m, n)
# # # # rand()는 균등분포를 따르는 0~1사이의 실수 1을 포함하지 않는
# # # # 사이에서 실수를 발생시켜
# # # # 또한 인수가 한개라면 m개로 간주하고 0~1사이의 실수 m개를 발생시키지.
# # # # 이때 np.random.random_sample(s)

# # # b= np.random.rand(m,n)
# # # b= np.random.random_sample(a.shape)

# # # # 가우시안 정규분포를 따른다.
# # # # 평균이 0이고 분산이 1인 m행 n열의 실수를 ㅅㅇ성.
# # # c = np.random.randn(m,n)
# # # c=  np.random.standard_normal(s)
# # # # 평균이 a이고 분산이 b인 shape s를 만듬.
# # # c = np.random.normal(a, b ,s)


# # # abc = np.arange(10, dtype=np.float)


# # # 3.1, 5, 0.25

# # # 5 - 3.1 / 0.25

# # # 1.9 / 0.25

# # # 190/25
# # # = 45/5
# # # = 9

# # # a = np.linspace(0, 0.6, 6)

# # # a = np.random.randint()
# # # a = np.random.rand() = np.random.random_sample(s)
# # # a = np.random.randn() == np.random.standard_normal() == np.random.normal(a, b, s)


# # # 배열의 기본연산에서 배열의 크기는 같아야함
# # # 배열의 기본연산에서 배열의 크기는 같아야 한다라는것.

# # # 배열의 기본연산 곱은 각 요소들끼리의 곱임
# # # 행렬의 곱은 dot()를 사용함


# # # array = np.arange(24).reshape(6,4)
# # # array1 = np.arange(24).reshape(4, 6)
# # # 6 * 6짜리가 만들어지는거지
# # import numpy as np
# # array = np.arange(24).reshape(6,4)
# # array1 = np.arange(24).reshape(4, 6)
# # a = np.dot(array, array1)
# # a[0][1] = 1
# # print(a)


# # array = np.array([1,2,3])
# # # 원소의 추가
# # array = np.append(array, 4)

# # a = np.array([[1,2,3],
# #               [4,5,6]])

# # a = np.append(a, [[7,8,9]], axis = 0)
# # print(a)
# # a = np.append(a, [[100],[100],[100]], axis = 1)
# # print(a)

# # a = np.delete(a, 0, axis = 0)
# # print(a)
# # a = np.delete(a, 1, axis = 1)
# # print(a)

# # a = np.insert(a, [0], [1,2,3], axis = 0)
# # print(a)
# # a = np.insert(a, 1, [3,3,3], axis = 1)
# # print(a)
# # # a = np.array([[1, 2, 3],
# # #               [4, 5, 6]])
# # # a = np.insert(a, 1, [-2, -2], axis = 1)
# # # print(a)
# # # matrix product
# # c = array @ array1
# # np.dot(array, array1)


# # #3면 4행 2열
# # a = np.arange(24).reshape(3, 4, 2)
# # print()

# # # 1차원으로 변경
# # b = a.ravel()
# # # broadcasting조건은
# # # 하나가 스칼라인경우 = 1차원으로 생각하면됨
# # # 두 배열중 하나의 배열이 1차원이거나 or 축의 크기가 동일한 경우

# # np.arange(3) + 5
# # # 이런식음 그럼 하나가 스칼라이기 때문에
# # # 5를 3개로 늘려서 계산
# # # 0 1 2 + [5]

# # # 3행 3열짜리고
# # # 하나가 1차원 배열일때
# # # 3행으로 늘려서 계산가능
# # np.ones((3, 3)) + np.arange(3)

# # # 3, 1 == 1, 3
# # # 이런경우도 가ㅡ능
# # # 축의 크기가 동일한 경우

# # # 3 4 2
# # # 1 4 3
# # # 이런경우는 불가
# # # 첫번재의 2열을 3열로 늘려야하는데
# # # 늘릴 것이 어떤건지 모름

# # # a = np.arange(24).reshape(3, 3, 2)
# # # b = np.arange(12).reshape(1, 4, 2)
# # # print(a)
# # # print(b)

# # # print(a + b)

# # # [[1,2],
# # #  [4,5],
# # #  [7,8]]

# # # 1면 4행 2열도
# # # [[[1,2],
# # # [1,2],
# # # [1,2],
# # # [1,2]]]
# # # 행이 부족한데 가능할까? 불가능
# # # 어떤걸 늘리는지 모르기 때문에
# # # 무조건 행이면 행 그대로를 늘려야되고
# # # 열이면 열 그대로를 늘려야함

# # # 1 1 5
# # # 1 5 1

# # # 1 5  5 1 축의 크기가 동일하므로
# # # 하나가 1인경우가 존재하니까

# # # 1열을 5열로 확산시키고
# # # 1행을 5행으로 확산시켜서
# # # 5행 5열로 만들 수 ㅇㅆ음


# # a = np.arange(10)

# # # 0~9까지 총 10개의 원소가 존재

# # print(a[3])
# # # 원소 전체를 의미함
# # print(a[:])

# # # 처음부터 0 1 2를 의미함
# # print(a[:3])

# # # 처음부터 -1마지막 -1을 의미하 
# # print(a[:-1])
# # # w즉 -2까지를 출력하게 ㅗ디는거ㅣㅈ
# # print(a[2::2])
# # # 인덱스 2부터 시작해서 step 이 2만큼 띄워서 출력

# # # 인덱스 7부터 index = 3까지 출력
# # print(a[7:2:-1])

# # # 마지막부터 처음까지 
# # print(a[::-1])

# # a = np.arange(10)
# # s = a[5:8]
# # print(s)

# # s[:] = 500
# # print(s)
# # print(a)

# # a[0:5, 1]
# # a[:, 1]


# # # numpy에서 얕은 복사가 되었었자나
# # # a[:] 이걸로 값을 변경했을때
# # # 그래서 만약 깊은 복사를하고 싶다

# # a = np.arange(0, 3.6).reshape((3,4))

# # # 3.6 - 0 / 0.3
# # # 36 / 3 = 12 

# # # 깊은 복사를 하기 위해서는 copy()를 이용한다.

# # b = a.copy()
# # print(b)

# # # fancyindexing을 사용하라 라고 한다면

# # a = np.arange(20).reshape((5, 4))

# # # 이렇게 사용하는게 fancyindex임
# # a[(0,1,2), 1]
# # # 즉 0행 1행 2행
# # # 을 선택하고 1열을 선택하라는것

# # # boolean인덱싱 이라고 하는것은
# # # 행이나 열 둘중에 하나만 적용할 수 있는개념으

# # # True인것만 가지고오는것

# # # 행에 적용할려면
# # # 행의 개수에 맞춰놓는다.

# # # 4행이라면 4개의 값을 맞춰 놓는다.
# # rows = np.array([True,False,True,False])

# # # 그럼 true인 값이 0과 2가 존재한다.

# # # 따라서 0행 2행을 가지고오게 된다.
# # # 이런식으로 적용하며
# # # True인값이 0 1 2이므로
# # # 012행을 가져오면서
# # # 모든 열을 다가져온다.
# # a[rows, :]


# # # filter를 거쳐서 가지고 올 수도 있다.

# # # 이런식으로 필터를 걸거나
# # # 현재 아래에서 적힌 식을 통해서
# # # true, false인 리스트가 만들어지고
# # filter = a % 2 ==0
# # # 이런식으로 만든다.
# # # 함수식에 따라 true인 값을
# # # 리스트로 만들어서
# # # b에 가져온다.
# # b = a[filter]

# # # searching은 매칭된 인덱스 요소를 반환함
# # arr = np.array([1,2,3,4,4,5,5])

# # # 4보다 큰 인덱스를 반환 .
# # x = np.where(arr > 4)

# # # searching을 통해서
# # # 가져온 것을 확ㅇ니해보면

# # # (array[], dtype)으로 가져오기 때문에
# # # x[0]
# # # 을 가지고 리스트를 꺼내사용할 수 있음


# # arr = np.array([[1,2,5,6], 
# #                 [5,4,4,5]])

# # # 만약 2차원에서 where를 하게 된다면

# # x = arr.where(arr > 4)
# # # 그럼 행과 열로 나눠진다.
# # # 행에는 조건에 맞는 것이 0행부터 몇개가 있는지를 검사하고
# # # 그 개수를 행번호로 채운다.
# # # 따라서 위 조건대로라면 arr >4 보다 큰 원소니까
# # # 행에는 2개가 있기 때문에 [0,0,1,1]
# # # 채워지게 되고, 1행 같은 경우 두객 ㅏ존재하므로
# # # 최종적으로 2차원에서 where를 이요해서
# # # 검사했을때 4보다 큰 원소가 0행에는 2개 1행에도 2개
# # # [0,0,1,1] 과 같이 생기는것을
# # # 확인할 수 있다.

# # # 이후 열은 해당 인덱스 번호를 기준으로 하게 되고
# # # 행에서 몇번째 인덱스에 존재하는지기ㅏ 열로 잡힌다.

# # # 따라서 0행에서먼저보면 2, 3이 존재
# # # 1행 0,3이 존재
# # # [2,3,0,3] 이 완성되는것.
# # # 그럼 이제 이걸 꺼내서 쓰기 위해ㅓㅅ

# # x[0], x[1]
# # # 각각 행과 열로 꺼내서 쓰면
# # # 이후부터는 자유롭게 사용가느 


# import numpy as np

# a = np.arange(24).reshape(2,3,4)

# # 2면이니까
# # 1면,1면 나오게 된거고
# for item in a:
#     print(item)
    
# # 첫번째 면을 먼저 선택한 것이므로
# # 첫번째 면에서의 3행들을 가지고 오겠
# for item in a[0]:
#     print(item)
    
# for i in range(len(a)):
#     # 면을 가지고 오겠지
    
#     # 두개의 면이 존재하니
#     # 첫번째면의 첫번째 행들을 가지고 올거지 
#     a[i][0]
    
# # 편평화 작업을해줌
# a.flat

import numpy as np
a= np.arange(3).reshape(3, 1)
b = np.arange(3)
# 3,1 과 1,3 이 있을때
# 이건 브로드캐스팅 연산이 가능한데
# 합치는건 가능할까
# 우선 vstck()인경우 열의 개수가 같아야하는데
# 현재 같지 않고 있음  
# 이런 경우 vstack이 적용안됨
# 브로드캐스팅은 연산시에 적용되는것이기 때문에
# vs = np.vstack((a, b))
# print(vs)

# 마찬가지로 hastack도 사용불가능


# vsplit(), hsplit()
# 수직으로 분리하는거고
# # 수평으로 hsplit()하는것임
# # vs = np.hstack((a,b))

# # 몇개로 나눌건지
# # 단 이때 나눠질때 동일하게 나누어져야함
# # 6행 4열을 vstack으로 자른다면
# # 수직으로 잘라야 하니까
# # 행을 기준으로 보면 2로 나누면 3행 3행씩
# # 분리될것을 알 수있음
# # 만약 3으로 하게 된다면 2행씩 나눠지고
# # 6으로 하게 되면 1하나씩 나눠질것임
# vs = np.arange(24).reshape(6,4)
# # 그럼 총 6개가 나오게 되니까
# # 감싸져서 나오는것을 확인할 수 이음
# for i in np.vsplit(vs, 6):
#     # split하고 사용하려면 i[0]에 접근한뒤 사용해야함
#     print(i[0])

# # hsplit도 마찬가지의 원리임
# # dhzpdl
# for i in np.hsplit(vs, 2):
#     print(i[0])
    
# 오케이이이

# n* n단위행렬을 만들어주고
# a = np.eye(3)
# print(a)

# a = np.transpose(a, s)
# # 만약 대각원소를 구해야한다
# # 이런식으로 구하면되고
# np.diag(a)
# # 대각원소의 합임
# np.trace(a)

# # 역행렬을 구해야 한다면


# # 차례로 역행렬
# # 행렬식임
# np.linalg.inv()
# np.linalg.det()
# # 전치행렬은 a.T로도 쓸 수 있음

# # 행이 열로 바뀌는것
# a.T

# 0 1 2번축이 2 1 0번으로 바꾸니다?
# 
# b = np.arange(32).reshape(2, 4,4)
# print(f"{b}\n")
# print(b.T)

a = np.random.random_sample((3, 4))
print(a)
# np.argmax(a) 는
# 현재 배열에서 가장 큰 값의 인덱스를 반
# 이때 1차원으로 생각해서 반환함

print(np.argmax(a))
agmp = np.argmax(a, axis = 0)
# axis = 0으로 지정했기 때문에 axis = 0방향에서
# axis = 0방향으로 탐색해나가면서
# 가장 큰 값을 표현함 즉 위에서 아래로 표현하게 되면
# 0 , 1, 2이런식으로

#  
# 이건 axis = 1방향 쪽으로 찾게 되는데
# 똑같은 원리로
# axis = 1방향으로 큰 인덱스를 찾음

ag = np.argmax(a, axis=1)

# ad-bc 가 == 0이면 역행렬이 없음
# 역행렬은 1/ad-bc [d -b -c a]