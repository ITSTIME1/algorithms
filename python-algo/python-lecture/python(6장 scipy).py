import numpy as np
from scipy.linalg import *
import matplotlib.pyplot as plt
from scipy.optimize import fmin_bfgs

a = np.arange(9).reshape(3, 3)
print(a)


# 방정식 미지수의 계수를 행렬로 만듬
# 이후 방정식 값을 행벡터로 만들어줌
# solve()함수를 통해서 계산
A = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]]) 
B = np.array([2, 4, -1]) # 열벡터

# 연립방정식을 풀기위한 함수
# print(solve(A, B))


# x = np.linspace(-1, 1, 101)
# plt.plot(x, np.exp(-x))
# plt.show()



# def f(x):
# 	return x**2 + 10*np.sin(x)
# print(fmin_bfgs(f, 0)) # 0에서 시작해서 탐색 print(fmin_bfgs(f, 6)) # 6에서 시작해서 탐색

x = np.linspace(1, 4, 5)
y = [1.5, 3.1, 4.2, 5.8, 7.3] 
plt.plot(x, y, 'o') 
plt.show()