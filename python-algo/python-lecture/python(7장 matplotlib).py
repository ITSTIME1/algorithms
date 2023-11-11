import matplotlib.pyplot as plt
import matplotlib.markers as mark
import numpy as np




# data = 
data = np.array([50,125,300,150,400])

# bar는 두개의 값을 둘다 인수로 넘겨주어야함

# 0~4까지의 수생성
# index = x, y
# plot(x, y)
# 만약 x, y둘 중 하나만 지정할 경우 
# y로 간주, x자동생성
# plt.plot(range(len(data)), data)

# arange 선형값 생성
# 0~ 3 * np.pi - 1까지의 데이터를 0.1 간격으로 설정
# 0, 9.42
# x = np.arange(0, 6*np.pi, 0.1)
# print(x)

# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, marker=11)
# plt.plot(x, y2)
# plt.plot()
# plt.show()



# matplotlib ndarray를 기본으로 사용
# x, y를 넣어서 그림
# 1inch = 300개찍음 
# 단위
# 27inch = 8100
plt.figure(dpi=70)
# plt.plot(range(100, 0, -1), 
# 				np.linspace(-1, 2, 100))
# plt.show()


# bar 데이터
# plt.bar(range(len(data)), 5)
# plt.barh(range(len(data)), 5)
# plt.show()


# 100, 
ndarray = np.arange(200).reshape(100, 2)
p = np.random.rand(ndarray.shape[0], ndarray.shape[1])
# p[:,0] ? 모든행, 열은 0번열
# p[:,1] 모든행 1번열
# x, y
# float, array
# plt.scatter(p[:,0], p[:,1])
# plt.show()
# print(p)





labels = ['Samsung', 'Huawei', 'Apple', 'Xiaomi', 'Oppo', 'Etc'] 
sizes = [20.4, 15.8, 10.5, 9, 7.6, 36.7]
# 원점으로 떨어진 거리
explode = [0.1, 0.2, 0.3, 0.4, 0.5, 6.6]
# print(explode)

# 폰트추가
plt.rc('font', family="AppleGothic", weight=10)
# title
plt.title("테스트", loc='center', fontsize=30, pad=10)
# x레이블
plt.xlabel("test - x")
# y레이블
plt.ylabel("test - y")
# 파이차트
plt.pie(sizes, explode=explode, 
	# 레이블
	labels=labels, 
	# autopct = 소수점 이하 자릿수
	# 정수는 한자리 소수점은 최대한자리로
	autopct='%5.1f%%', 
	shadow=True, 
	# 시계 반대방향으로 배치
	# start angle = 12시방향
	# 진행방향은 반대방향으로
	startangle=90)

plt.show()

print("%20.5f", 123.4152)




